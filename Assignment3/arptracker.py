import dpkt,socket
f=open("arp-storm.pcap","rb")
pcap = dpkt.pcap.Reader(f)
count=0
for ts,bufffer in pcap:
 count+=1
 print "\n"
 print "processing packet ",count
 eth=dpkt.ethernet.Ethernet(bufffer)
 print "source address=",(eth.src).encode("hex")
 print "destination address=",(eth.dst).encode("hex")
 print "operation=",eth.data.op
 print "source hardware address=",(eth.data.sha).encode("hex")
 print "target hardware address=",(eth.data.tha).encode("hex")
 print "source protocol address=",socket.inet_ntoa(eth.data.spa)
 print "target protocol address=",socket.inet_ntoa(eth.data.tpa)

 
f.close()
