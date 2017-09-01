from scapy.all import *
from keys import * 
from distance import get_travel_time
from text import send_text
import math
import datetime

MAC_ADDRESS = '68:37:e9:5a:e3:d0'

def get_times():
    travel_time = get_travel_time()
    now = datetime.datetime.now()
    arrival = now + datetime.timedelta(seconds = travel_time)
    return datetime.datetime.strftime(arrival, '%I:%M %p') #formats to 06:30 PM

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc ==  MAC_ADDRESS:
            print ('dash button pressed!')
            send_text(get_times())

print (sniff(prn=arp_display, filter='arp', store=0, count=0))
