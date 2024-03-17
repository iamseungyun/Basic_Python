def hello_func():
    return 'Hello Function!'

print(hello_func().upper())

def hello_func(greeting):
    return '{} Function!'.format(greeting)
print(hello_func('Hi'))

def hello_func(greeting, name = 'You'):
    return '{}, {}!'.format(greeting, name)

print(hello_func('Hi'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info('Math', 'Art', name = 'John', age = 22)

courses = ['Math', 'Art']
info = {'name' : 'John', 'age' : 22}

student_info(*courses, **info)


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31 ]

def is_leap(year):
    """Return True for leap years, False for non-leap years"""
    return year%4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month) :
    if not 1 <= month <= 12 :
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2020, 1))

