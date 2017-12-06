#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/6 下午3:35
# @Author  : Chef
# @Site    : 
# @File    : whileGuessAge.py
# @Software: PyCharm




age_chenf = 25
count = 0

# while True:
#     if count == 3:
#         break
#     guess_age = int(input("Guess Age:"))
#     if guess_age == age_chenf:
#         print("yes, you got it.")
#         break
#     elif guess_age <= age_chenf:
#         print("think smaller...")
#     else:
#         print("think bigger!")
#     count = count +1


while count < 3:
    guess_age = int(input("Guess Age:"))
    if guess_age == age_chenf:
        print("yes, you got it.")
        break
    elif guess_age <= age_chenf:
        print("think smaller...")
    else:
        print("think bigger!")
    count = count + 1
# if count == 3:
#     print("Excessive number of errors，fuck off！")
else:
    print("Excessive number of errors，fuck off!")
