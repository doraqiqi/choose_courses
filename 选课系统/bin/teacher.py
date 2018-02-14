# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
class School:
    pass


from core import main
a = main.Teacher.load("alex")
print(a.NAME)

def run():

    login()

def login():
    db_path = os.path.join(BASE_DIR,"db","teacher")
    print(file_name(db_path))
    teacher_name = input("输入你的名字：").strip()
    if teacher_name not in file_name(db_path):
        print("\033[31;1m该老师不存在\033[0m")
        return
    else:
        this_teacher = main.Teacher.load(teacher_name)
        from core import teacher_model
        teacher_model.run(this_teacher)

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print(root,dirs,files) #当前路径下所有非目录子文件
        return files

if __name__ == '__main__':
    run()
