package process

import (
	"common/message"
	"encoding/json"
	"fmt"
	"net"
	"server/model"
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
	user, err := model.MyUserDao.Login(loginMes.UserId, loginMes.UserPwd)
	if err != nil {
			if err == model.ERROR_USER_NOTEXISTS {
				loginResMes.Code = 500
				loginResMes.Error = err.Error()
			} else if err == model.ERROR_USER_PWD  {
				loginResMes.Code = 403
				loginResMes.Error = err.Error()
			} else {
				loginResMes.Code = 505
				loginResMes.Error = "服务器内部错误..."
			}
	}else {
		loginResMes.Code=200
		fmt.Println(user,"登录成功")
	}
	/*	if loginMes.UserId==100{
		loginResMes.Code=200
		fmt.Println("登录成功")
	}else {
		loginResMes.Code=500
		loginResMes.Error="用户不存在，请注册"

	}*/
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

func (this *UserProcess) ServerProcessRegister(mes *message.Message) (err error){
	//声明注册结构体，将反序列化后的结构体存入注册结构体
	var registerMes message.RegisterMessage
	err = json.Unmarshal([]byte(mes.Data), &registerMes)
	//声明消息结构体，存入类型
	var resMes message.Message
	resMes.Type=message.RegisterResMesType
	//声明注册响应结构体，
	var registerResMes message.RegisterResMes
	//向数据库redis中存入数据
	err = model.MyUserDao.Register(&registerMes.User)
	if err != nil {
		if err==model.ERROR_USER_EXISTS{
			registerResMes.Code=505
			registerResMes.Error=model.ERROR_USER_EXISTS.Error()
		}else {
			registerResMes.Code=506
			registerResMes.Error="注册未知错误"
		}
	}else {
		registerResMes.Code=200
	}
	//处理好注册响应结构体的实例后，将数据序列化到注册结构体中
	rdata, err := json.Marshal(registerResMes)
	if err != nil {
		fmt.Println("json.Marshal(registerResMes) error=",err)
		return
	}
	resMes.Data=string(rdata)
	data, err := json.Marshal(resMes)
	if err != nil {
		fmt.Println("json.Marshal(resMes) error=",err)
		return
	}
	//序列化好后，发送数据
	tf:=utils.Transfer{
		Conn: this.Conn,
	}
	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("tf.WritePkg(data) error",err)
		return
	}
	return
}

















