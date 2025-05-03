'''
import os
import glob
import threading
from concurrent.futures import ThreadPoolExecutor
# 获取当前文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))

# 使用glob模块查找所有.txt文件
txt_files = glob.glob(os.path.join(current_folder, '*.txt'))
addList=['环保补贴', '绿色补贴', '税收优惠', '绿色信贷', '专项基金', '减免税', '环保专项资金', '政府补助', '鼓励探索', '财政扶持','环境宽松', '环境合规', '未被列为重点监管对象', '弹性监管', '优化监管', '环境友好', '环保奖励','绿色信贷', '环境债券', 'ESG', '资源投入', '环保设备升级', '技术应用', '污染治理设施', '清洁能源']
reduceList=["环境监管", "环境监测", "环保督察", "突击检查", "挂牌督办", "约谈问责", "限期整改", "在线监测联网", "实时数据上传", "环境审计", "环境处罚", "专项检查", "舆论压力", "专项检查", "实时监控", "排放标准", "排污许可", "超低排放", "特别限值", "总量控制", "区域限批", "零容忍", "攻坚战", "社会关注", "舆论压力"]
#得分函数
def process_file(file):
    score=0
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        for i in addList:
            start = 0
            while True:
                index = content.find(i, start)
                if index!=-1:
                    score+=1
                else:
                    break
                # 更新起始位置以便查找下一个匹配项
                start = index + len(i)
        for j in reduceList:
            start = 0
            while True:
                index = content.find(j, start)
                if index!=-1:
                    score-=1
                else:
                    break                   
                start = index + len(j)
    print(f"{file}的得分是{score}")
    return file,score
with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(process_file, txt_files)
'''
import os
import glob
from concurrent.futures import ThreadPoolExecutor
import threading
import csv
# 获取当前文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))

# 使用glob模块查找所有.txt文件
txt_files = glob.glob(os.path.join(current_folder, '*.txt'))

addList = ['环保补贴', '绿色补贴', '税收优惠', '绿色信贷', '专项基金', '减免税', '环保专项资金', '政府补助', '鼓励探索', '财政扶持',
           '环境宽松', '环境合规', '未被列为重点监管对象', '弹性监管', '优化监管', '环境友好', '环保奖励', '绿色信贷',
           '环境债券', 'ESG', '资源投入', '环保设备升级', '技术应用', '污染治理设施', '清洁能源']

reduceList = ["环境监管", "环境监测", "环保督察", "突击检查", "挂牌督办", "约谈问责", "限期整改", "在线监测联网",
              "实时数据上传", "环境审计", "环境处罚", "专项检查", "舆论压力", "专项检查", "实时监控", "排放标准",
              "排污许可", "超低排放", "特别限值", "总量控制", "区域限批", "零容忍", "攻坚战", "社会关注", "舆论压力"]

# 得分函数
def process_file(file):
    score = 0
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        for i in addList:
            start = 0
            while True:
                index = content.find(i, start)
                if index == -1:
                    break
                score += 1
                start = index + len(i)
        for i in reduceList:
            start = 0
            while True:
                index = content.find(i, start)
                if index == -1:
                    break
                score -= 1
                start = index + len(i)
    return score

# 使用多线程处理所有文件
def main():
    final_scores = []
    with ThreadPoolExecutor() as executor:
        # 提交任务到线程池
        futures = [executor.submit(process_file, file) for file in txt_files]
        for future in futures:
            # 获取每个文件的得分
            final_scores.append(future.result())
    

    with open('A得分.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['文件名','得分'])
        for file, score in zip(txt_files, final_scores):
            writer.writerow([file,score])
            # print(f"文件: {file}, 得分: {score}")

if __name__ == "__main__":
    main()
