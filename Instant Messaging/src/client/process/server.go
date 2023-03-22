package process

import (
	"client/utils"
	"common/message"
	"encoding/json"
	"fmt"
	"net"
	"os"
)

func ShowMenu(){
	fmt.Println("---------------------Congratulation you login success------------------------")
	fmt.Println("1.show online user")
	fmt.Println("2.send message")
	fmt.Println("3.message link")
	fmt.Println("4.exit")
	var key int
	fmt.Scanf("%d\n",key)
	switch key {
	case 1:
		outputOnlineUser()
	case 2:
	case 3:
	case 4:
		os.Exit(0)
	default:
		fmt.Println("enter error")
	}

}
//keep in touch with server
func serverProcessMes(conn net.Conn){
	tf:=&utils.Transfer{
		Conn: conn,
	}
	for{
		fmt.Println("读取服务端发来的消息")
		mes, err := tf.ReadPkg()
		if err != nil {
			fmt.Println("tf.ReadPkg() error",err)
			return
		}
		switch mes.Type {
		case message.NotifyUserStatusMesType:
			var notifyUserStatusMes message.NotifyUserStatusMes
			json.Unmarshal([]byte(mes.Data), &notifyUserStatusMes)
			//把这个用户的信息，状态保存到客户map[int]User中
			updateUserStatus(&notifyUserStatusMes)
		default:
			fmt.Println("未知消息类型")
		}
		fmt.Printf("mes=%v\n",mes)

	}
}









