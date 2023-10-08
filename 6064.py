a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)  
ab = a if (a<b) else b
bc = b if (b<c) else c
total = ab if(ab<bc) else bc
print(total)