# Author：zhaoyanqi
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海 2 所学校 ok
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开 ok
# 3. 课程包含，周期，价格，通过学校创建课程 ok
# 4. 通过学校创建班级， 班级关联课程、讲师 ok
# 5. 创建学员时，选择学校，关联班级 ok
# 5. 创建讲师角色时要关联学校， #关联到课程，因为课程和学校是绑定的
# 6. 提供两个角色接口 ok
# 6.1 学员视图， 可以注册， 交学费， 选择班级， ok
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 ok
# 6.3 管理视图，创建讲师， 创建班级，创建课程 ok
#
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里 ok


import uuid
import pickle
import os
import sys

BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

class School(object):
    '''
    学校的属性有：城市
    '''
    def __init__(self,city):
        self.CITY = city
    def save(self):
        pickle.dump(self,open(os.path.join(BASE_DIR,"db","school",self.CITY),"wb"))

    @staticmethod
    def load(school):
        s = pickle.load(open(os.path.join(BASE_DIR,"db","school",school),'rb'))
        #print(s)
        return s

class Course(object):
    '''
    课程绑定学校
    '''
    def __init__(self,name,school,period,fee):
        self.NAME = name
        self.SCHOOL = school
        self.PERIOD = period
        self.FEE = fee

    def save(self):
        pickle.dump(self,open(os.path.join(BASE_DIR,"db","course",self.NAME),"wb"))

    @staticmethod
    def get_course_list():
        db_path = (os.path.join(BASE_DIR,"db","course"))
        course_name_list = file_name(db_path)
        for item in course_name_list:
            course_data = Course.load(item)
            #return teacher_data
            print("课程吗:%s,学校名:%s,周期:%s,费用:%s"\
                  %(course_data.NAME,course_data.SCHOOL.CITY,course_data.PERIOD,course_data.FEE))

    @staticmethod
    def load(course):
        C = pickle.load(open(os.path.join(BASE_DIR,"db","course",course),'rb'))
        #print(s)
        return C

class Classes(object):
    '''
    班级绑定课程,老师
    '''
    def __init__(self,name,course):
        self.NAME = name
        self.COURSE = course
        #self.TEACHER_LIST = teacher_list
    def save(self):
        pickle.dump(self,open(os.path.join(BASE_DIR,"db","classes",self.NAME),"wb"))

    @staticmethod
    def load(Classes):
        c = pickle.load(open(os.path.join(BASE_DIR,"db","classes",Classes),'rb'))
        #print(s)
        return c

    @staticmethod
    def get_classes_list():
        db_path = (os.path.join(BASE_DIR,"db","classes"))
        classes_data_list = []
        classes_name_list = file_name(db_path)
        for item in classes_name_list:
            classes_data = Classes.load(item)
            classes_data_list.append(classes_data)
        return classes_data_list
            #print("姓名:%s,课程:%s"%(teacher_data.NAME,teacher_data.COURSE.NAME))

class teacher_to_class(object):
    '''
    讲师类里面查看班级列表
    '''
    classes_list= []
    number = 0
    def __init__(self,teacher,classes):
        self.ID = str(uuid.uuid1())
        self.TEACHER = teacher
        self.CLASSES = classes

    def save(self):
        pickle.dump(self,open(os.path.join(BASE_DIR,"db","teacher_to_classes",self.ID),"wb"))

    @staticmethod
    def get_teacher_to_class():
        teacher_to_class_list = []#这是存放实例内容的列表
        db_path = os.path.join(BASE_DIR,"db","teacher_to_classes")
        teacher_to_class_id_list = file_name(db_path)
        for item in teacher_to_class_id_list:#循环uuid列表
            teacher_to_class_data = teacher_to_class.load(item)#读取每一个实例的内容并把他们以元组的形式放到列表里
            a = (teacher_to_class_data.TEACHER,teacher_to_class_data.CLASSES)
            #print(a)
            teacher_to_class_list.append(a)
        #print(teacher_to_class_list)
        return teacher_to_class_list#返回这个列表

    @staticmethod
    def load(id):
        tc = pickle.load(open(os.path.join(BASE_DIR,"db","teacher_to_classes",id),'rb'))
        #print(s)
        return tc

