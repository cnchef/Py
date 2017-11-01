#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/17 17:47
# @Author  : chenf
# @Site    : 
# @File    : ipcheck.py
# @Software: PyCharm

import requests
import json
import urllib.request
import time
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
'''
import urllib.requests
import json
import time
#import sys

url = 'http://ip.taobao.com/service/getIpInfo.php?ip='

def checkTaobaoIP(ip):
    try:
        response = urllib.urlopen(url + ip, timeout=5)
        result = response.readlines()
        data = json.loads(result[0])
        return "%15s: %s-%s-%s" % (ip,data['data']['isp'],data['data']['region'],data['data']['city'])
    except:
        return "%15s: timeout" % ip

if __name__ == "__main__":
    f = open('C:\\Users\\Administrator\\Desktop\\ip.txt')
    ips = f.readlines()
    f.close()

    f = open('ip-check.txt', 'w')
    for ip in ips:
        line = checkTaobaoIP(ip.strip())
        if line:
            print (line.encode('utf-8'))
            f.write(line+'\n')
        else:
            print (line)
            f.write(line+'\n')
    f.close()
    print ("Done!")
'''




def lookup(ip):
    URL = "http://freeapi.ipip.net/" + ip
    try:
       r = requests.get(URL,timeout=3)
    except requests.RequestException as e:
        print(e)

    json_data = r.json()
    print('查询IP信息如下：' + ip, '\t''所在国家：' + json_data[0],'\t''所在省份：' + json_data[1],'\t''所在城市：' + json_data[2])
    return (ip)

'''
    json_data = r.json()
    print('查询IP信息如下：' + ip)
    print('所在国家：' + json_data[0])
    print('所在省份：' + json_data[1])
    print('所在城市：' + json_data[2])
    return (ip)
'''


try:
    if __name__ == "__main__":
        Ipfile = open("C:\\Users\\Administrator\\Desktop\\ip.txt",'r')
        #Ipfileline = Ipfile.readlines()
        #Ipfile.close()
    for Ip in Ipfile:
        time.sleep(1)
        #Ipline = lookup(Ip.strip())
        lookup(Ip.strip())
        #print("Done!")
        #with open('C:\\Users\\Administrator\\Desktop\\ipinfo.txt', 'ab', encoding='utf8') as f:
            #f.write(Ip + '\n')
            #f.close()
finally:
    Ipfile.close()
    print('Cleaning up...closed the file')

'''
    while 1:
        line = Ipfile.readline()
        time.sleep(1)
        lines = lookup(line.strip())
        #print(lines)
        #with open('C:\\Users\\Administrator\\Desktop\\ipinfo.txt', 'a', encoding='utf8') as f:
            #f.write( lines + '\n')
            #f.close()
        #print(lines)
        if not line:
            break
    for Line in line:
        pass # do something'''





'''
    #f = open('C:\\Users\\Administrator\\Desktop\\ipcheck.txt', 'w',encoding='utf8')
    for Ip in Ipfile:
        time.sleep(1)
        Ipline = lookup(Ip.strip())
        print("Done!")

        #with open('C:\\Users\\Administrator\\Desktop\\ipinfo.txt', 'a', encoding='utf8') as f:
            #f.write(Ipline +'\n')
            #f.close()
'''



