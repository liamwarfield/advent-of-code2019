class Node:
    def __init__(self, name):
        self.children = []
        self.parent = None
        self.depth = -1
        self.data = name
    
    def __repr__(self):
        return repr(self.data)


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
            system[planet] = Node(planet)
            system[planet].children.append(satalite)
        if satalite in system:
            system[satalite].parent = planet
        else:
            system[satalite] = Node(satalite)
            system[satalite].parent = planet
    system['COM'].depth = 0
    return system

# Breadth first searce
def num_orbits(system):
    s_queue = ['COM']
    num = 0
    while len(s_queue) > 0:
        next_node = s_queue.pop(0)
        depth = system[next_node].depth
        for child in system[next_node].children:
            system[child].depth = depth + 1
            s_queue.append(child)
        num += depth
    return num

# Potentially O(n^2), but good enough for this
def LCA(n1, n2, system):
    parents = [n1.data]
    node = n1
    while node.parent != None:
        node = system[node.parent]
        parents.append(node.data)
    node = n2
    while node.parent not in parents and node.parent != None: # Could cause O(n) search O(n) times, O(n^2)
        node = system[node.parent]
    return system[node.parent]


def dist_to_santa(system):
    santa = system['SAN']
    you = system['YOU']
    num_orbits(system) # Creates depth information needed.
    last_common_anc = LCA(you, santa, system)
    
    # The -2 compensates for double counting the LCA
    return abs(last_common_anc.depth - you.depth) + abs(last_common_anc.depth - santa.depth) - 2

def main():
    solar_system = read_input()
    num = dist_to_santa(solar_system)
    print(num)

if __name__ == "__main__":
    main()