f = open("input2.txt", "r")
total = 0
get_first = ""
power = 0
for line in f.readlines():
    game_vals = line.split(':')[1]
    hands = game_vals.split(';')
    red_val, green_val, blue_val = 0, 0, 0
    for hand in hands:
        color_counts = hand.split(',')
        for color_count in color_counts:
            number, color = color_count.strip().split(' ')
            if color == 'red':
                red_val = max(int(number), red_val)
            elif color == 'blue':
                blue_val = max(int(number), blue_val)
            elif color == 'green':
                green_val = max(int(number), green_val)
    power += (red_val * blue_val * green_val)
print(power)
f.close()