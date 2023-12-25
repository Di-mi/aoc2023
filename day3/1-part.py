from functools import reduce


def check_if_star_is_adj(mat, i, j):
    dirs = [
            (-1,-1),
            (-1,0),
            (1,-1),
            (-1,1),
            (1,1),
            (0,1),
            (0,-1),
            (1,0),
            ]
    for x, y in dirs:
        try:
            target = mat[i+x][j+y]
            

            if not target.isdigit() and target != '.':
                return True
        except IndexError:
            continue
    return False

def run(input_file):

    with open(input_file, 'r') as file:
        content = [line.strip() for line in file.readlines()]
        
        is_part_of_digit = False
        is_adj = False
        curr_digit = 0
        sum =0 
        for i in range(len(content)):
            is_part_of_digit = False
            is_adj = False
            curr_digit = 0
            for j in range(len(content[i])):
                ch = content[i][j]
                if not ch.isdigit():
                    if is_part_of_digit and is_adj:
                        print(curr_digit)
                        sum += curr_digit
                    curr_digit = 0
                    is_part_of_digit = False
                    is_adj = False

                if ch.isdigit():
                    curr_digit = curr_digit * 10 + int(ch)
                    is_part_of_digit = True
                    if not is_adj:
                        is_adj = check_if_star_is_adj(content, i, j)
            if curr_digit and is_adj:
                sum += curr_digit
        return sum


        

if __name__ == "__main__":
    print(run('1-input.txt'))
