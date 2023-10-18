li = []
w, h = input().split() #격자판 가로세로
w = int(w) #가로
h = int(h) #세로
for i in range(w+1):
    li.append([])
    for j in range(h+1):
        li[i].append(0)

#막대의 갯수
n = int(input())
for i in range(n):
    l,d,x,y = input().split()
    l = int(l)
    d = int(d) #가로 0, 세로 1
    x = int(x)
    y = int(y)
    for j in range(l):
        if d == 0:
            li[x][y+j] = 1
        else:
            li[x+j][y] = 1
            
for i in range(1,w+1):
    for j in range(1,h+1):
        print(li[i][j],end=" ")
    print()