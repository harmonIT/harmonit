package utils

import (
	"common/message"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"net"
)
type Transfer struct {
	Conn net.Conn
	Buf [8096]byte
}
func (this *Transfer) ReadPkg() (mes message.Message,err error){
	fmt.Println("读取数据中。。。")
	_,err=this.Conn.Read(this.Buf[0:4])
	if err!=nil{
		//fmt.Println("conn Read error=",err)
		return
	}
	var pkgLen uint32
	pkgLen = binary.BigEndian.Uint32(this.Buf[0:4])

	n, err := this.Conn.Read(this.Buf[:pkgLen])
	if n!= int(pkgLen) || err!=nil{
		//fmt.Println("conn Read(buf[:pkgLen]) error=",err)
		return
	}
	if pkgLen==0{
		fmt.Println("pkgLen==0")
		return
	}
	//反序列化成message.Message
	err = json.Unmarshal(this.Buf[:pkgLen], &mes) //!!!!结构体是值传递，必须加取值符
	if err != nil {
		fmt.Println("json.Unmarshal(buf[:pkgLen], &mes) error=",err)
		return

	}
	return mes,err
}


func (this *Transfer) WritePkg(data []byte) (err error){
	//先发送消息长度
	var pkgLen uint32
	pkgLen = uint32(len(data))
	//var buf [4]byte
	binary.BigEndian.PutUint32(this.Buf[:4],pkgLen)
	n, err := this.Conn.Write(this.Buf[:4])
	if n!=4||err != nil {
		fmt.Println("writePkg conn.Write(buf[:4]) error=",err)
		return
	}
	//发送数据
	n, err = this.Conn.Write(data)
	if uint32(n)!=pkgLen || err != nil {
		fmt.Println("writePkg conn.Write(buf[:4]) error=",err)
		return
	}
	return
}