f = open("input2.txt", "r")
total = 0
get_first = ""
for line in f.readlines():
    game_valid = True
    game_vals = line.split(':')[1]
    hands = game_vals.split(';')
    for hand in hands:
        if not game_valid:
            break
        color_counts = hand.split(',')
        red_val, green_val, blue_val = 0, 0, 0
        for color_count in color_counts:
            number, color = color_count.strip().split(' ')
            if color == 'red':
                red_val = int(number)
            elif color == 'blue':
                blue_val = int(number)
            elif color == 'green':
                green_val = int(number)
        if red_val <= 12 and green_val <=13 and blue_val <=14:
            game_valid = True
        else:
            game_valid = False
    if game_valid:
        get_first += line.split(':')[0]
        total += int(get_first.split(' ')[-1])
print(total)
f.close()