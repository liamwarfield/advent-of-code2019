from collections import defaultdict
from enum import Enum
import logging
logging.basicConfig(level=logging.INFO)
import sys

class IntMachine:
    class IO(Enum):
        HUMAN = 0
        COMPUTER = 1
    def __init__(self, inputfile, iomode=IO.HUMAN, loglevel=logging.ERROR):
        self.tape_pos = 0
        self.on_fire = False
        self.iomode = iomode
        self.logger = logging.getLogger('intMachines')
        self.logger.setLevel(loglevel)
        self.rbase_offset = 0
        self.create_main_mem(inputfile)
        self.instruction_lengths = {
            1:3,
            2:3,
            3:1,
            4:1,
            5:3,
            6:3,
            7:3,
            8:3,
            9:2,
            99:3
        }

    def create_main_mem(self, ifile):
        main_mem = {}
        try:
            f = open(ifile)
        except FileNotFoundError:
            print("Could not find an input file")
            quit(-1)
        mem = [int(x) for x in f.readline().split(",")] # Yay
        main_mem = defaultdict(int) # Uninitialized memory is 0
        for i in range(len(mem)):
            main_mem[i] = mem[i]
        f.close()
        self.mem = main_mem

    '''
    Parse's an instruction and returns the values of the arguements
    '''
    def parse_instruction_args(self, instruction, mem, tape_pos):
        op_code = instruction % 100
        num_args = self.instruction_lengths[op_code]
        write_arg = num_args -1
        instruction //= 100
        
        modes = [0 for x in range(3)]
        args = [0 for x in range(3)]
        for i in range(num_args):
            modes[i] = instruction % 10
            instruction //= 10
        self.logger.debug(f"Modes, {modes}")
        
        for i in range(3):
            if modes[i] == 2:   # Relative Base
                #print("relative mem: ",tape_pos, mem[tape_pos + i + 1], self.rbase_offset, tape_pos + mem[tape_pos + i + 1] + self.rbase_offset)
                relative_pos = mem[tape_pos + i + 1] + self.rbase_offset
                args[i] = mem[relative_pos]
            elif modes[i] == 1: # Immediant mode
                args[i] = mem[tape_pos + i + 1]
            else:              # Positional mode
                args[i] = mem[mem[tape_pos + i + 1]]
        if modes[write_arg] == 2:
            #print("relative mem: ",tape_pos, mem[tape_pos + write_arg + 1], self.rbase_offset, tape_pos + mem[tape_pos + write_arg + 1] + self.rbase_offset)
            args[write_arg] = mem[tape_pos + write_arg + 1] + self.rbase_offset
            #print(args[write_arg])
        else:
            args[write_arg] = mem[tape_pos + 1 + write_arg]
        self.logger.debug(f"Arguments: {args}")
        return (op_code, args[0], args[1], args[2])
        #self.logger.info("Local Memory", tape_pos, mem[tape_pos: tape_pos +12])
    
    '''
    Run a program until it halts.
    '''
    def run_program(self):
        while True:
            if not self.exec_instruction():
                break
        print([self.mem[x] for x in range(10)])
    
    '''
    Steps the machine through one instruction
    '''
    def exec_instruction(self):
        mem = self.mem
        tape_pos = self.tape_pos
        instruction = mem[self.tape_pos]
        self.logger.debug(f"Instruction: {instruction, self.tape_pos}")
        op_code, arg1, arg2, arg3 = self.parse_instruction_args(instruction, mem, self.tape_pos)
        self.logger.debug(f"OpCode: {op_code}")
        if op_code == 1: # Add
            mem[arg3] = arg1 + arg2
            self.tape_pos += 4
        elif op_code == 2: # Multiply
            mem[arg3] = arg1 * arg2
            self.tape_pos += 4
        elif op_code == 3: # Input
            mem[arg1] = int(input('Please input a value: '))
            self.tape_pos += 2
        elif op_code == 4: # Print
            print(mem[arg1])
            self.tape_pos += 2
        elif op_code == 5: # Jump if true
            if arg1:
                self.tape_pos = arg2
            else:
                self.tape_pos += 3
        elif op_code == 6: # Jump if false
            if not arg1:
                self.tape_pos = arg2
            else:
                self.tape_pos += 3
        elif op_code == 7: # Less than
            if arg1 < arg2:
                mem[arg3] = 1
            else:
                mem[arg3] = 0
            self.tape_pos += 4
        elif op_code == 8: # Equals
            if arg1 == arg2:
                mem[arg3] = 1
            else:
                mem[arg3] = 0
            self.tape_pos += 4
        elif op_code == 9: # Set relative base
            self.rbase_offset += arg1
            self.tape_pos += 2
            self.logger.debug(f'rbase ={self.rbase_offset, arg1}')
        elif op_code == 99:
            return False
        else:
            self.logger.error(f"INVALID OPCODE: {op_code}")
            self.on_fire = True
            return False
        self.logger.debug('\n')
        return True

def main():
    input_file = sys.argv[1]
    if '-v' in sys.argv:
        I_machine = IntMachine(input_file, loglevel=logging.DEBUG)
    elif '-vv' in sys.argv:
        I_machine = IntMachine(input_file, loglevel=logging.INFO)
    else:
        I_machine = IntMachine(input_file)
    I_machine.run_program()

if __name__ == "__main__":
    main()