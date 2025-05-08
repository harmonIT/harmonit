import redis

# 连接 Redis（默认本地 6379 端口，无密码）
r = redis.Redis(host='127.0.0.1')

#存储一个列表到 Redis
my_list = [f"item_{i}" for i in range(10)]
#rpush方法是将字符串推入redis的列表中
r.rpush("my_key", *my_list)

my_list2 = [f"item_{i}" for i in range(10)]
r.rpush("my_key", *my_list2)
#从 Redis 读取列表
retrieved_list = r.lrange("my_key", 0, -1)  # 获取全部元素
print(type(retrieved_list),[item.decode('utf-8') for item in retrieved_list])#redis里面存储以字节的形式，用utf-8解码读取主持字符串
#windows命令chcp 65001更改编码为utf-8