package main

import (
	"client/process"
	"fmt"
	"os"
)
var userId int
var userPwd string
var userName string
func main() {
	var key int
	//loop:=true
	for{
		fmt.Println("------------------Login in System----------------------")
		fmt.Println("1 Login in")
		fmt.Println("2 Sigh up")
		fmt.Println("3 Exit")
		fmt.Println("Choose 1 to 3")
		fmt.Scanf("%d\n",&key)//加换行符，只扫描一个数字
		switch key {
		case 1:
			fmt.Println("Login in")
			fmt.Println("Please enter id")
			fmt.Scanf("%d\n",&userId)
			fmt.Println("Please enter password")
			fmt.Scanf("%s\n",&userPwd)
			up:=process.UserProcess{}
			err := up.Login(userId,userPwd)
			//err := Login(userId, userPwd)
			if err != nil {
				fmt.Println("Login failure")
			}else{
				fmt.Println("Login success")
			}
			//loop=false
		case 2:
			fmt.Println("Sigh up")
			//loop=false
			fmt.Println("please enter id")
			fmt.Scanf("%d\n",userId)
			fmt.Println("please enter password")
			fmt.Scanf("%s\n",userPwd)
			fmt.Println("please enter name")
			fmt.Scanf("%s\n",userName)
			//创建一个注册结构体实例
			up:=process.UserProcess{}
			err := up.Register(userId, userPwd, userName)
			if err != nil {
				fmt.Println("up.Register(userId, userPwd, userName) error=",err)
				return
			}else {
				fmt.Println("success")
				return
			}
		case 3:
			fmt.Println("Exit")
			//loop=false
			os.Exit(0)
		default:
			fmt.Println("error,enter again")
		}

	}

}















