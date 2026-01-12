arr = [1,2,3,4]
print(arr)
marks = [70,80,90]
print(marks[0])
for m in marks:
    print(m)
print(len(marks))
#Sum Of Element
arr =[1,2,3,4]
total = 0
for i in arr:
    total += i
print("total :",total)
#Maximum Element
arr =[10,40,5,90,2]
max_val = arr[0]
for i in arr:
    if i>max_val:
        max_val = i
print("max:",max_val)
#count even & odd
arr = [1,2,3,4,5]
even = 0
odd = 0
for i in arr:
    if i % 2==0:
        even+=1
    else:
        odd+=1
print("even :",even)
print("odd",odd)