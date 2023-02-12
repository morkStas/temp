n = int(input())
m = int(input())
mtx = [list(map(int, input().split())) for i in range(n)]
a, b = input().split()

for i in range(n):
    mtx[i][int(a)], mtx[i][int(b)] = mtx[i][int(b)], mtx[i][int(a)]
    print(*mtx[i])
