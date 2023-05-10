from scapy.all import *

packets = rdpcap ("packets.pcap")

# 1. Calculate the number of ICMP echo replies from 192.168.122.1
count = 0
for i in packets:
    if i.haslayer("ICMP") and i["IP"].src == "192.168.122.1":
        count+=1
print ("Total replies received from 192.168.122.1 =", count)

# 2. Calculate the total bytes received (frame length) of ICMP echo replies from 8.8.8.8
total_bytes = 0
for i in packets:
    if i.haslayer("ICMP") and i["IP"].src == "8.8.8.8":
        total_bytes+=len(i)
print ("Total reply bytes received from 8.8.8.8", total_bytes)

# 3. Calculate the total data bytes received (data inside the ICMP packet, excluding all headers) 
# of ICMP echo replies from 8.8.8.8
total_data_bytes = 0
ethernet_header = 14
ip_header = 20
icmp_header = 8
for i in packets:
    if i.haslayer("ICMP") and i["IP"].src == "8.8.8.8":
        total = len (i)
        total_data_bytes+=(total - ethernet_header - ip_header - icmp_header)
print ("Total reply data received from 8.8.8.8 =", total_data_bytes)
