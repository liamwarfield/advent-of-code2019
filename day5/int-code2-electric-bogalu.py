from collections import defaultdict
def create_main_mem():
    main_mem = {}
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    mem = [int(x) for x in f.readline().split(",")] # Yay
    main_mem = defaultdict(int) # Uninitialized memory is 0
    for i in range(len(mem)):
        main_mem[i] = mem[i]
    f.close()
    return main_mem

def parse_instruction_args(instruction, mem, tape_pos):
    mode1 = (instruction // 100) % 10
    mode2 = (instruction // 1000) % 10
    mode3 = (instruction // 10000) % 10
    #print("Modes", mode1, mode2, mode3)
    #print(tape_pos, mem[tape_pos: tape_pos +12])
    if mode1 == 1: # Immediant 
        arg1 = mem[tape_pos + 1]
    else: # Positional mode
        arg1 = mem[mem[tape_pos + 1]]
    if mode2 == 1:
        arg2 = mem[tape_pos + 2]
    else:
        arg2 = mem[mem[tape_pos + 2]]
    if mode3 == 1:
        arg3 = mem[tape_pos + 3]
    else:
        arg3 = mem[mem[tape_pos + 3]]
    #print('Arguements: ', arg1, arg2, arg3)
    return (arg1, arg2, arg3)

def run_program(mem):
    tape_pos = 0
    while True:
        instruction = mem[tape_pos]
        #print("Instruction: ", instruction, tape_pos)
        op_code = instruction % 100
        arg1, arg2, arg3 = parse_instruction_args(instruction, mem, tape_pos)
        if op_code == 1: # Add
            mem[mem[tape_pos + 3]] = arg1 + arg2
            tape_pos += 4
        elif op_code == 2: # Multiply
            mem[mem[tape_pos + 3]] = arg1 * arg2
            tape_pos += 4
        elif op_code == 3: # Input
            mem[mem[tape_pos + 1]] = int(input('Please input a value: '))
            tape_pos += 2
        elif op_code == 4: # Print
            print(mem[mem[tape_pos + 1]])
            tape_pos += 2
        elif op_code == 5: # Jump if true
            if arg1:
                tape_pos = arg2
            else:
                tape_pos += 3
        elif op_code == 6: # Jump if false
            if arg1 == 0:
                tape_pos = arg2
            else:
                tape_pos += 3
        elif op_code == 7: # Less than
            if arg1 < arg2:
                mem[mem[tape_pos + 3]] = 1
            else:
                mem[mem[tape_pos + 3]] = 0
            tape_pos += 4
        elif op_code == 8: # Equals
            if arg1 == arg2:
                mem[mem[tape_pos + 3]] = 1
            else:
                mem[mem[tape_pos + 3]] = 0
            tape_pos += 4
        elif op_code == 99:
            return
        else:
            print("INVALID OPCODE", op_code)
            quit(-1)


def main():
    main_mem = create_main_mem()
    #print(main_mem[0])
    run_program(main_mem)

if __name__ == "__main__":
    main()