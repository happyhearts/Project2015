import dpkt,socket
f=open('tcp-ecn-sample.pcap','rb')
pcap = dpkt.pcap.Reader(f)
count=0
for ts,buffr in pcap:
 try:
   print "\n"
   eth=dpkt.ethernet.Ethernet(buffr)
   print "source address=",(eth.src).encode("hex") 
   print "destination address=",(eth.dst).encode("hex") 
   ip=eth.data
   if ip.p==dpkt.ip.IP_PROTO_TCP:
     count=count+1
     print "analyzing IP packet ",count
     print "tos=",ip.tos
     print "source address=",socket.inet_ntoa(ip.src)
     print "destination address=",socket.inet_ntoa(ip.dst)
     tcp=ip.data
     print "source port=",tcp.sport
     print "destination port=",tcp.dport
     print "urgent pointer=",tcp.urp
     print "seq =",tcp.seq
     print "ack",tcp.ack
     
 except dpkt.dpkt.NeedData: 
   print "EOF reached "
 
