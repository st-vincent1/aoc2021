import itertools
import copy
import queue


def add_to_edges(a, b):
    for p1, p2 in [(a, b), (b, a)]:
        if p1 == 'end' or p2 == 'start': continue
        try:
            e[p1] = e[p1] + [p2]
        except KeyError:
            e[p1] = [p2]
    return e


def set_visibility(vis, node):
    if node.islower():
        vis[node] += 1
    return vis


def bfs(e, extra_cave):
    to_visit = queue.Queue()
    node = 'start'
    score = 0
    paths = []
    vis = {k_: 0 for k_ in e.keys()}
    vis[extra_cave] = -1
    vis = set_visibility(vis, node)
    for neighbour in e[node]:
        if vis[neighbour] != 1:
            to_visit.put((neighbour, [node, neighbour], copy.deepcopy(vis)))

    while not to_visit.empty():
        node, path_, vis = to_visit.get()
        if node == 'end':
            score += 1
            paths.append(path_)

        vis = set_visibility(vis, node)
        for neighbour in e[node]:
            if vis[neighbour] != 1:
                to_visit.put((neighbour, path_ + [neighbour], copy.deepcopy(vis)))
    return score, paths


if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
        e = {}
        paths_ = []
        for line in lines:
            a, b = line.split('-')
            e = add_to_edges(a, b)
        e['end'] = []

        for cave in e.keys():
            if cave.islower() and cave not in ['start', 'end']:
                print(cave)
                score, paths = bfs(e, cave)
                paths_ = paths_ + paths
        paths_.sort()
        paths = list(k for k, _ in itertools.groupby(paths_))
        print(len(paths))
