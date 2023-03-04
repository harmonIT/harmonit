package process

import (
	"common/message"
	"encoding/json"
	"fmt"
	"net"
	"server/utils"
)
type UserProcess struct {
	Conn net.Conn
}

//处理登录请求的函数
func (this *UserProcess) ServerProcessLogin(mes *message.Message) (err error){
	var loginMes message.LoginMessage//此处拿到的一定是LoginMessage结构体
	err = json.Unmarshal([]byte(mes.Data), &loginMes)
	if err != nil {
		fmt.Println("json.Unmarshal([]byte(mes.Data), &loginMes) error=",err)
		return
	}
	var resMes message.Message
	resMes.Type=message.LoginResponseType
	var loginResMes message.LoginResponse
	if loginMes.UserId==100{
		loginResMes.Code=200
		fmt.Println("登录成功")
	}else {
		loginResMes.Code=500
		loginResMes.Error="用户不存在，请注册"

	}
	//将loginResMes序列化
	data, err := json.Marshal(&loginResMes)
	if err != nil {
		fmt.Println("json.Marshal(loginResMes) error=",err)
		return
	}
	resMes.Data=string(data)
	//对resMes序列化
	data, err = json.Marshal(&resMes)
	if err != nil {
		fmt.Println("json.Marshal(resMes) error=",err)
		return
	}
	//发送数据
	tf:=&utils.Transfer{
		Conn:this.Conn,
	}
	err = tf.WritePkg(data)
	return
}