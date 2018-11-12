#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/7/29 22:53
# @Author : liaochao
# @File   : excample.py
'''
name=input('请输入你的姓名');
age=input('请输入你的年龄');
print('我的名字是'+name,age);
print(type(name));
'''

'''
if 5 > 4:
    print(6666)
print(777)

a='ll'
b=int(a)
print(type(b))
'''
'''
count=1
flag=True
print('111')
while flag:
    print('我们不一样')
    print('在人间')
    print('痒')
    count=count+1
    print(count)
    if count==20:
        flag=False
'''
'''
count=1
while count<20:
    print(count)
    continue
    count=count+1
'''

count=0

while count<=100:
    count+=1
    if count > 5 and count < 95:
        continue
    print("loop",count);
print("..........out of while loop")


