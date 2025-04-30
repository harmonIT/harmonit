import os
import glob

# 获取当前文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))

# 使用glob模块查找所有.txt文件
txt_files = glob.glob(os.path.join(current_folder, '*.txt'))

# 遍历找到的.txt文件并读取内容
for file in txt_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        search_term = '应收账款'
        start = 0
        
        # 查找所有出现的“应收账款”
        while True:
            index = content.find(search_term, start)
            if index == -1:
                break
            
            start_index = index + len(search_term)
            end_index = start_index + 20
            result = content[start_index:end_index]
            print(f"文件名: {file}:{result}\n")
            
            # 更新起始位置以便查找下一个匹配项
            start = index + len(search_term)
