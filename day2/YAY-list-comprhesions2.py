import copy
def create_main_mem():
    main_mem = {}
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    main_mem = [int(x) for x in f.readline().split(",")] # Yay
    f.close()
    return main_mem

def run_program(mem):
    instruction_ptr = 0
    while True:
        op_code = mem[instruction_ptr]
        if op_code == 1:
            mem[mem[instruction_ptr + 3]] = mem[mem[instruction_ptr + 1]] + mem[mem[instruction_ptr + 2]]
        elif op_code == 2:
            mem[mem[instruction_ptr + 3]] = mem[mem[instruction_ptr + 1]] * mem[mem[instruction_ptr + 2]]
        elif op_code == 99:
            return
        else:
            print("INVALID OPCODE")
            quit(-1)
        instruction_ptr += 4


def main():
    main_mem = create_main_mem()
    for noun in range(100): # Brute force best force
        for verb in range(100):
            mem_cp = copy.deepcopy(main_mem)
            mem_cp[1] = noun
            mem_cp[2] = verb
            run_program(mem_cp)
            if(mem_cp[0] == 19690720):
                print(f"noun={noun} verb=verb{verb} The answer is: ", noun * 100 + verb)
                quit(0)


    temp = int(input("First Value: "))
    main_mem[1] = temp
    temp = int(input("Second Value: "))
    main_mem[2] = temp

    run_program(main_mem)
    print(main_mem[0])

if __name__ == "__main__":
    main()