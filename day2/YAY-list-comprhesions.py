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
    tape_pos = 0
    while True:
        print(tape_pos, mem)
        op_code = mem[tape_pos]
        if op_code == 1:
            mem[mem[tape_pos + 3]] = mem[mem[tape_pos + 1]] + mem[mem[tape_pos + 2]]
        elif op_code == 2:
            mem[mem[tape_pos + 3]] = mem[mem[tape_pos + 1]] * mem[mem[tape_pos + 2]]
        elif op_code == 99:
            return
        else:
            print("INVALID OPCODE")
            quit(-1)
        tape_pos += 4


def main():
    main_mem = create_main_mem()

    temp = int(input("First Value: "))
    main_mem[1] = temp
    temp = int(input("Second Value: "))
    main_mem[2] = temp

    run_program(main_mem)
    print(main_mem[0])

if __name__ == "__main__":
    main()