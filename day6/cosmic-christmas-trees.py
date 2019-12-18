class Node:
    def __init__(self):
        self.children = []
        self.parent = None
        self.depth = -1


def read_input():
    system = {}
    try:
        f = open("input.txt")
    except FileNotFoundError:
        print("Could not find an input file")
        f.close()
        quit(-1)
    for line in f:
        planet, satalite = line.rstrip().split(')')
        if planet in system:
            system[planet].children.append(satalite)
        else:
            system[planet] = Node()
            system[planet].children.append(satalite)
        if satalite in system:
            system[satalite].parent = planet
        else:
            system[satalite] = Node()
            system[satalite].parent = planet
    system['COM'].depth = 0
    return system

# Breadth first searce
def num_orbits(system):
    s_queue = ['COM']
    num = 0
    while len(s_queue) > 0:
        next_node = s_queue.pop(0)
        print(next_node, system[next_node].children)
        depth = system[next_node].depth
        for child in system[next_node].children:
            system[child].depth = depth + 1
            s_queue.append(child)
        num += depth
    return num

def main():
    solar_system = read_input()
    num = num_orbits(solar_system)
    print(num)

if __name__ == "__main__":
    main()