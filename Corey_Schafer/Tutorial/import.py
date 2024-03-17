#import my_module

#courses = ['History', 'Math', 'Physics', 'CompSci']

#index = my_module.find_index(courses, 'Math')
#print(index)

#import my_module as mm
#courses = ['History', 'Math', 'Physics', 'CompSci']
#index = mm.find_index(courses, 'Math')
#print(index)

from my_module import find_index, test
courses = ['History', 'Math', 'Physics', 'CompSci']
index = find_index(courses, 'Math')
print(index)
print(test)

# from my_module import find_index as fi, test
# from my_module import *
import sys
print(sys.path)

# import sys
# sys.path.append('address')
# standard_library

import random

courses = ['History', 'Math', 'Physics', 'CompSci']
random_course = random.choice(courses)
print(random_course)

import math

rads = math.radians(90)
print(math.sin(rads))

import datetime
import calendar

today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

import os
print(os.getcwd())
print(os.__file__)
