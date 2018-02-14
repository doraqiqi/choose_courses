import os
import sys
BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

from core import main

def run(this_student):
    while True:
        list = [
            "1、查看详细信息",
            "2、缴费",
            "3、查看分数",
            "4、退出",
        ]
        for i in list:
            print(i)

        choose = input("请输入序号：").strip()
        if choose == "1":
            info(this_student)
        elif choose == "2":
            fee(this_student)
        elif choose == "3":
            score(this_student)
        elif choose == "4":
            exit()
        else:
            print("请输入争取的序号！！")


def info(this_student):
    this_student = main.Student.load(this_student.NAME)#刷新
    #print(this_student)
    this_student_fee = this_student.get_fee()
    print("------------------%s 信息-------------------"%this_student.NAME)
    print("用户名：",this_student.NAME)
    print("当前班级：",this_student.CLASSES.NAME)
    print("账户余额：",this_student_fee)
    if this_student.FEE_STATE == True:
        print("缴费状态：已缴费")
    else:
        print("缴费状态：\033[31;1m待缴费\033[0m")
    print("--------------------------------------------")

def fee(this_student):
    this_student = main.Student.load(this_student.NAME)#刷新
    if this_student.FEE_STATE == True:
        print("已经付过了！")
        return
    this_student_fee = this_student.get_fee()
    print("账户余额：",this_student_fee)
    this_student_course_name = this_student.CLASSES.COURSE.NAME
    #print(this_student_course_name)
    this_student_course_fee = this_student.CLASSES.COURSE.FEE
    print("\033[31;1m你报名的课程为%s，需要缴费的金额为%s,是否确定缴费？\033[0m"\
          %(this_student_course_name,this_student_course_fee))
    choose = input("yes or no?：").strip()
    if choose == "no":
        return
    elif choose == "yes":
        print(this_student)
        this_student_fee_now = this_student_fee - this_student_course_fee
        if this_student_fee_now < 0:
            print("\033[1;31余额不足！\033[0m")
        else:
            this_student = main.Student\
                (this_student.NAME,this_student.CLASSES,this_student_fee_now,this_student.PASSWD)
            this_student.FEE_STATE = True
            this_student.save()
            return



def score(this_student):
    this_student = main.Student.load(this_student.NAME)#刷新
    this_student_score = this_student.SCORE
    print("你的分数是：",this_student_score)
