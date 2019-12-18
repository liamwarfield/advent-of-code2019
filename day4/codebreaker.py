from tqdm import tqdm # For pretty loading bar

min = int(input('Enter the lower bound: '))
max = int(input('Enter the upper bound: '))
num_passwd = 0
for i in tqdm(range(min, max)):
    last_digit = 10
    double = False
    digit_check = True
    while i > 0:
        digit = i % 10
        if digit > last_digit:
            digit_check = False
            break
        if digit ==  last_digit:
            double = True
        last_digit = digit
        i = i // 10
    if double and digit_check:
        num_passwd += 1

print(num_passwd)