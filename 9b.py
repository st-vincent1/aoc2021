import numpy as np


def walk(arr_, visited, x, y, size):
    visited[x][y] = 1
    size += 1
    neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for x_, y_ in neighbours:
        if not visited[x_][y_] \
                and arr_[x_][y_] != 9:
             size = walk(arr_, visited, x_, y_, size)
    return size

def search_sizes(graph):
    sizes = []
    for x in range(1, graph.shape[0]-1):
        for y in range(1, graph.shape[1] - 1):
            if graph[x][y] != 9 and not visited[x][y]:
                size = walk(graph, visited, x, y, 0)
                sizes.append(size)
    return np.array(sizes)

if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
    rows = [[int(x) for x in line] for line in lines]

    arr_ = np.pad(np.array(rows), [(1,), (1,)], mode='constant', constant_values=9)
    sizes = []
    visited = np.zeros_like(arr_)
    sizes = search_sizes(arr_)

    print(np.prod(sizes[np.array(sizes).argsort()[-3:]]))
