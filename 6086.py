a = int(input())
i = 0
sum = 0
# for i in range(0,a):
#     i += 1
#     sum += i
#     if sum >= a:
#         print(sum)
#         break
while True:
    i += 1
    sum += i
    if sum >= a:
        break
print(sum)