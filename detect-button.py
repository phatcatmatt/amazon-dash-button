from scapy.all import *
from keys import * 
from distance import travel_time
from text import send_text
import math

MAC_ADDRESS = '68:37:e9:5a:e3:d0'

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc ==  MAC_ADDRESS:
            print ('dash button pressed!')
            time = math.ceil(travel_time()/60)
            print (str(time) + ' minutes')
            send_text(time)

print (sniff(prn=arp_display, filter='arp', store=0, count=0))
