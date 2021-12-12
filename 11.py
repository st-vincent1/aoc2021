import numpy as np


def get_neighbours(x, y):
    return np.array([
        [x - 1, y - 1],
        [x - 1, y],
        [x - 1, y + 1],
        [x, y - 1],
        [x, y + 1],
        [x + 1, y - 1],
        [x + 1, y],
        [x + 1, y + 1],
    ])


def update_me_and_neighbours(map_, idxs, vis, flashes):
    for [x, y] in idxs:
        if not vis[x, y]:
            if map_[x, y] in [9, 10]:
                vis[x, y] = True
                flashes += 1
                map_[x, y] = 0
                map_, flashes = update_me_and_neighbours(map_, get_neighbours(x, y), vis, flashes)
            else:
                map_[x, y] += 1
    return map_, flashes


def one_step(map_, flashes, visited):
    # update all lights by 1
    assert np.where(map_ == 10)[0].size == 0
    map_ += 1
    temp_map, flashes = update_me_and_neighbours(map_, np.argwhere(map_ == 10), visited, flashes)
    while (map_ != temp_map).all():
        map_ = temp_map
        temp_map, flashes = update_me_and_neighbours(map_, np.argwhere(map_ == 10), visited, flashes)

    return map_, flashes


if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
        map_nopad = np.array([[int(c) for c in line] for line in lines])
    flashes = 0
    map_ = np.pad(map_nopad, [(1,), (1,)], mode='constant', constant_values=11)
    for i in range(10000):
        visited = np.pad(np.zeros_like(map_nopad),
                         [(1,), (1,)], mode='constant', constant_values=True)
        map_, flashes = one_step(map_, flashes, visited)
        if (map_[1:-1, 1:-1] == 0).all():
            print(f"First index is {i+1}!")
            break
    # print(f"Answer to 11a: {flashes}")
