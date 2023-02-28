package main

import (
	"encoding/binary"
	"fmt"
	"github.com/goccy/go-json"
	"harmonit/src/common/message"
	"net"
	"time"
)
var userId int
var userPwd string
func main() {
	var key int
	loop:=true
	for loop{
		fmt.Println("------------------Login in System----------------------")
		fmt.Println("1 Login in")
		fmt.Println("2 Sigh up")
		fmt.Println("3 Exit")
		fmt.Println("Choose 1 to 3")
		fmt.Scanf("%d\n",&key)//加换行符，只扫描一个数字
		switch key {
		case 1:
			fmt.Println("Login in")
			loop=false
		case 2:
			fmt.Println("Sigh up")
			loop=false
		case 3:
			fmt.Println("Exit")
			loop=false
		default:
			fmt.Println("error,enter again")
		}

	}
	if key==1{
		fmt.Println("Please enter id")
		fmt.Scanf("%d\n",&userId)
		fmt.Println("Please enter password")
		fmt.Scanf("%s\n",&userPwd)
		err := Login(userId, userPwd)
		if err != nil {
			fmt.Println("Login failure")
		}else{
			fmt.Println("Login success")
		}
	}

}

func Login(userId int,userPwd string) (err error){
	//fmt.Println(userId,userPwd)
	//连接服务器
	conn, err := net.Dial("tcp", "localhost:18888")
	if err != nil {
		fmt.Println("net.Dial error=",err)
		return err
	}
	defer conn.Close()
	var mes message.Message
	mes.Type= message.LoginMessageType
	//创建结构体对象
	var loginMes message.LoginMessage
	loginMes.UserId=userId
	loginMes.UserPwd=userPwd
	//loginMes序列化
	data, err := json.Marshal(loginMes)
	if err != nil {
		fmt.Println("json.Marshal error=",err)
		return
	}
	mes.Data=string(data)//字节转换成字符串给这个结构体实例的字段
	//mes序列化
	data, err = json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal error=",err)
		return
	}
	mes.Data=string(data)
	//data为发送的数据
	//先发送数据长度，防止丢包
	var pakLen uint32
	pakLen = uint32(len(data))
	var buf [4]byte
	binary.BigEndian.PutUint32(buf[0:4],pakLen)
	//发送长度
	n, err := conn.Write(buf[:4])
	if n!=4||err!=nil{
		fmt.Println("conn Write error",err)
		return
	}
	//发送消息
	_, err = conn.Write(data)
	if err != nil {
		fmt.Println("conn.Write(data) error",err)
		return
	}
	fmt.Printf("客户端发送消息长度ok,长度=%d,内容=%s",len(data),string(data))
	time.Sleep(time.Second*5)
	fmt.Println("sleep 5s")
	return err
}













