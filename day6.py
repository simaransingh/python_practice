student = {
    "name": "simran",
    "branch": "cse",
    "age": 20,
}
print(student)
print(student["name"])
print(student["age"])
# modify/add
student["age"]=21 #UPDATE
student["collage"] ="JMS INSTITUTE OF TECHNOLOGY"#ADD
print(student)
#dictionary loop
for key in student:
    print(key,":", student[key])
#DICTIONARY METHOD
print(student.keys())
print(student.values())
print(student.items())

#SET (STORE UNIQUE VALUES )
n={1,2,3,4,5}
print(n)
#SET OPERATION
n.add(6)
n.remove(2)
print(n)
#LOOP WITH SET
for num in n:
    print(num)
    #STUDENT DICTIONARY PRINT
student ={
    "name": "Happy",
    "branch" : "ECE",
    "age" :"25"
}
for k in student:
    print(k,student[k])
#REMOVE DUPLICATE USING SET
num= [1,2,2,3,4,5]
unique = set(num)
print(unique)
#COUNT WORD FREQUENCY
text ="python is easy python is powerful"
words = text.split()
freq = {}
for w in words:
    if w in freq:
        freq[w] +=1
    else:
        freq[w] =1
print(freq)