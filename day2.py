#data types
a = 10#int
b = 3.5 #float
name = "simran" #string
is_cse = True #boolean
print(a,type(a))
print(b,type(b))
print(name,type(name))
print(is_cse,type(is_cse))
#type casting
x= "10"
y=int(x)
print(x,type(x))
print(y,type(y))
#if-else condition
age= int(input("enter age :"))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible")
# question
num = int(input("enter number :"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
# positive negative
n = int(input("enter number:"))
if n>0:
    print("postive")
else:
    print("negative")
# pass/fail
marks = int(input("enter marks :"))
if marks >= 40:
    print("pass")
else:
    print("fail")