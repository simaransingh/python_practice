def greet(): # def is a function and greet is a function name
    print("hello simran")
greet() #using call
#function with parameter
def greet(name):
    print("hello",name)
greet("simran")
greet("python")
# Function with return
def add(a,b):
    return a+b #return value
result = add(10,5)
print(result)
# Even/Odd function
def is_even(num):
    if num % 2==0:
        return True
    else:
        return False
print(is_even(8))
print(is_even(7))
#function Loop
def print_odd():
    for i in range(1,21):
        if i % 2 !=0:
            print(i)
print_odd()
# Square Function
def square (n):
    return n*n
print(square(5))
# Table Function 
def table(num):
    for i in range (1,11):
        print(num,"x",i,"=",num*i)
table(3)
def table(num):
    for i in range(1,21):
        print(num*i)
table(2)