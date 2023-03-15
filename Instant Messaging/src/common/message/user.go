package message
type User struct {
	UserId int `json:"userId"`//此操作保证序列化为此名称
	UserPwd string `json:"userPwd"`
	UserName string `json:"userName"`
}
