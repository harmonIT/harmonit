package main

import (
	"fmt"
	"net"
	"server/model"
	"time"
)


func main() {
	initPool("localhost:6379",16,0,time.Second*300)
	initUserDao()
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
	processor:=&Processor{
		Conn:conn,
	}
	err := processor.process2()
	if err != nil {
		fmt.Println("goroutine error=",err)
		return
	}
}
func initUserDao(){
	model.MyUserDao=model.NewUserDao(pool)//这里的pool是全局变量
}













