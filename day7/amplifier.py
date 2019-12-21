from EIntMachine import EIntMachine
from copy import deepcopy
from itertools import permutations

initialized_machine = EIntMachine('input.txt')
signal_strengths = []
for phase_setting in permutations([0,1,2,3,4]):
    signal = 0
    for i in range(5):
        amp = deepcopy(initialized_machine) # Create Machine
        amp.run_program()
        amp.input(phase_setting[i]) # Input phase setting
        signal = amp.input(signal)
    signal_strengths.append(signal)
print(max(signal_strengths))