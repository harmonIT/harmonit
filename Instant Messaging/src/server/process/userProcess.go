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
	userId int
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
		this.userId=loginMes.UserId
		//将登陆成功的用户id，赋给this
		userMgr.AddOnlineUser(this)
		//通知其他用户，此用户上线了
		this.NotifyOtherOnlineUser(loginMes.UserId)
		//将这些id储存到登录响应消息结构体里面的字段里，
		for id,_:=range userMgr.onlineUsers{
			loginResMes.UserIds=append(loginResMes.UserIds,id)
		}

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
	data, err := json.Marshal(registerResMes)
	if err != nil {
		fmt.Println("json.Marshal(registerResMes) error=",err)
		return
	}
	resMes.Data=string(data)
	data, err = json.Marshal(resMes)
	if err != nil {
		fmt.Println("json.Marshal(resMes) error=",err)
		return
	}
	//序列化好后，发送数据
	tf:=&utils.Transfer{
		Conn: this.Conn,
	}
	err = tf.WritePkg(data)
/*	if err != nil {
		fmt.Println("tf.WritePkg(data) error",err)
		return
	}*/
	return
}

func (this *UserProcess) NotifyOtherOnlineUser(userId int){
	for id,up:=range userMgr.onlineUsers{
		if id==userId{
			continue
		}
		up.NotifyMeOnline(userId)
	}
}
func (this *UserProcess) NotifyMeOnline(userId int) {

	//组装我们的NotifyUserStatusMes
	var mes message.Message
	mes.Type = message.NotifyUserStatusMesType

	var notifyUserStatusMes message.NotifyUserStatusMes
	notifyUserStatusMes.UserId = userId
	notifyUserStatusMes.Status = message.UserOnline

	//将notifyUserStatusMes序列化
	data, err := json.Marshal(notifyUserStatusMes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}
	//将序列化后的notifyUserStatusMes赋值给 mes.Data
	mes.Data = string(data)

	//对mes再次序列化，准备发送.
	data, err = json.Marshal(mes)
	if err != nil {
		fmt.Println("json.Marshal err=", err)
		return
	}

	//发送,创建我们Transfer实例，发送
	tf := &utils.Transfer{
		Conn : this.Conn,
	}

	err = tf.WritePkg(data)
	if err != nil {
		fmt.Println("NotifyMeOnline err=", err)
		return
	}
}














