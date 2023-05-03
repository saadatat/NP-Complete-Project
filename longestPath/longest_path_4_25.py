# T/F Longest Path (NP Comlete as described by wikipedia)
# Always returns true if not a DAG.
def longest_path1(graph, weights, length):
    # helper function to recursively find a path of length >= provided
    def find_path(node, path_length):
        # base case: path of length provided or greater has been found
        if path_length >= length:
            return True
        # recursive case: try each neighbor of the current node
        if node in graph:
            for neighbor in graph[node]:
                # check if there is an edge between the current node and its neighbor
                edge = (node, neighbor)
                if edge in weights:
                    # recursively check if a path of length >= provided can be found starting at the neighbor
                    if find_path(neighbor, path_length + weights[edge]):
                        return True
        # no path of length >= provided was found
        return False

    # try starting at each node in the graph
    for start_node in graph:
        if find_path(start_node, 0):
            return True
    return False

# Solves the sample input/output in announcement
# Basically just a DFS, takes the longest of those paths
# Assumes no graph is cyclic, if it did, it would be infinite loop


def longest_path2(graph, weights):
    # Helper function to perform depth-first search
    def dfs(node, visited, path, max_path):
        # Add current node to path and mark as visited
        visited.add(node)
        path.append(node)
        # If the path is longer than the current maximum path, update the maximum path
        if len(path) > len(max_path):
            max_path[:] = path[:]
        # Recursively visit all neighbors of the current node
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    edge_weight = weights[(node, neighbor)]
                    dfs(neighbor, visited, path, max_path)
            # Backtrack by removing current node from path and mark as unvisited
        path.pop()
        visited.remove(node)

    # Initialize variables
    visited = set()
    path = []
    max_path = []
    # Perform depth-first search starting from each node in the graph
    for node in graph:
        if node not in visited:
            dfs(node, visited, path, max_path)
    # Compute the length of the longest path
    max_length = sum(weights[(max_path[i], max_path[i+1])]
                     for i in range(len(max_path)-1))
    # Return the longest path and its length
    return (max_path, max_length)


def main():
    total = input()
    line_spl = total.split()
    num_edges = int(line_spl[1])

    edges = [input().split(' ') for _ in range(num_edges)]
    graph = dict()
    weights = dict()

    # populate the graph and weights list
    for u, v, w in edges:
        u, v, w = u, v, int(w)
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]

        weights[(u, v)] = w

    print(longest_path1(graph, weights, 999))
    longest_path, total_weight = longest_path2(graph, weights)
    print(total_weight)
    print(longest_path)


if __name__ == "__main__":
    main()
