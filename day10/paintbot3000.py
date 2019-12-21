from EIntMachine import EIntMachine
import numpy as np

imach = EIntMachine('input.txt')
hull = np.zeros((100,100), dtype=int)
ispainted = np.zeros((100,100), dtype=int)
x = 50
y = 50
hull[x,y] = 1
direction = 0 # 0:UP, 1:RIGHT, 2:DOWN, 3:LEFT

#for i in range(25):
while True:
    val = imach.run_program()
    color = imach.input(int(hull[x,y]))
    if val is False:
        break
    hull[x,y] = color
    ispainted[x,y] = 1
    rot = imach.run_program()
    
    if rot == 1:
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    if direction == 0:
        y += 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y -= 1
    elif direction == 3:
        x -= 1
    else:
        print('ERROR')

sum = 0
for i in range(100):
    print()
    for j in range(100):
        if hull[i,j] == 0:
            print('.', end='')
        else:
            print('#', end='')
            sum += 1


print(np.sum(ispainted))