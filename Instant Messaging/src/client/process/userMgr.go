package process

import (
	"common/message"
	"fmt"
)
var onlineUsers map[int]*message.User=make(map[int]*message.User,10)

func updateUserStatus(notifyUserStatusMes *message.NotifyUserStatusMes){
	user,ok:=onlineUsers[notifyUserStatusMes.UserId]
	if!ok{
		user=&message.User{
			UserId:notifyUserStatusMes.UserId,
		}
	}
	user.UserStatus=notifyUserStatusMes.Status
	onlineUsers[notifyUserStatusMes.UserId]=user
	outputOnlineUser()
}

func outputOnlineUser(){
	fmt.Println("显示在线用户列表")
	for id, _ := range onlineUsers {
		fmt.Println("用户id:\t",id)
	}
}
