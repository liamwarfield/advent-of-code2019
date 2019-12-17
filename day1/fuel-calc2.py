def calc_fuel(weight):
    total_fuel = 0
    new_fuel = (weight // 3) - 2
    while True:
        total_fuel += new_fuel
        new_fuel = (new_fuel // 3) -2
        if new_fuel <= 0:
            return total_fuel

def main():
    total = 0
    iteration = 0
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    for line in f:
        print(iteration)
        total += calc_fuel(int(line))
        iteration += 1
    print(total)
    f.close()

if __name__ == "__main__":
    main()