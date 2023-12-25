
import re


def run(input_file):
    RED_RX = r'([0-9]+) red' 
    BLUE_RX = r'([0-9]+) blue' 
    GREEN_RX = r'([0-9]+) green' 
    GAME_RX = r'Game ([0-9]+)' 
    with open(input_file) as file:
        contents = [line.strip() for line in file.readlines()]
        sum = 0
        for line in contents:
            game_match = re.search(GAME_RX, line)
            if game_match:
                game_num = game_match.group(1)
            blue_max = max(map(int, re.findall(BLUE_RX, line)))
            red_max = max(map(int, re.findall(RED_RX, line)))
            green_max = max(map(int, re.findall(GREEN_RX, line)))
            sum+= blue_max * red_max * green_max
        return sum


        
if __name__ == "__main__":
    print(run('2-part.txt'))
