




def run(input_file):

    with open(input_file, 'r') as file:
        content = [line.strip() for line in file.readlines()]
        sum = 0
        for line in content:
            remove_game_string = line.split(':')[1]
            numbers_string = remove_game_string.split('|')
            wining_dict = {}
            for winning_number in numbers_string[0].strip().split():
                wining_dict[int(winning_number)] = True
            count = 0
            print(remove_game_string)
            print(numbers_string[1])
            for played_number in numbers_string[1].strip().split():
                if wining_dict.get(int(played_number)) is not None:
                    print(played_number)
                    count +=1
            if count:
                sum += pow(2,count - 1)
                

        return sum
        


if __name__ == "__main__":
    print(run('1-input.txt'))
