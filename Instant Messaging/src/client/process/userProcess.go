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
func (this *UserProcess) Login(userId int,userPwd string) (err error){
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
	fmt.Printf("客户端发送消息长度ok,长度=%d,内容=%s\n",len(data),string(data))

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
		fmt.Println("当前在线用户列表如下")
		for _,v:=range loginResMes.UserIds{
			if v==userId{
				continue
			}
			fmt.Println("用户id：\t",v)
		}
		fmt.Println()
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

func (this *UserProcess) Register(userId int,userPwd,userName string) (err error){
	//连接到服务器
	conn, err := net.Dial("tcp", "localhost:18888")
	if err != nil {
		fmt.Println("net.Dial(\"tcp\", \"localhost:18888\") error=",err)
		return
	}
	defer conn.Close()
	//通过conn连接实例，发送消息
	//创建结构体实例
	var mes message.Message
	mes.Type=message.RegisterMessageType
	var registerMes message.RegisterMessage
	registerMes.User.UserId=userId
	registerMes.User.UserPwd=userPwd
	registerMes.User.UserName=userName
	//将结构体实例序列化封装
	data, err := json.Marshal(registerMes)
	if err != nil {
		fmt.Println("json.Marshal(registerMes) error=",err)
		return
	}
	mes.Data=string(data)
	data, err = json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal(mes) error=",err)
		return
	}
	//写入和发送数据
	tf:=utils.Transfer{
		Conn:conn,
	}
	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("tf.WritePkg(data) error=",err)
		return
	}

	//处理返回的数据，看id和密码匹配是否成功
	var registerResMes message.RegisterResMes
	err = json.Unmarshal([]byte(mes.Data), &registerResMes)
	if err != nil {
		fmt.Println("json.Unmarshal([]byte(mes.Data), &registerResMes) error=",err)
		return
	}
	if registerResMes.Code==200{
		fmt.Println("注册成功,请重新登录")
		//os.Exit(0)

	}else{
		fmt.Println(registerResMes.Error)
		//os.Exit(0)
	}
	return

}












