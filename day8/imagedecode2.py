def read_input():
    image = [-1 for x in range(150)]
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    for line in f:
        for i in range(0, len(line)):
            val = i % 150
            if image[val] != -1:
                continue
            if line[i] == '0':
                image[val] = 0
            elif line[i] == '1':
                image[val] = 1
    for i in range(150):
        if i % 25 ==0:
            print()
        if image[i] == 1:
            print('#', end='')
        else:
            print(' ', end='')

read_input()