import time
from enum import Enum

def task1():
    with open("d23input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    graph = {}
    for line in lines:
        n1, n2 = line.split("-")
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []

        graph[n1].append(n2)
        graph[n2].append(n1)

    tuples = []
    for x in graph.keys():
        if x[0] != "t":
            continue

        for y in graph.keys():
            if x == y:
                continue

            if y not in graph[x]:
                continue

            if y in graph[x]:
                for z in graph.keys():
                    if z == y:
                        continue

                    if z not in graph[x] or z not in graph[y]:
                        continue

                    tuples.append(tuple(sorted([x,y,z])))
    print(len(set(tuples)))


    print(time.time() - ttt)


def task2():
    with open("d23input.txt", "r") as f:
        lines = f.read().split("\n")
    ttt = time.time()

    graph = {}
    for line in lines:
        n1, n2 = line.split("-")
        if n1 not in graph:
            graph[n1] = []
        if n2 not in graph:
            graph[n2] = []

        graph[n1].append(n2)
        graph[n2].append(n1)

    groups = [{x} for x in graph.keys()]
    past_g = None
    while past_g is None or len(groups) > 0:
        new_groups = []
        for group in groups:
            # For each item, get all neighbors.
            # Get an union of those neighbors.
            # For each union, make a new group together with the old guys.

            neighbors = set(graph.keys())
            for node in group:
                neighbors = neighbors.intersection(graph[node])

            for neighbor in neighbors:
                # print(f"Joined {neighbor} to {','.join(sorted(list(group)))}")
                new_groups.append(group.union({neighbor}))

        past_g = groups
        new_groups = [set(y) for y in set([tuple(sorted(list(x))) for x in new_groups])]
        groups = new_groups
    print(len(past_g[0]))
    print(past_g[0])
    print(",".join(sorted(list(past_g[0]))))


    print(time.time() - ttt)


if __name__ == '__main__':
    task1()
    task2()
