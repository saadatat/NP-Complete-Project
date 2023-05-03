"""
    name:  Zane Metz
    Random Algorithm for approximating Longest Path
    
"""
import random
import time


def longestapp(graph, weights, u, visited):
    poss = []
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            poss.append(v)
    if len(poss) == 0:
        return ([],0)
    v = random.choice(poss)
    next = longestapp(graph, weights, v, visited)
    return ([v] + next[0], weights[(u,v)] + next[1])


def main():    
    start = time.perf_counter()
    numv, nume = [int(x) for x in input().split()]
    graph = {}
    weights = {}
    nodes = []

    for _ in range(nume):
        u, v, w = input().split()
        w = int(w)
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v not in graph:
            graph[v] = []
        if u not in nodes:
            nodes.append(u)
        weights[(u,v)] = w

    longest = []
    sum = 0
    for _ in range(numv * 2):
        u = random.choice(nodes)
        next = longestapp(graph, weights, u, set())
        temp = ([u] + next[0], 0 + next[1])
        if temp[1] > sum:
            longest = temp[0]
            sum = temp[1]
    
    elapsed = time.perf_counter() - start
    print(sum)
    print(" ".join(longest))
    # print(elapsed)
    pass


if __name__ == "__main__":
    main()