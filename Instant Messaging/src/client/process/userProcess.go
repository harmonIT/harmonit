package process

import (
	"client/utils"
	"common/message"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"net"
	"time"
)
type UserProcess struct {

}
func (this *UserProcess) Login(userId int) (err error){
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
	//loginMes.UserPwd=userPwd
	//loginMes序列化
	data, err := json.Marshal(&loginMes)
	if err != nil {
		fmt.Println("json.Marshal error=",err)
		return
	}
	mes.Data=string(data)//字节转换成字符串给这个结构体实例的字段
	//mes序列化
	data, err = json.Marshal(&mes)
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

	time.Sleep(time.Second*5)//客户端发送完请求，等待服务端响应数据

	//创建连接对象实例，拿的一直是一个连接
	tf:=&utils.Transfer{
		Conn: conn,
	}
	mes, err = tf.ReadPkg()
	if err != nil {
		fmt.Println("readPkg(conn) error=",err)
		return
	}
	//将mes的Data反序列化为LoginResponse类型
	var loginResMes message.LoginResponse
	err = json.Unmarshal([]byte(mes.Data), &loginResMes)
	if err != nil {
		fmt.Println("json.Unmarshal([]byte(mes.Data), &loginResMes) error=",err)
		return
	}
	if loginResMes.Code==200{
		go serverProcessMes(conn)
		fmt.Println("login success")
		for{
			ShowMenu()
		}
	}else {
		fmt.Println(loginResMes.Error)
	}
	return err
}