# -*- coding: utf-8 -*-
import pcap
import dpkt
pc=pcap.pcap()    #注，参数可为网卡名，如eth0
pc.setfilter('tcp port 80')    #设置监听过滤器
for ptime,pdata in pc:    #ptime为收到时间，pdata为收到数据
    print ptime,pdata    #...