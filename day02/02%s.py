#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/11/11 8:51
# @Author : liaochao
# @File   : 02%s.py
# name='太白'
# age='16'
# height='175'
# msg = "我叫%s,今年%s 身高%s" %(name,age,height)
# print(msg)
name = input('请输入名称:')
age = input('请输入年龄:')
job = input('请输入工作:')
hobbie = input('请输入爱好:')

msg='''-------------info of inde Li%s---------
Nanme :%s
Age :%d
Job: %s
Hobbie:%s
学习进度到了3%%
'''%(name,name,int(age),job,hobbie)

print(msg)