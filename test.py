#!/usr/bin/python3

name = "Will"
print("Hello %s" % name)

x = 1
y = 2
print("x is equal to y: %s" % (x==y))
z = 1
print("x is equal to z: %s" % (x==z))

course = 'Python for Beginners'
print (course.lower())
print (course.upper())
print (course)
shorter_course = course[0:6]
print (shorter_course)
if (shorter_course in course):
    print("You will learn %s in %s" % (shorter_course, course))
else:
    print("You will not learn %s in %s" % (shorter_course, course))
    
for class_letter in course[:]:
    print(class_letter)
