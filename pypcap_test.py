import pcap
# list all of the Internet devices
devs = pcap.findalldevs()
print devs, "\n"
pc = pcap.pcap(devs[4], promisc=True, immediate=True, timeout_ms=50)
# fiter http pcakets
pc.setfilter('tcp port 10000')
for ptime, pdata in pc:
    print(ptime, pdata)
