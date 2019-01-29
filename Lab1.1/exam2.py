f = open("sample.txt")
lines = f.readlines()
f.close()

for j in range(len(lines[0])):
    for i in range(len(lines)):
        print(lines[i][j])
