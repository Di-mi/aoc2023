
def run(input_file):
    with open(input_file) as file:
        contents = [ line.strip() for line in file.readlines()]
        sum = 0 
        for line in contents:
            first = None
            second = None
            for c in line:
                if c.isdigit():
                    if first is None:
                        first = int(c)
                    else:
                        second = int(c)
            if first is not None:
                sum += first * 10 + second if second else first * 10 + first

        return sum

if __name__ == "__main__":
    print(run('input2.txt'))

