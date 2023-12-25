
def union(groups, weights, first, second):
    if groups[first] == first:
        groups[second] = first
    else: 
        next_parent = groups[first]
        while groups[next_parent] != next_parent:
            next_parent = groups[next_parent]
        groups[second] = next_parent

    weights[second] = weights[first] + weights[second]

def run(input_file:str):
    with open(input_file, 'r') as file:
        content = [line.strip() for line in file.readlines()]
        match_counts=[]
        for line in content:
            remove_game_string = line.split(':')[1]
            numbers_string = remove_game_string.split('|')
            wining_dict = {}
            for winning_number in numbers_string[0].strip().split():
                wining_dict[int(winning_number)] = True
            match = 0
            for played_number in numbers_string[1].strip().split():
                if wining_dict.get(int(played_number)) is not None:
                    match+=1
            match_counts.append(match)

        print(match_counts)
        group_pointers = [ind for ind in range(len(match_counts))]
        group_weights = [1] * len(match_counts)
        print(group_pointers  )
        for ind in range(len(match_counts)):
            for next_copy in range(1,match_counts[ind]+1):
                print(ind, ind+next_copy)
                union(group_pointers, group_weights, ind, ind+next_copy)
                print(group_weights)

        return sum(group_weights)
    
if __name__ == "__main__":
    print(run('2-input.txt'))
