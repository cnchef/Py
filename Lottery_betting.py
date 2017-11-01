#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 16:37
# @Author  : Willpower-chen
# @Site    : 
# @File    : Lottery_betting.py
# @Software: PyCharm

import random
from time import clock
count=int(input("你要买几注:"))
indexout = 0
arry1 = []
while indexout<count:
##蓝色球部分
 indexin=0
 while indexin <= 5:
     rand=random.randint(1,32)
     if rand not in arry1:
        arry1.insert(indexin,rand)
        indexin += 1
     arry1.sort()
##红色球部分
 arry1.insert(6,'||')
 arry1.insert(len(arry1),random.randint(1,16))
 print(arry1)
 arry1.clear()
 indexout+=1
