import PyPDF2
import os
import glob
from concurrent.futures import ThreadPoolExecutor
import threading
import csv
# 获取当前文件夹路径
current_folder = os.path.dirname(os.path.abspath(__file__))

# 使用glob模块查找所有.txt文件
txt_files = glob.glob(os.path.join(current_folder, '*.pdf'))

# addList = ['环保补贴', '绿色补贴', '税收优惠', '绿色信贷', '专项基金', '减免税', '环保专项资金', '政府补助', '鼓励探索', '财政扶持',
#            '环境宽松', '环境合规', '未被列为重点监管对象', '弹性监管', '优化监管', '环境友好', '环保奖励', '绿色信贷',
#            '环境债券', 'ESG', '资源投入', '环保设备升级', '技术应用', '污染治理设施', '清洁能源']

# reduceList = ["环境监管", "环境监测", "环保督察", "突击检查", "挂牌督办", "约谈问责", "限期整改", "在线监测联网",
#               "实时数据上传", "环境审计", "环境处罚", "专项检查", "舆论压力", "专项检查", "实时监控", "排放标准",
#               "排污许可", "超低排放", "特别限值", "总量控制", "区域限批", "零容忍", "攻坚战", "社会关注", "舆论压力"]

List1=["数字化转型", "大数据", "人工智能", "物联网", "云计算", "区块链", "数字化技术", "数字化平台", "智能生产", "智能制造", "数据驱动", "信息化",
      "绿色发展", "环境保护", "绿色专利", "节能减排", "清洁能源", "可再生能源", "资源回收", "污染治理", "生态保护", "绿色供应链", "绿色产品", "碳排放",
      "创新驱动", "技术创新", "研发投入", "创新能力", "创新成果", "专利申请", "新产品开发", "新工艺", "新服务模式"]
List2=['数字化绿色创新','绿色数字化转型','智能能效管理','数字环保技术','智能节能减排系统','数字化可再生能源管理','区块链绿色供应链']
# 得分函数
def process_file(file):
    score = 0
    with open(file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # 获取PDF文件的页数
        num_pages = pdf_reader.numPages
        # 遍历每一页并提取文本
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            content = page.extractText()
            for i in List1:
                start = 0
                while True:
                    index = content.find(i, start)
                    if index == -1:
                        break
                    score += 1
                    start = index + len(i)
            for i in List2:
                start = 0
                while True:
                    index = content.find(i, start)
                    if index == -1:
                        break
                    score =score+2
                    start = index + len(i)
            # for i in reduceList:
            #     start = 0
            #     while True:
            #         index = content.find(i, start)
            #         if index == -1:
            #             break
            #         score -= 1
            #         start = index + len(i)
    return score

# 使用多线程处理所有文件
def main():
    final_scores = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 提交任务到线程池
        futures = [executor.submit(process_file, file) for file in txt_files]
        for future in futures:
            # 获取每个文件的得分
            final_scores.append(future.result())
    

    with open('这次文件数字化得分.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['文件名','得分'])
        for file, score in zip(txt_files, final_scores):
            writer.writerow([file,score])
            # print(f"文件: {file}, 得分: {score}")

if __name__ == "__main__":
    main()

