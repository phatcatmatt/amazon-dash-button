from scapy.all import *
from blinkrandom import blink

MAC_ADDRESS = '68:37:e9:5a:e3:d0'

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc ==  MAC_ADDRESS:
            print ("dash button pressed!")
            blink(24, 25)

print (sniff(prn=arp_display, filter="arp", store=0, count=0))
