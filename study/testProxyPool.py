import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/?type=https").json()

def delete_proxy(proxy):
    requests.get(f"http://127.0.0.1:5010/delete/?proxy={proxy}")

# 获取代理
proxy = get_proxy().get("proxy")
print(f"获取到的代理: {proxy}")
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "cookie": "ASP.NET_SessionId=hbrpsq3poj4vrhbvv1scmedv; GASGOO_B2B_SEARCHKEY=gfkplMQHfUJfOdEll7Nbw5WLQ47fTVvQfj2AUEDowvXTFbhPG5mniA==; Hm_lvt_8e90480b1bf68ede548c407057660718=1746583791; HMACCOUNT=9982405386288C7A; cna=a045e65f6aa94062980064fc96a9515c; GASPSP_OUTER_URLREFER=https://i.gasgoo.com/supplier/Boom.aspx?cid=9425&page=2; _gid=GA1.2.1084810197.1746586565; _ga=GA1.1.1207433812.1746583791; .Gasgoo_FromAuthCookieName=EFC97A56EB3795A5A5B597B9D82269922185EB327A41C819E77F114AB7B4567F32B1DE87C7CC6436E84EF0AF8B35828696B6F6B1B755E393F829C8A8E765F331B3A5AA4C9DE80E0857C6EAF52D1B097BCCDC69F13943237FFDA2D85E351FCA96B0C92FD8537B73439722E2E6803580476790E38E298C6A6D4FDB99BE3C8386323120E5729E658FA03BEEF218AED335D4; GASGOO_SNS_USER=UserName=6h7frOCsoTGDBNKZtdkilQ==&Password=yAovM7c4Id5ah0XlwdzK9tq1jepK4sTNUGFDHuiIJcA=&isAutoLogin=uqiAyMXroYY=; GASGOO_SNS_USERID=oEpKRPaNMNE=; GASGOO_USER=https%3a%2f%2fc2.gasgoo.com%2faccount%2fimages%2fPerson.jpg%7c%e7%9b%96%e4%b8%96%e7%bd%91%e5%8f%8b_108b47e0fcda21e9%7c11477238%7cFalse%7cFalse%7cMinghua+%e9%99%88%7cQ3D%2fzYQnIBuT7rfCJRHmEA%3d%3d%7c1746586649319%7c0%7c1743994649; GASGOO_USER_EXPIRES=2025-05-21 10:57:29.3109 +08:00; GASGOO_SNS_NIO=NIOUser=0; GASGOO_SNS_USER_SALES_LOGIN=CN; _ga_3JW0F78HZ0=GS2.1.s1746586565$o1$g1$t1746586649$j0$l0$h0; Hm_lpvt_8e90480b1bf68ede548c407057660718=1746586692; _ga_GPM5E72JNY=GS2.1.s1746586486$o2$g1$t1746586695$j0$l0$h0",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://i.gasgoo.com/supplier/boom/c-9425/index-21.html",
    "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}
def test_():
    retry_count = 1
    while retry_count < 4:
        try:
            resp = requests.get('https://i.gasgoo.com/supplier/boom/c-9425/index-2.html', proxies={"http": f"http://{proxy}","https": f"http://{proxy}"})#这里的https仍然是http开头
            return resp.text[:2000]
        except Exception as e:
            print(f'第{retry_count}次尝试代理失败',e)
            retry_count += 1
    delete_proxy(proxy)
print(test_())
