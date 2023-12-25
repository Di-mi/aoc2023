

from typing import List, Tuple
from bisect import bisect, bisect_left


def run(input_file):

    
    with open(input_file, 'r') as file:
        contents = [line.strip() for line in file.readlines()]
            
        seeds = contents[0].split(':')[1].strip().split()
        
        state = None
        remaping_lists = []
        current_list: List[Tuple] = []
        for line in contents[1:]:
            if 'map' in line:
                if current_list: 
                    remaping_lists.append(current_list)
                    current_list = []
                continue
            if not len(line):
                continue   
            
            input_list = line.split(' ')
            
            convert_to = int(input_list[0])
            convert_from = int(input_list[1])
            offset = int(input_list[2])

            current_list.append((convert_from, convert_to, offset))

        remaping_lists.append(current_list)

        for remap_list in remaping_lists:
            remap_list.sort(key=lambda x: x[0])
        results =[]
        for seed in seeds:
            current = int(seed)
            for remap_list in remaping_lists:
                group_ind = bisect(remap_list, current, key=lambda x: x[0]) - 1

                if 0 <= group_ind and current >= remap_list[group_ind][0] and current - remap_list[group_ind][0] <= remap_list[group_ind][2]:
                    current = remap_list[group_ind][1] + (current - remap_list[group_ind][0])

            results.append(current)
            print('end_value', current)
        return min(results)


if __name__ == "__main__":
    print(run('1-input.txt'))
