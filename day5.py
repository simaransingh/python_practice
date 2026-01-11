#List
n=[5,4,3,2,1]
print(n)
#list indexing
print(n[0])
print(n[2])
#list modify
n[1]=25
print(n)
#list method
n.append(50) #add
n.remove(1)#remove
print(len(n))
#loops with list
for num in n:
    print(num)
#string basics
name= "simran"
print(name)
#string indexing
print(name[0])
print(name[3])
#string slicing
word ="python"
print(word[0:3])
print(word[::-1])
#imp string method
text="hello world"
print(text.upper())
print(text.lower())
print(text.count("o"))
print(text.replace("world","python"))
# Even no from list 
num=[1,2,3,4,5,6]
for n in num:
    if n %2 ==0:
        print(n)
#reverse String
word="python"
print(word[::-1])
#count vowels
text="education"
count =0
for ch in text:
    if ch in "aeiou":
        count +=1
print(count)





