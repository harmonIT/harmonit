package main

import (
	"encoding/binary"
	"errors"
	"fmt"
	"github.com/goccy/go-json"
	"harmonit/src/common/message"
	"io"
	"net"
)


func main() {
	fmt.Println("Listen to 18888")
	listen, err := net.Listen("tcp", "127.0.0.1:18888")
	defer listen.Close()
	if err != nil {
		fmt.Println("Listen error=",err)
		return
	}
	for{
		fmt.Println("wait for connection")
		conn, err := listen.Accept()
		if err != nil {
			fmt.Println("listen.Accept error=",err)

		}
		go Process(conn)
	}

}
func Process(conn net.Conn){
	defer conn.Close()
	for{
/*		buf:=make([]byte,8096)
		fmt.Println("读取数据中。。。")
		_,err:=conn.Read(buf)
		if err!=nil{
			fmt.Println("conn Read error=",err)
			return
		}
		fmt.Println("读到的buf为",buf[:4])*/
		mes, err := readPkg(conn)
		if err != nil {
			if err==io.EOF{
				fmt.Println("客户端退出")
				return
			}else {
				errors.New("readPkg(conn) error")
				return
			}
		}
		fmt.Println("接收到的消息为",mes)
	}

}
func readPkg(conn net.Conn) (mes message.Message,err error){
	buf:=make([]byte,8096)
	fmt.Println("读取数据中。。。")
	_,err=conn.Read(buf[:4])
	if err!=nil{
		fmt.Println("conn Read error=",err)
		return
	}
	var pkgLen uint32
	pkgLen = binary.BigEndian.Uint32(buf[:4])
	n, err := conn.Read(buf[:pkgLen])
	if uint32(n) != pkgLen ||err!=nil{
		fmt.Println("conn Read(buf[:pkgLen]) error=",err)
		return
	}
	//反序列化成message.Message
	err = json.Unmarshal(buf[:pkgLen], &mes)//!!!!结构体是值传递，必须加取值符
	if err != nil {
		fmt.Println("json.Unmarshal(buf[:pkgLen], &mes) error=",err)
		return

	}
	return mes,err
}












