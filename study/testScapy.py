from scapy.all import *

# 捕获所有经过网卡的数据包（持续嗅探，直到手动停止）
packets = sniff(iface="Realtek PCIe GbE Family Controller", prn=lambda x: x.summary())
# print(conf.ifaces)