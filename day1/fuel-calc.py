def calc_fuel(weight):
    return (weight // 3) - 2

def main():
    total = 0
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    for line in f:
        total += calc_fuel(int(line))
    print(total)
    f.close()

if __name__ == "__main__":
    main()