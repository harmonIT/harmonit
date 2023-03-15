package message

const (
	LoginMessageType = "LoginMessage"
	LoginResponseType="LoginResponse"
	RegisterMessageType="RegisterMessage"
	RegisterResMesType="RegisterResMes"
)

type Message struct {
	Type string`json:"type"`
	Data string`json:"data"`
}
type LoginMessage struct {
	UserId int`json:"userId"`
	UserPwd string`json:"userPwd"`
	UserName string`json:"userName"`
}
type LoginResponse struct {
	Code int`json:"code"`
	Error string`json:"error"`
}
type RegisterMessage struct {
	User User`json:"user"`
}
type RegisterResMes struct {
	Code int`json:"code"`
	Error string`json:"error"`
}
