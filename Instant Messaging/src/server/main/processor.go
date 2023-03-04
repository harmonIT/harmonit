package main

import (
	"common/message"
	"errors"
	"fmt"
	"io"
	"net"
	"server/process"
	"server/utils"
)
type Processor struct {
	Conn net.Conn
}

//总控制器
//根据客户端发送的消息种类，判断用什么函数处理
func (this *Processor) serverProcessMes(mes *message.Message) (err error){
	switch mes.Type {
	case message.LoginMessageType:
		//处理登录
		up:=&process.UserProcess{
			Conn: this.Conn,
		}
		err := up.ServerProcessLogin(mes)
		if err != nil {
			fmt.Println("up.ServerProcessLogin(mes) error=",err)
			return err
		}
	case message.RegisterMessageType:
		//处理注册
	default:
		fmt.Println("无法识别用什么函数处理请求")

	}
	return err
}
func (this *Processor) process2() (err error){

	for{
		/*		buf:=make([]byte,8096)
				fmt.Println("读取数据中。。。")
				_,err:=conn.Read(buf)
				if err!=nil{
					fmt.Println("conn Read error=",err)
					return
				}
				fmt.Println("读到的buf为",buf[:4])*/
		tf:=&utils.Transfer{
			Conn: this.Conn,
		}
		mes, err := tf.ReadPkg()
		if err != nil {
			if err==io.EOF{
				fmt.Println("客户端退出")
				return err
			}else {
				errors.New("readPkg(conn) error")
				return err
			}
		}
		err = this.serverProcessMes(&mes)
		if err != nil {
			fmt.Println("serverProcessMes(conn, &mes) error=",err)
			return err
		}
		fmt.Println("接收到的消息为",mes)
	}
}









