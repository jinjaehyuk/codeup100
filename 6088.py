a , b, n = input().split()
a = int(a)
b = int(b) 
n = int(n)  

sum = a
for i in range(1,n):
    sum += b

print(sum)