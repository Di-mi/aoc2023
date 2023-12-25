import copy

def update_adj_gears(content,curr_num, mat, row_of_digit, column_of_digit):

    len_of_num = len(str(curr_num))

    for i in range(-1,2):
        for j in range(column_of_digit - (len_of_num) ,column_of_digit +2):
            try:
                if content[row_of_digit+ i][j] == '*':
                    if mat.get(f"{row_of_digit+ i},{j}"):
                        mat[f"{row_of_digit+ i},{j}"].append(curr_num)
                    else:
                        mat[f"{row_of_digit+ i},{j}"] = [curr_num]
            except IndexError:
                continue



def run(input_file):
    with open(input_file, 'r') as file:
        content = [line.strip() for line in file.readlines()]

        gear_mat = {} 
        for i in range(len(content)):
            is_digit = False
            curr_digit = 0
            for j in range(len(content[i])):
                
                ch = content[i][j]
                if ch.isdigit():
                    print(ch)
                    curr_digit = 10 * curr_digit + int(ch) 
                    is_digit = True

                else:
                    if is_digit:
                        is_digit = False
                        update_adj_gears(content, copy.deepcopy(curr_digit), gear_mat, i, j-1)
                        curr_digit = 0

            if curr_digit:
                print(curr_digit)
                update_adj_gears(content, copy.deepcopy(curr_digit), gear_mat, i, len(content[i])-1)
                
        sum = 0

        print(gear_mat)
        for _, value in gear_mat.items():
            if len(value) == 2:
                sum += value[0] * value[1]
        return sum 

if __name__ == "__main__":
    print(run('2-input.txt'))
