import itertools as it
import math

def read_input():
    try:
        f = open('input.txt')
    except FileNotFoundError:
        print("Could not find an input file")
        quit(-1)
    row = 0
    asteriods = []
    asteriod_num = 0
    for line in f:
        for col in range(len(line)):
            if line[col] == "#":
                asteriods.append((row, col, asteriod_num))
                asteriod_num += 1
        row += 1
    return asteriods

def main():
    asteriods = read_input()
    sight_lines = [set() for x in range(len(asteriods))]
    for pair in it.combinations(asteriods, 2):
        dx = pair[0][0] - pair[1][0]
        dy = pair[0][1] - pair[1][1]
        gcd = math.gcd(abs(dx), abs(dy))
        dx //= gcd
        dy //= gcd
        sight_lines[pair[0][2]].add((dx, dy))
        sight_lines[pair[1][2]].add((-dx, -dy))
    num_sight_lines = [len(sight_lines[x]) for x in range(len(sight_lines))]
    print(max(num_sight_lines))

if __name__ == "__main__":
    main()