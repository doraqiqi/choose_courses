import uuid
import pickle
class School(object):
    def __init__(self,city):
        self.City = city


class Course(object):
    def __init__(self,name,school):
        self.Name = name
        self.School = school
#
#
s1 = School("shanghai")
f = open(str(s1.City),"w")
f.write(pickle.dumps(s1))
# c1 = Course("python",s1.City)
#
# print(c1.School)
#
# class num(object):
#     uuid.UUID
#     def __init__(self):
#         self.num = num
#     @staticmethod

