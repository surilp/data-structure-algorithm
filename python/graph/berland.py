from disjoint_set import DSU


def berland(connections, cities):
    dsu = DSU(cities + 7)
    can_be_removed = []
    for city1, city2 in connections:
        parent1 = dsu.find_parent(city1)
        parent2 = dsu.find_parent(city2)
        if parent1 == parent2:
            can_be_removed.append((city1, city2))
        else:
            dsu.union(city1, city2)
    parent_set = set()
    for city in range(1, cities + 1):
        parent_set.add(dsu.find_parent(city))

    print(can_be_removed, parent_set)


cities = 7

connections = [
    (1, 2),
    (2, 3),
    (3, 1),
    (4, 5),
    (5, 6),
    (6, 7)
]

berland(connections, cities)