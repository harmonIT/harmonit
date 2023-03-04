package process

import (
	"fmt"
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
		fmt.Println()
	case 2:
	case 3:
	case 4:
		fmt.Println("exited")
		os.Exit(0)
	default:
		fmt.Println("enter error")
	}

}
