import redis
# 连接到 Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# 存储数据时使用 UTF-8 编码
data = "这是一个测试字符串"
r.set('test_key2', data.encode('gbk'))

# # 读取数据时使用 UTF-8 解码
# retrieved_data = r.get('test_key').decode('utf-8')
# print(retrieved_data)
