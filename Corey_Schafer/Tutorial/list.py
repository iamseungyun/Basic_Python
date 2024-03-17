courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[1:-1])

courses.append('Art')
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0,'Art')
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0,courses_2)
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.extend(courses_2)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop()
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(popped)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()
print(courses)

nums = [1,5,2,4]
nums.sort()
print(nums)

nums = [1,5,2,4]
nums.sort(reverse = True)
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort(reverse = True)
print(nums)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('CompSci'))
print('Art' in courses)
print('Math' in courses)

for course in courses :
    print(course)

for index, course in enumerate(courses, start=1) :
    print(index, course)

course_str = ', '.join(courses)
print(course_str)
new_list = course_str.split()
print(new_list)