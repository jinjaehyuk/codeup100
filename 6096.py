d = []
for i in range(20):
    d.append([])    
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input())    
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    for j in range(1,20):
        if d[j][b] == 1:
            d[j][b] = 0
        else:
            d[j][b] = 1
            
        if d[a][j] == 1:
            d[a][j] = 0
        else:
            d[a][j] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = " ")
    print()        