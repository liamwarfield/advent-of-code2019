from EIntMachine import EIntMachine
from copy import deepcopy
from itertools import permutations

initialized_machine = EIntMachine('input.txt')
signal_strengths = []
for phase_setting in permutations([5,6,7,8,9]):
    signal = 0
    amplifiers = [deepcopy(initialized_machine) for x in range(5)]
    for i in range(5):
        amplifiers[i].run_program()
        amplifiers[i].input(phase_setting[i]) # Input phase setting
    amp_num = 0
    while(True):
        temp = amplifiers[amp_num].input(signal)
        amplifiers[amp_num].run_program()
        if temp is False:
            break
        else:
            signal = temp
            amp_num = (amp_num + 1) % 5
    signal_strengths.append(signal)
print(max(signal_strengths))