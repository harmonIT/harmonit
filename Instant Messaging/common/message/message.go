package harmonit

const (
	LoginMessageType = "LoginMessage"
	LoginResponseType="LoginResponse"
)

type Message struct {
	Type string
	Data string
}
type LoginMessage struct {
	UserId int
	UserPwd string
	UserName string
}
type LoginResponse struct {
	Code int//状态码
	Error string
}
