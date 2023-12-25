
tree = {
        "data": None,
        "children": [
            {"data": 'o', "children": [
                {"data": 'n', "children": [
                    {"data": 'e', "number": 1, "children":None },
                    ] },
                ] },
            {"data": 't', "children":  [
                {"data": 'w', "children":[
                    {"data": 'o', "number": 2,"children":None },
                    ] },
                {"data": 'h', "children": [
                    {"data": 'r', "children": [
                        {"data": 'e', "children": [
                            {"data": 'e', "number":3, "children": None },
                            ] },
                        ] },
                    ] },
                ]},
            {"data": 'f', "children": [
                {"data": 'o', "children": [
                    {"data": 'u', "children": [
                        {"data": 'r', "number":4 , "children": None },
                        ]},
                    ] },

                {"data": 'i', "children": [
                    {"data": 'v', "children": [
                        {"data": 'e', "number":5,"children": None },
                        ] },
                    ] },
                ]},
            {"data": 's', "children": [
                {"data": 'i', "children": [
                    {"data": 'x', "number":6,"children":None },
                    ] },
                {"data": 'e', "children":[
                 {"data": 'v', "children":[
                  {"data": 'e', "children":[
                      {"data": 'n', "number": 7,"children": None},
                            ]},
                        ]},
                    ]},
                    ]},
                  {"data": 'e', "children":[
                   {"data": 'i', "children":[
                    {"data": 'g', "children": [
                        {"data": 'h', "children":[
                            {"data": 't', "number": 8, "children": None}
                        ]},
                         ]},
                     ]},
                     ]},
                    {"data": 'n', "children": [
                        {"data": 'i', "children":[
                            {"data": 'n', "children": [
                                {"data": 'e', "number": 9, "children":None},
                                ] },
                            ] },
                        ] },
]}


def find_in_tree(node, ch) -> None | dict:
    for child in node.get('children', []):
        if ch == child.get('data'):
            return child
    return None



def run(input_file: str):
    global tree

    with open(input_file, 'r') as file:
        contents = [line.strip() for line in file.readlines()]
        sum = 0

        for line in contents:
            curr_word_len=0
            print(line)
            current_node = tree
            first = None
            second = None
            ch_index = 0
            while ch_index < len(line):
                ch = line[ch_index]
                number = ch
                if not ch.isdigit():
                    if current_node:=find_in_tree(current_node, ch):
                        curr_word_len +=1 
                    else:
                        current_node = tree
                        ch_index -= curr_word_len

                        curr_word_len = 0

                    if current_node.get('number'):
                        number = current_node.get('number')
                        current_node = tree
                        ch_index -= curr_word_len - 1
                        curr_word_len = 0

                if number and (type(number) is int or number.isdigit()):
                    if first is None:
                        first = int(number)
                    else:
                        second = int(number)
                ch_index +=1

            if first:
                if second:
                    sum+= first *10 + second
                    print(first, second)
                else:
                    sum+= first * 10 + first
                    print(first, second)
        return sum




if __name__ == "__main__":
    print(run('part2.txt'))
