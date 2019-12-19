def read_input():
    num_zeros = []
    num_ones = []
    num_twos = []
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    for line in f:
        print(len(line))
        for i in range(0, len(line)):
            if i % 150 == 0:
                num_zeros.append(0)
                num_ones.append(0)
                num_twos.append(0)
            if line[i] == '0':
                num_zeros[-1] += 1
            elif line[i] == '1':
                num_ones[-1] += 1
            elif line[i] == '2':
                num_twos[-1] += 1
    min_zeros = 1000000
    index = 0
    for i in range(len(num_zeros)):
        if num_zeros[i] < min_zeros:
            min_zeros = num_zeros[i]
            index = i
    print(num_ones[index] * num_twos[index])

read_input()