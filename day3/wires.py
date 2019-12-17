import numpy as np
from tqdm import trange

def read_input():
    wires = []
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    for line in f:
        wire = [(x[0], int(x[1::])) for x in line.split(',')]
        wires.append(wire)
    return wires

def size_of_grid(wires):
    minx = 10000000
    miny = 10000000
    maxx = -10000000
    maxy = -10000000
    x = 0
    y = 0
    for wire in wires:
        for step in wire:
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
            if step[0] == "U":
                y += step[1]
            elif step[0] == "D":
                y -= step[1]
            elif step[0] == "R":
                x += step[1]
            elif step[0] == "L":
                x -= step[1]
            else:
                print('INVALID DIRECTION')
                quit(-1)
    print(minx, miny, maxx, maxy)

def fill_board(board, wires):
    wire_num = 0
    for wire in wires:
        wire_num += 1
        pos = [15874, 7695]
        board[15874, 7695] = -1
        for step in wire:
            if step[0] == "U":
                for i in range(step[1]):
                    pos[1] += 1
                    if board[pos[0],pos[1]] == wire_num or board[pos[0],pos[1]] == 0:
                        board[pos[0],pos[1]] = wire_num
                    else:
                        board[pos[0],pos[1]] = -2
            elif step[0] == "D":
                for i in range(step[1]):
                    pos[1] -= 1
                    if board[pos[0],pos[1]] == wire_num or board[pos[0],pos[1]] == 0:
                        board[pos[0],pos[1]] = wire_num
                    else:
                        board[pos[0],pos[1]] = -2
            elif step[0] == "R":
                for i in range(step[1]):
                    pos[0] += 1
                    if board[pos[0],pos[1]] == wire_num or board[pos[0],pos[1]] == 0:
                        board[pos[0],pos[1]] = wire_num
                    else:
                        board[pos[0],pos[1]] = -2
            elif step[0] == "L":
                for i in range(step[1]):
                    pos[0] -= 1
                    if board[pos[0],pos[1]] == wire_num or board[pos[0],pos[1]] == 0:
                        board[pos[0],pos[1]] = wire_num
                    else:
                        board[pos[0],pos[1]] = -2


def search_for_X(board):
    min_dist = 10000000000
    min_pos = []
    for i in trange(len(board)):
        for j in range(len(board[0])):
            if board[i,j] == -2:
                dist = abs(15874 - i) + abs(7695 - j)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = (i,j)
                    #print(min_pos, board[i,j], min_dist)
    print(min_pos)
    return min_dist

def printboard(board, size):
    for j in range(size):
        print()
        for i in range(size):
            val = int(board[15874-(size//2) + i, 7695-(size//2) + j])
            if val == -1:
                print('O', end='')
            elif val == 0:
                print('.', end='')
            elif val == 1:
                print('|', end='')
            elif val == -2:
                print('X', end='')
            else:
                print(val, end='')


def main():
    wires = read_input()
    #size_of_grid(wires) I need a 22583x14404 start is at 15
    print("Initializing the board")
    board = np.zeros((22583,14404))
    print("Adding wires to the board")
    fill_board(board, wires)
    #printboard(board, 130)
    print("Performing Bruteforce search")
    min_dist = search_for_X(board)
    print(f'Minimum Manhattan Distance: {min_dist}')


if __name__ == "__main__":
    main()