# 3 4
# 1234
# 5678
# 9101
m, n = map(int, input().split())

i = 1
lines = []
line = ""

while True:
    s = str(i)
    if len(line + s) >= n:
        # TODO: correct later
        print(n - len(line))
        line += s[:n - len(line)]
        lines.append(line)
        line = s[n - len(line):]
    else:
        line += s
    if len(lines) == m:
         break
    i += 1

print(lines)