from tqdm import tqdm # For pretty loading bar

min = int(input('Enter the lower bound: '))
max = int(input('Enter the upper bound: '))
num_passwd = 0
for i in tqdm(range(min, max)):
    last_digit = 10
    last_last_digit = 11
    double = False
    digit_check = True
    for j in range(6):
        digit = i % 10
        next_digit = (i//10) % 10
        next_next_digit = (i//100) % 10
        #print(last_last_digit, last_digit, digit, next_digit, next_next_digit)
        if digit > last_digit:
            digit_check = False
            break
        # Extrodinarly ugly code the creates a 5 wide sliding window
        if (digit == last_digit and digit != next_digit and digit != last_last_digit) or (digit == next_digit and digit != last_digit and digit != next_next_digit):
            double = True
        last_last_digit = last_digit
        last_digit = digit
        i = i // 10
    if double and digit_check:
        num_passwd += 1

print(num_passwd)