class Teacher(object):
    '''
    老师绑定课程
    '''
    db_path = (os.path.join(BASE_DIR,"db","teacher"))

    def __init__(self,name,course):
        self.NAME = name
        self.COURSE = course
    def save(self):
        pickle.dump(self,open(os.path.join(BASE_DIR,"db","teacher",self.NAME),"wb"))

    @staticmethod
    def get_teacher_list():
        db_path = (os.path.join(BASE_DIR,"db","teacher"))
        teacher_name_list = file_name(db_path)
        for item in teacher_name_list:
            teacher_data = Teacher.load(item)
            #return teacher_data
            print("姓名:%s,课程:%s"%(teacher_data.NAME,teacher_data.COURSE.NAME))

    @staticmethod
    def load(teacher):
        t = pickle.load(open(os.path.join(BASE_DIR,"db","teacher",teacher),'rb'))
        #print(s)
        return t

    # def get_all_classes_list(self):

class Student():
    '''
    学生绑定班级
    '''
    def __init__(self,name,classes,fee,passwd):
        self.NAME = name
        self.CLASSES = classes
        self.__FEE = fee
        self.PASSWD = passwd
        self.FEE_STATE = False
        self.SCORE = 0

    def get_fee(self):
        return self.__FEE

    @staticmethod
    def get_student_list():
        students_list = []
        db_path = os.path.join(BASE_DIR,"db","student")
        students_file = file_name(db_path)
        for file in students_file:
            #print("file:",file)
            s = Student.load(file)
            #print("s:",s)
            students_list.append(s)
        return students_list


    def test(self):
        print("a")
    # def save(self):
    #     pickle.dump(self,open(os.path.join(BASE_DIR,"db","student",self.NAME),"wb"))
    def save(self):
        db_path = os.path.join(BASE_DIR,"db","student")
        pickle.dump(self,open(os.path.join(db_path,self.NAME),"wb"))

    @staticmethod
    def load(student):
        db_path = os.path.join(BASE_DIR,"db","student")
        S = pickle.load(open(os.path.join(db_path,student),"rb"))
        return S

    # def __del__(self):
    #     print("数据已经更改～")

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print(root,dirs,files) #当前路径下所有非目录子文件
        return files

# file_name_list = file_name(os.path.join(BASE_DIR,"db","school"))
# # for item in os.path.join(BASE_DIR,"db","school"):
# #     print(item)
# print(file_name(os.path.join(BASE_DIR,"db","school")))
# obj = School("shanghai")#建一个学校上海
# print(obj.CITY)
# if obj.CITY in file_name_list:
#     print("该学校已存在")
# else:
#     obj.save()
# obj = School("beijing")#建一个学校北京
# if obj.CITY in file_name_list:
#     print("该学校已存在")
# else:
#     obj.save()

# s1 = School.load("shanghai")
# print(s1.CITY)


#if __name__ == '__main__':

# def run():
#     print("aaa")
#     # school_shanghai = School("shanghai")
#     # school_beijing = School("beijing")
#
#     course_linux = Course("linux",school_beijing.CITY)
#     course_python = Course("python",school_beijing.CITY)
#     course_go = Course("go",school_shanghai.CITY)
#
#
#     t1 = Teacher("老师A",course_linux)
#     t2 = Teacher("老师B",course_linux)
#     t3 = Teacher("老师C",course_python)
#     t4 = Teacher("老师D",course_go)
#
#
#     c1 = Classes("linux1",course_linux,t1)
#     c2 = Classes("linux2",course_linux,t2)
#     c3 = Classes("python1",course_python,t3)
#     c4 = Classes("go1",course_go,t4)
#
#     s1 = Student("学员A",c3)
#
#     ttc1 = teacher_to_class(t1,c1)
#     ttc2 = teacher_to_class(t1,c2)
#     ttc2 = teacher_to_class(t3,c3)
#
#     print("python课程的学校：",course_python.SCHOOL)
#     print("go课程的学校：",course_go.SCHOOL)
#     print("c3的学校和老师名字：",c3.COURSE.SCHOOL,c3.TEACHER.NAME)
#     print("学生1的名字，学院1所在班级的名字：",s1.NAME,s1.CLASSES.NAME)
#     print(ttc1.TEACHER.NAME)

# course = Course("python","上海")
# print(course.NAME)
# course.save()
