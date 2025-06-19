import django_setup
from school.models import Schedule,Subject,Student,Teacher,Group,Grade

print("""
1 - Create Teacher
2 - Create Student
3 - Create Grade
4 - Create Subject
x - leave
""")
user_input = input()
1
while True:
    if user_input == "1":
        teacher_name = input()
        subject_name = input()
        Teacher.objects.create(name=teacher_name,subject=subject_name)
    if user_input == "2":
        name = input()

    if user_input == "3":
        name = input()

    if user_input == "4":
        name = input()
        Subject.objects.create(title=name)
    if user_input =="x":
        break