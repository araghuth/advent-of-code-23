dicti = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
f = open("input2.txt", "r")
total = 0
#f = 'seven94four\n 9h6nine\n'
for i in f.readlines():
    start, end = 0, 0
    string_val_j, string_val_k = '', ''
    flag_j, flag_k = False, False
    for j in i:
        string_val_j += j
        for keys in dicti:
            if keys in string_val_j:
                start = dicti[keys]
                flag_j = True
                break
        if flag_j:
            break
        if j.isdigit():
            start = j
            break
    for k in reversed(i):
        string_val_k = k + string_val_k
        for keys in dicti:
            if keys in string_val_k:
                end = dicti[keys]
                flag_k = True
                break
        if flag_k:
            break
        if k.isdigit():
            end = k
            break
    number = int(str(start) + str(end))
    total += number
print(total)
f.close()