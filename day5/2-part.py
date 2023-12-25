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
            remap_list.sort(key=lambda x: x[1])

        limits =  [(remap[0], remap[1] - remap[0], remap[2]) for remap in remaping_lists[-1]]

        for remap_list in reversed(remaping_lists[:-1]):
            new_limits = []
            print(limits)
            for (limit, transform, offset) in limits:
                group_ind = bisect(remap_list, limit, key=lambda x: x[1]) - 1
                if 0 <= group_ind and limit >= remap_list[group_ind][1] and (limit - remap_list[group_ind][1]) <= remap_list[group_ind][2]:
                    new_limit = remap_list[group_ind][0] + (limit - remap_list[group_ind][1])
                    new_limits.append((new_limit, transform + (remap_list[group_ind][1] - remap_list[group_ind][1]),offset))
                else:
                    new_limits.append((limit, transform, offset))

            new_limits.sort(key=lambda x: x[0])
            limits = new_limits
            print('new limits', limits)
            for remap in remap_list:
                group_ind = bisect(limits, remap[0], key=lambda x: x[0]) - 1 
                if 0 <= group_ind and remap[0] >= limits[group_ind][0] and (remap[0] - limits[group_ind][0] <= limits[group_ind][2]):
                    limits.append((remap[0], limits[group_ind][1] + (remap[0] - limits[group_ind][1]),remap[2]))
                else:
                    limits.append((remap[0], remap[1]-remap[0], remap[2]))
            limits.sort(key=lambda x: x[0])


        print(limits)
        

if __name__ == "__main__":
    print(run('2-input.txt'))
