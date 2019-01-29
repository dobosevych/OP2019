f = open("sample.txt")
lines = [line.strip("\n") for line in f.readlines()]
print(lines)

vowels = "aeoiu"
for i in range(len(lines)):
    lst = []
    for j in range(len(lines[0])):
        if lines[i][j] not in vowels:
            lst.append(lines[i][j])
    print(lst)


vowels = "aeoiu"
for j in range(len(lines[0])):
    lst = []
    for i in range(len(lines)):
        if lines[i][j] in vowels:
            lst.append(lines[i][j])
    print(lst)
