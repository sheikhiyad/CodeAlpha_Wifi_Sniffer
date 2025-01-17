# Basic Wi-Fi Sniffer | Sheikh Iyad | CodeAlpha

import subprocess
from scapy.all import sniff
import time

count_ = 0
while True:
    packet = sniff(filter="ip", count=1)[0]     # sniffing one packet transfered in the network
    src_ip = packet["IP"].src                   # extracting Source IP
    dst_ip = packet["IP"].dst                   # extracting Destination IP

    print(f"Source IP: {src_ip} -> Destination IP: {dst_ip}")       # prints <SourceIP> -> <Destination IP>

    if (not src_ip.startswith("192.168.")):                     # two if Conditions
        print("Executing nslookup on the source IP.. ", src_ip)
        subprocess.Popen(["nslookup", src_ip])

    if not dst_ip.startswith("192.168."):
        print("Executing nslookup for destination IP.. ", dst_ip)
        subprocess.Popen(["nslookup", dst_ip])

    count_ = count_ + 1                           # counting the times the loop was executed and store in count.
    print("Number of times executed: ", count_)
    time.sleep(0.1)                               # using a pause break to avoid overloading the system





