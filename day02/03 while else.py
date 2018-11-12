#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/11 9:13
# @Author : liaochao
# @File   : 03 while else.py
count = 0
while count<=5:
    count+=1
    if count == 3:break
    print('Loop',count)

else:
    print('循环正常执行完啦')
print('---------------out  of while ;oop')