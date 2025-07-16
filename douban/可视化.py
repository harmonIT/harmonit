import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
matplotlib.rcParams['axes.unicode_minus'] = False 
# 读取Excel文件
file_path = '清洗后的数据.xlsx'
df = pd.read_excel(file_path).head(20)

x = df.iloc[:, 0][::-1]  
y = df.iloc[:, 1][::-1]     
plt.figure(figsize=(15, 8))  
plt.plot(x, y, marker='o', linestyle='-', color='b')

plt.title('评论数折线图')
plt.xlabel('排名')
plt.ylabel('评论数')

plt.grid(True)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.show()
