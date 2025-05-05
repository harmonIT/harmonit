import matplotlib.pyplot as plt

# 假设列表1和列表2已经定义
列表1 = [1, 2, 3, 4, 5]  # 这将是你的横坐标数据
列表2 = [2, 3, 5, 7, 11] # 这将是你的纵坐标数据

# 绘制折线图
plt.plot(列表1, 列表2, marker='o')  # 'marker' 参数是可选的，用于在每个数据点上添加标记

# 添加标题和标签
plt.title('Data Analysis')
plt.xlabel('price')
plt.ylabel('sale')

# 显示图形
plt.show()
