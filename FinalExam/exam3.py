from scapy.all import *

packets = rdpcap ("TeddyBallgame.pcap")

# 1. Query 1: Calculate the number of Echo Requests received from 192.168.100.2
count = 0
test_count = 0
for i in packets:
    if i.haslayer("ICMP") and i["IP"].src == "192.168.100.2" and i['ICMP'].type == 8:
        count+=1
print ("Echo Requests received from 192.168.100.2 =", count)

# 2. Query 2: Calculate the number of Echo Request bytes (total frame size) and data (ICMP payload size) sent to 192.168.200.2
total_bytes = 0
total_data_bytes = 0
ethernet_header = 14
ip_header = 20
icmp_header = 8
for i in packets:
    if i.haslayer("ICMP") and i["IP"].dst == "192.168.200.2" and i["ICMP"].type == 8:
        total = len(i)
        total_bytes+=total
        total_data_bytes+=(total - ethernet_header - ip_header - icmp_header)
print ("Echo Request bytes sent to 192.168.200.2 =", total_bytes)
print ("Echo Request bytes sent to 192.168.200.2 =", total_data_bytes)

# Bonus: Specified number of course evaluations completed by the class
# Everybody completed their course evaluations