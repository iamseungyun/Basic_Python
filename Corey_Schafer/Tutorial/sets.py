# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)
print('Math' in cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = {} # This makes dictionary!
empty_set = set()