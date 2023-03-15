package model

import (
	"common/message"
	"encoding/json"
	"fmt"
	"github.com/garyburd/redigo/redis"
)

var (
	MyUserDao *UserDao
)
type UserDao struct {
	pool *redis.Pool
}
//工厂模式
func NewUserDao(pool *redis.Pool) (userDao *UserDao){
	userDao=&UserDao{
		pool: pool,
	}
	return userDao
}
func (this *UserDao) getUserById(conn redis.Conn,id int) (user *User,err error){
	res,err:= redis.String(conn.Do("HGet","users",id))
	if err != nil {
		if err== redis.ErrNil {
			err= ERROR_USER_NOTEXISTS
		}
		return
	}
	user=&User{}
	err = json.Unmarshal([]byte(res), user)
	if err != nil {
		fmt.Println("json.Unmarshal([]byte(res), user) err=",err)
		return
	}
	return nil, nil
}
func (this *UserDao) Login(userId int,userPwd string) (user *User,err error){
	//从连接池取出一个连接
	conn:=this.pool.Get()
	defer conn.Close()
	user, err = this.getUserById(conn, userId)
	if err != nil {
		return
	}
	//这时证明这个用户是获取到.
	if user.UserPwd != userPwd {
		err = ERROR_USER_PWD
		return
	}
	return
}

func (this *UserDao) Register(user *message.User) (err error){
	conn := this.pool.Get()
	defer conn.Close()
	//调用redis的get，如果没有错，说明用户存在，不可注册
	_, err = this.getUserById(conn, user.UserId)
	if err == nil {
		err=ERROR_USER_EXISTS
		return
	}
	//此时说明用户不存在，可以注册
	//序列化
	data, err := json.Marshal(user)
	if err != nil {
		fmt.Println("json.Marshal(user) error=",err)
		return
	}
	//存入redis中
	_, err = conn.Do("HSet", "users", user.UserId, string(data))
	if err != nil {
		fmt.Println("conn.Do(\"HSet\", \"users\", user.UserId, string(data)) error=",err)
		return

	}
	return
}





