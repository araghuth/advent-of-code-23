f = open("input3.txt", "r")
input_matrix = []

# input matrix for dfs
for line in f.readlines():
    chars_by_line = []
    for character in line:
        if character == '\n':
            continue
        chars_by_line.append(character)
    input_matrix.append(chars_by_line)

len_of_input = len(input_matrix)
touched = [[False for _ in range(len_of_input)] for __ in range(len(input_matrix[0]))]

def adjacent_pos(row, col, search_space):
    if search_space[row][col].isnumeric():
        return [[row,col-1], [row, col+1]]
    return [[row+1,col], [row-1,col], [row,col+1], [row,col-1], [row+1,col+1], [row-1,col+1], [row+1,col-1], [row-1,col-1]]

def dfs(row, col, search_space, touched):
    global len_of_input
    
    position_list = adjacent_pos(row, col, search_space)
    count = 0
    for next_row, next_col in position_list:
        if next_row < 0 or next_row >= len_of_input:
            continue
        if next_col < 0 or next_col >= len(search_space[row]):
            continue
        if not search_space[next_row][next_col].isnumeric():
            continue
        count += 1
        if touched[next_row][next_col] == True:
            continue
        touched[next_row][next_col] = True
        dfs(next_row, next_col, search_space, touched)
    return count

result = 0
for i in range(len_of_input):
    len_of_each_row = len(input_matrix[i])
    for j in range(len_of_each_row):
        if not input_matrix[i][j].isalnum() and input_matrix[i][j] != '.':
            value = dfs(i, j, input_matrix, touched)
            if value == 2:
                pass