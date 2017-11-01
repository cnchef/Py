#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/18 21:26
# @Author  : chenf
# @Site    : 
# @File    : BMI_Calculation.py
# @Software: PyCharm


# 体质指数（BMI）=体重（kg）÷身高^2（m）
# EX：70kg÷（1.75×1.75）=22.86
# geight = 1.75
# weight = 80.5
geight = float(input('请输入你的身高（如:1.75）:'))
weight = float(input('请输入你的体重KG（如:80）:'))
bmi = (weight / (geight ** 2))
#print(bmi)

if bmi <= 18.5:
    #print('过轻','身高:',geight,'体重:',weight,'KG,BMI:',bmi)
    print('过轻\t身高:%s\t体重:%sKG\t\tBMI:%.2f' % (geight,weight,bmi))
elif bmi  <= 25:
    #print('正常','身高:',geight,'体重:',weight,'KG,BMI:',bmi)
    print('正常\t身高:%s\t体重:%sKG\t\tBMI:%.2f' % (geight,weight,bmi))
elif bmi <= 32:
    #print('过肥','身高:',geight,'体重:',weight,'KG,BMI:',bmi)
    print('过肥\t身高:%s\t体重:%sKG\t\tBMI:%.2f' % (geight,weight,bmi))
else:
    #print('严重肥胖','身高:',geight,'体重:',weight,'KG,BMI:',bmi)
    print('严重肥胖\t身高:%s\t体重:%sKG\t\tBMI:%.2f' % (geight,weight,bmi))
