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
    sight_lines = [] # Theta:asteriod
    thetas = []
    for pair in it.combinations(asteriods, 2):
        dx = pair[0][0] - pair[1][0]
        dy = pair[0][1] - pair[1][1]
        theta1 = math.atan(dy/dx)
        theta2 = math.atan(-dy/-dx)
        sight_lines.append((theta1, pair[0][2]))
        sight_lines.append((theta2, pair[1][2]))
        sight_lines.sort

if __name__ == "__main__":
    main()