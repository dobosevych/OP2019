m, n = map(int, input().split())

i = 1
lst = []
while len(lst) < m * n:
    lst += str(i)
    i += 1

print(lst)

for i in range(m):
    for j in range(n):
        print(lst[i * n + j], end="")
    print()