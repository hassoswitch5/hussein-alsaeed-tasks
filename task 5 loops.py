#task1
n = int(input("pls enter  the nth therm of fibonacci"))

x=0
y=1
feb=x+y
if n == 1:
    feb=0
elif n == 2:
    feb =1
else:
    i= 3
    while i < n :
        x=y
        y=feb
        print(x)
        print(y)
        i+=1
        feb=x+y
    
print(feb)











#task2

n =  int(input("Print prime numbers untill"))

list = []

for num in range (2, n + 1 ):

    is_prime = True

    for i in range (2 , num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime == True:
        list.append(num)

print(list)



#task 3


