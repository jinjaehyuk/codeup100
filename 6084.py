a, b, c ,s = input().split()
a = int(a)
b = int(b)
c = int(c)
s = int(s)
wav = a*b*c*s/8/1024/1024
print(round(wav,1),"MB",sep =' ')