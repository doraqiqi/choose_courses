# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

#DIR_NAME = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class School():
    pass

while True:
    list = [
    "1、管理员",
    "2、讲师",
    "3、学生",
    "4、退出"
    ]
    for item in list:
        print(item)
    choose = input("请输入你的身份：")
    if choose == "1":
        import admin
        admin.identify()
    if choose == "2":
        import teacher
        teacher.run()
    elif choose == "3":
        import student
        student.run()
    elif choose == "4":
        exit()
    else:
        print("输入有误！！")
