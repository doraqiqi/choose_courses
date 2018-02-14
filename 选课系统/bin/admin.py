# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import pickle
import uuid
#DIR_name = os.path.dirname(__file__)
#print(DIR_name)


BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

class School:
    '''调用main模块提示缺少school类。。'''
    pass

from core import main

def identify():
    flag = True
    password = False
    while flag:
        if password == False:
            input_passwd = input("请输入密码,输入return返回，输入exit退出：")
            if input_passwd == "123456":
                password = True
                run()
            elif input_passwd == "return":
                import start
            elif input_passwd == "exit":
                exit()
            else:
                print("wrong password!")
        else:
            run()

def run():
    while True:
        choose_list = [
            "1、新建课程",
            "2、新建班级",
            "3、注册老师",
            "4、查看班级列表",
            "5、查看课程列表",
            "6、查看教师列表",
            "7、老师绑定班级",
            "8、退出",
        ]
        for item in choose_list:
            print(item)
        input_choose = input("输入你的选择：")
        if input_choose == "1":
            creat_course()
        elif input_choose == "2":
            creat_classes()
        elif input_choose == "3":
            creat_teacher()
        elif input_choose == "4":
            classes_list()
        elif input_choose == "6":
            teacher_list()
        elif input_choose == "5":
            course_list()
        elif input_choose == "7":
            teacher_to_class()
        elif input_choose == "8":
            exit()


def creat_classes():
    while True:
        input_class_name = input("请输入班级名称:").strip()
        class_list = file_name(os.path.join(BASE_DIR,"db","classes"))
        if input_class_name in class_list:
            print("----------这个班级已经存在了------------")
            break
        input_course_name = input("输入课程名：").strip()
        course_list = file_name(os.path.join(BASE_DIR,"db","course"))
        if input_course_name not in course_list:
            print("--------------没有这个课程----------------")
            break
        else:
            this_course = main.Course.load(input_course_name)
            this_course_name = this_course.NAME
            print(this_course_name)
            classes_model(input_class_name,this_course)
            break

def file_name(file_dir):
    '''查询目录下所有文件'''
    for root, dirs, files in os.walk(file_dir):
        #print(root,dirs,files) #当前路径下所有非目录子文件
        return files

def creat_course():
    while True:
        input_course_name = input("输入你的课程名称：").strip()
        course_list = file_name(os.path.join(BASE_DIR,"db","course"))
        if input_course_name in course_list:
            print("----------这个课程已经存在了------------")
            break
        input_course_school = input("输入学校在北京还是上海：").strip()
        if input_course_school =="北京":
            input_course_school = main.School.load("beijing")
            print(input_course_school.CITY)
        elif input_course_school =="上海":
            input_course_school = main.School.load("shanghai")
            print(input_course_school.CITY)
        else:
            print("没有这个学校")
            break
        input_course_period = input("输入课程周期（单位：周）：").strip()
        input_fee_period = input("输入学费：").strip()
        input_fee_period = int(input_fee_period)
        course_model(input_course_name,input_course_school,input_course_period,input_fee_period )
        break

def creat_teacher():
    flag = True
    while flag:
        input_teacher_name = input("输入老师的名字：").strip()
        teacher_list = file_name(os.path.join(BASE_DIR,"db","teacher"))
        if input_teacher_name in teacher_list:
            print("----------这个老师名字已经被注册了------------")
            break
        input_course_name = input("输入课程名：").strip()
        course_list = file_name(os.path.join(BASE_DIR,"db","course"))
        if input_course_name not in course_list:
            print("--------------没有这个课程----------------")
            flag = False
        else:
            this_course = main.Course.load(input_course_name)
            this_course_name = this_course.NAME
            print(this_course_name)
            teachaer_model(input_teacher_name,this_course)
            flag = False

def classes_list():
    print("------------班级-------------")
    classes_data_list = main.Classes.get_classes_list()
    #print(classes_data_list)
    for item in classes_data_list:
        print("班级名：%s,课程名：%s，上课地点：%s，老师如下："\
              %(item.NAME,item.COURSE.NAME,item.COURSE.SCHOOL.CITY))
        # print("姓名%s,课程%s"%(teacher_data.NAME,teacher_data.COURSE.NAME))
        db_path_teacher_to_classes =  (os.path.join(BASE_DIR,"db","teacher_to_classes"))
        for file in file_name(db_path_teacher_to_classes):#从老师和班级绑定实例中查询该班级的老师有哪些
            classes_name = main.teacher_to_class.load(file).CLASSES
            teacher_name = main.teacher_to_class.load(file).TEACHER
            if classes_name == item.NAME:
                print(teacher_name)
    print("--------------------------------")

def teacher_list():
    print("------------教师列表-------------")
    teacher_list = main.Teacher.get_teacher_list()
    # print("姓名%s,课程%s"%(teacher_data.NAME,teacher_data.COURSE.NAME))
    # print(teacher_data)
    print("--------------------------------")

def course_list():
    print("------------课程列表-------------")
    course_list = main.Course.get_course_list()
    # print("姓名%s,课程%s"%(teacher_data.NAME,teacher_data.COURSE.NAME))
    # print(teacher_data)
    print("--------------------------------")

def teacher_to_class():
    flag = True
    while flag:
        input_teacher = input("输入老师：").strip()
        teacher_list = file_name(os.path.join(BASE_DIR,"db","teacher"))
        if input_teacher not in teacher_list:
            print("该老师不存在！！")
            break
        input_classes= input("输入班级：").strip()
        classes_list = file_name(os.path.join(BASE_DIR,"db","classes"))
        print(classes_list)
        if input_classes not in classes_list:
            print("这个班级不存在！！")
            break
        else:
            this_teacher_classes = (input_teacher,input_classes)#以老师班级的组合创建一个元组
            print(this_teacher_classes)
            teacher_to_class_list = main.teacher_to_class.get_teacher_to_class()\
                #这个列表存放所有教师和课程的信息，用元组形式
            print(teacher_to_class_list)
            # TC = main.teacher_to_class(input_teacher,input_course)
            # TC.save()
            if teacher_to_class_list == []:#如果列表是空的那么就直接绑定老师和课程
                TC = main.teacher_to_class(input_teacher,input_classes)
                TC.save()
                flag = False
            else:#如果不是空的要检查是否已经绑定过了
                if this_teacher_classes in teacher_to_class_list:
                    print("该老师已经绑定过该班级！！")
                    flag = False
                else:
                    print(input_teacher,input_classes)
                    TC = main.teacher_to_class(input_teacher,input_classes)
                    TC.save()
                    flag = False

def course_model(course,school,period,fee):
    course = main.Course(course,school,period,fee)
    print(course.NAME,course.SCHOOL.CITY)
    course.save()

def teachaer_model(name,course):
    teacher = main.Teacher(name,course)
    teacher.save()

def classes_model(name,course):
    classes = main.Classes(name,course)
    classes.save()


if __name__ == '__main__':

    identify()
