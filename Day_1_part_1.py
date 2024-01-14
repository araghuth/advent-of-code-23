f = open("input1.txt", "r")
total = 0
for i in f.readlines():
    start, end = 0, 0
    for j in i:
        if j.isdigit():
            start = j
            break
    for k in reversed(i):
        if k.isdigit():
            end = k
            break
    number = int(start + end)
    total += number
print(total)
f.close()