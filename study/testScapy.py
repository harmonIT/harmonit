from scapy.all import *

# 定义一个回调函数来处理每个数据包
def handle_packet(packet):
    # 打印数据包的摘要信息
    print(packet.summary())
    
    # 详细解析数据包
    print("详细解析数据包:")
    packet.show()


# 捕获一个数据包
packet = sniff(iface="Realtek PCIe GbE Family Controller", prn=handle_packet,filter='tcp port 80 or tcp port 443')
