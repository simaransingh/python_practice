name = input("enter your name :")
branch = input("Enter your branch")
Marks = int(input("Enter your marks"))
Student = {
    "name" : name,
    "branch" : branch,
    "Marks" : Marks,

}
if Marks >=50:
    result="pass"
else:
    result="fail"
if Marks >=75:
    grade="A"
elif Marks >=60:
    grade ="B"
elif Marks >=40:
    grade ="c"
else:
    grade="F"
print("\nStudent Details")
print(Student)
print("result :",result)
print("Grade :",grade)