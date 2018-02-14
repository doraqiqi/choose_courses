# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import main

def run(this_teacher):
    while True:
        #print("this is your name",this_teacher.NAME)
        list = [
            '1、查看班级',
            '2、查看学员',
            '3、学员打分',
            '4、退出',
        ]
        for i in list:
            print(i)

        input_choose = input("输入你的选择：").strip()
        if input_choose == '1':
            check_classes(this_teacher)
        elif input_choose == '2':
            check_student(this_teacher)
        elif input_choose == '3':
            give_score(this_teacher)
        elif input_choose == '4':
            exit()
        else:
            print("输入有误！！！")

def check_classes(this_teacher):
    this_teacher_classes_list = teacher_classes_list(this_teacher)
    print("\033[31;1m现在你在教以下班级：\033[0m")
    for item in this_teacher_classes_list:
        print(item[1])
    print("-------------------------------")


def check_student(this_teacher):
    this_teacher_classes_list = teacher_classes_list(this_teacher)
    print(this_teacher_classes_list)
    print("\033[31;1m现在你在教以下班级：\033[0m")
    classes_list = []
    for item in this_teacher_classes_list:
        print(item[1])
        classes_list.append(item[1])
    choose_classes = input("\033[31;1m输入一个班级：\033[0m").strip()
    if choose_classes not in classes_list:
        print("\033[31;1m这不是你的班级！！！\033[0m")
    else:
        print("\033[31;1m以下是你的学生：\033[0m")
        get_student_data_list = main.Student.get_student_list()
        #print(get_student_data_list)
        this_teacher_student = []
        for item in get_student_data_list:
            #print(item.CLASSES.NAME)
            if item.CLASSES.NAME == choose_classes:
                print(item.NAME)
                this_teacher_student.append(item)
        print("-------------------------------")
        return this_teacher_student



def give_score(this_teacher):
    this_teacher_student_data = check_student(this_teacher)
    this_teacher_student = []
    for item in this_teacher_student_data:
        this_teacher_student.append(item.NAME)
    print("-------------------------------")
    choose_student = input("\033[31;1m你想给谁打分？\033[0m").strip()
    if choose_student not in this_teacher_student:
        print("\033[31;1m这不是你的学生！！！\033[0m")
    else:
        score = input("\033[31;1m分数是多少？\033[0m").strip()
        score = int(score)
        print(this_teacher_student)
        for item in this_teacher_student_data:
            if item.NAME == choose_student:
                item.SCORE = score
                item.save()


def teacher_classes_list(this_teacher):
    teacher_to_classes_list = main.teacher_to_class.get_teacher_to_class()
    #print(teacher_to_classes_list)
    teacher_classes_list = []
    for item in teacher_to_classes_list:
        if item[0] == this_teacher.NAME:
            teacher_classes_list.append(item)
    return teacher_classes_list
