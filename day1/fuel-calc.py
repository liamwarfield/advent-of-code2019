def calc_fuel(weight):
    return (weight // 3) - 2

def main():
    total = 0
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        quit()
    for line in f:
        total += calc_fuel(int(line))
    print(total)

if __name__ == "__main__":
    main()