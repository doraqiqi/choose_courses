# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
class School:
    pass

from core import  main


def run():
    while True:
        choose_list = [
            "1、注册",
            "2、登陆",
            "3、退出",
        ]
        for item in choose_list:
            print(item)
        input_choose = input("输入你的选择：").strip()
        if input_choose == "1":
            reg()
        elif input_choose == "2":
            login()
        elif input_choose == "3":
            exit()



def reg():
    flag = True
    while flag:
        # a = main.Student("小明","a班","25000")
        # print(a.NAME)
        # a.save()
        student_list = []
        student_data_list = main.Student.get_student_list()
        for item in student_data_list:
            print(item.NAME)
            student_list.append(item.NAME)
        print(student_list)
        name = input("输入你的用户名：").strip()
        if name in student_list:
            print("\033[31;1m该用户已经存在！！！\033[0m")
            break
        classes_list = []
        classes_list_data = main.Classes.get_classes_list()
        for item in classes_list_data:
            classes_list.append(item.NAME)
        print(classes_list)
        classes = input("输入选择班级：").strip()
        if classes not in classes_list:
            print("\033[31;1m该班级不存在！！！\033[0m")
            break
        else:
            classes = main.Classes.load(classes)
        fee = input("存入账户余额：").strip()
        fee = int(fee)
        input_passwd = input("输入密码：")
        reinput_passwd = input("请在输入一次：")
        if input_passwd == reinput_passwd:
            S = main.Student(name,classes,fee,input_passwd)
            print(S.NAME,S.CLASSES,S.PASSWD)
            S.save()
            flag = False
        else:
            print("\033[31;1m两次密码输入不一致\033[0m")
            flag = False


def login():
    student_list = []
    student_data_list = main.Student.get_student_list()
    for item in student_data_list:
        print(item.NAME)
        student_list.append(item.NAME)
    print(student_list)
    name = input("输入你的用户名：").strip()
    password = input("请输入密码：")
    if name not in student_list:
        print("\033[31;1m该用户不存在！！！\033[0m")
    else:
        this_student = main.Student.load(name)
        print(this_student.NAME,this_student.CLASSES)
        if this_student.PASSWD != password:
            print("\033[31;1m密码错！！！\033[0m")
        else:
            from core import student_model
            student_model.run(this_student)

if __name__ == '__main__':
    run()


