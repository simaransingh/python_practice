# For Loop
for i in range(1,6):
    print(i)
# Range
#print(range(stop 5)) ---- 0 to 4
#print(list(range(5)))----- convert to list
for i in range(2,11,2): #start---2, end--11, jump--2
    print(i)
# while Loop
i = 1
while i <= 5:
    print(i)
    i = i+1
# Break
for i in range(1,10):
    if i==5:
        break
    print(i)
# Continue
for i in range(1,6):
    if i ==3:
        continue
    print(i)
    # print even no
for i in range(1,11):
    if i %2==0:
        print(i)
    #print sum of 1 to 5
    sum = 0
for i in range(1,6):
    sum +=i
print(sum) 
# Reverse counting(5 to 1)
for i in range(5,0,-1):
    print(i)
for i in range(1,11):
    print(2*i)
for i in range(1,21):
    if i % 3==0:
        print(i)
# print table 5
for i in range (1,11):
    print(5*i)
# Print Odd no(1 to 10)
for i in range(1,11):
    if i % 2 !=0:
        print(i)

