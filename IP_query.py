#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/17 17:47
# @Author  : chenf
# @Site    :
# @File    : IP_query.py
# @Software: PyCharm

import requests
import json
import time
import os
#reload(sys)
#sys.setdefaultencoding('utf-8')



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
        Ipline = lookup(Ip.strip())
        #lookup(Ip.strip())
        #print("Done!")
        with open('C:\\Users\\Administrator\\Desktop\\ipinfo.txt', 'a', encoding='utf8') as f:
            f.write(Ipline + '\n')
            f.close()

finally:
    Ipfile.close()
    print('Cleaning up...closed the file')
    os.system('notepad C:\\Users\\Administrator\\Desktop\\ipinfo.txt')
