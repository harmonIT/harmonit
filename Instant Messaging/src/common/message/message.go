package message

const (
	LoginMessageType = "LoginMessage"
	LoginResponseType="LoginResponse"
	RegisterMessageType="RegisterMessage"
)

type Message struct {
	Type string`json:"type"`
	Data string`json:"data"`
}
type LoginMessage struct {
	UserId int`json:"user_id"`
	UserPwd string`json:"user_pwd"`
	UserName string`json:"user_name"`
}
type LoginResponse struct {
	Code int`json:"code"`
	Error string`json:"error"`
}
type RegisterMessage struct {

}
