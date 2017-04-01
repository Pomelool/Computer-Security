import dpkt
import sys
import socket


# some maps
mapSyn = {}
mapSynAck ={}

# read in pcap file
pktAnalysis = dpkt.pcap.Reader(open(str(sys.argv[1])))

# iterate thorough each packet
for ts, buf in pktAnalysis:
    try: ethPkt = dpkt.ethernet.Ethernet(buf)
    except dpkt.UnpackError or AttributeError: continue
    
    # if it's ip packet
    if ethPkt.type == dpkt.ethernet.ETH_TYPE_IP:
        ipPkt = ethPkt.data
        # if it's tcp packet
        if(ipPkt.p == dpkt.ip.IP_PROTO_TCP):
            tcpPkt = ipPkt.data
            # print "ip src: " + ipSrc + "ip.dst: " + ipDst
            ipSrc = socket.inet_ntoa(ipPkt.src)
            ipDst = socket.inet_ntoa(ipPkt.dst)
            if tcpPkt.flags & dpkt.tcp.TH_SYN != 0:
                if tcpPkt.flags & dpkt.tcp.TH_ACK != 0:
                    if ipDst not in mapSynAck :
                        mapSynAck[ipDst] = 0
                    mapSynAck[ipDst] += 1
                else:
                    if ipSrc not in mapSyn :
                        mapSyn[ipSrc] = 0
                    mapSyn[ipSrc] += 1
for ip_addr in mapSyn:
    if ip_addr not in mapSynAck :
        mapSynAck[ip_addr] = 0
    if(mapSyn[ip_addr] > mapSynAck[ip_addr] * 3):
        print ip_addr


#ipSrc = socket.inet_ntoa(ipPkt.src)
#ipDst = socket.inet_ntoa(ipPkt.dst)