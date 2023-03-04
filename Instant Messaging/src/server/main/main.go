package main

import (
	"fmt"
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
	processor:=&Processor{
		Conn:conn,
	}
	err := processor.process2()
	if err != nil {
		fmt.Println("goroutine error=",err)
		return
	}

}














