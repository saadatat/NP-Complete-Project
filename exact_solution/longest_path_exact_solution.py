import itertools
# import time


# Generate all permutations, find longest path. O(n*n!) run time :(
# Written by Arman Saadat
# Source: Dr. Bowers explained the logic behind this in class 4/24/23
#         To our group


def longest_path3(nodes, weights):

    # generate all the permutations of the list of nodes in the graph
    perms = list(itertools.permutations(nodes))

    longest_path_count = 0
    longest_path_nodes = []

    # Loop through every permutation
    for perm in perms:
        path_len = 0
        path = []

        # Loop through the nodes in this permutation
        for i, node in enumerate(perm[:-1]):

            # If this pair of nodes in the permutation is an edge
            if (perm[i], perm[i+1]) in weights:

                # Add the first node to the path if it is index 0 of perm
                if (i == 0):
                    path.append(perm[i])

                # Add the second node in the pair to the path
                path.append(perm[i+1])

                # Update path length
                path_len += weights[(perm[i], perm[i+1])]
            else:
                break

        # If the final path length for this permutation is the longest so far, update the variables
        if (path_len > longest_path_count):
            longest_path_count = path_len
            longest_path_nodes = path

    print(longest_path_count)
    print(' '.join(longest_path_nodes))


def main():
    # start_time = time.time()
    total = input()
    line_spl = total.split()
    num_edges = int(line_spl[1])


    edges = [input().split(' ') for _ in range(num_edges)]
    weights = dict()
    nodes = []

    # populate the weights list and nodes list
    for u, v, w in edges:
        u, v, w = u, v, int(w)
        if u not in nodes:
            nodes.append(u)
        if v not in nodes:
            nodes.append(v)

        weights[(u, v)] = w

    longest_path3(nodes, weights)
    # print("My program took", time.time() - start_time, "seconds to run")


if __name__ == "__main__":
    main()
