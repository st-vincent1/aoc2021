import numpy as np
import copy
import networkx as nx


def expand_caves(map_):
    ver_stacks = []
    for k in range(0, 5):
        temp = map_ + k
        temp = np.where(temp >= 10, temp - 9, temp)
        ver_stacks.append(temp)
    ver_stacks = np.concatenate((ver_stacks), axis=0)
    new_map = copy.deepcopy(ver_stacks)
    for k in range(1, 5):
        temp = ver_stacks + k
        temp = np.where(temp >= 10, temp - 9, temp)
        new_map = np.concatenate((new_map, temp), axis=1)

    return new_map

def gen_nx_graph(data):
    G = nx.DiGraph()
    for y in range(len(data)):
        for x in range(len(data)):
            G.add_node((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x_, y_ = x + dx, y + dy
                if 0 <= x_ < len(data) and 0 <= y_ < len(data):
                    G.add_edge((x, y), (x_, y_), weight=data[y_][x_])
    return G

example = ["1163751742",
           "1381373672",
           "2136511328",
           "3694931569",
           "7463417111",
           "1319128137",
           "1359912421",
           "3125421639",
           "1293138521",
           "2311944581"]

if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
    map_ = np.array([[int(c) for c in x] for x in lines])

    map_ = expand_caves(map_)
    X = len(map_)
    Y = len(map_[0])
    map_ = np.pad(map_, [(1,), (1,)], mode='constant', constant_values=9999999)
    G = gen_nx_graph(map_)
    path = nx.shortest_path(G, source=(1, 1), target=(X, Y), weight='weight')
    risk = sum(map_[y][x] for x, y in path[1:])
    print(risk)