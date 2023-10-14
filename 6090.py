a , m, d, n= input().split()
a = int(a)
m = int(m) 
d = int(d)  
n = int(n)

sum = a
for i in range(1,n):
    sum *= m
    sum += d

print(sum)