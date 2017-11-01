#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/4 17:07
# @Author  : chenf
# @Site    : 
# @File    : shopping.py
# @Software: PyCharm




salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")

welcome_msg = ("Welcome to Chenf Shopping mall" .center(50,'-'))
print(welcome_msg)

exit_flag = False
product_list = [
    ('Iphone', 5288),
    ('Mac Air', 6288),
    ('Mac Pro', 9288),
    ('Xiao Mi', 1999),
    ('vivo', 2599),
    ('Mei Zu', 1999),
    ('Hua Wei', 2999),]

shop_car = []
while exit_flag is not True:
    print("product_list".center(50,'-'))
    #for p_name,p_price in product_list:
     #   print(p_name,p_price)
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)

    user_choice = input("[q=quit,c=check]What do you want to buy?:")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary:
                shop_car.append(p_item)
                salary -= p_item[1]
                print("Added [%s] into shop car,youcurrent balance is \033[31;1m[%s]\033[0m" %
                      (p_item,salary))
            else:
                print("you balance is [%s],cannot afford this.." % salary)
    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)
            exit_flag = True
        elif user_choice =='c' or user_choice =='check':
            print("purchased products as below".center(40, '*'))
            for item in shop_car:
                print(item)
            print("END".center(40, '*'))
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)
            exit_flag = True







