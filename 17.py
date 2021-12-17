import pprint as pp

def closer_to_zero(num):
    if num < 0: return num + 1
    if num > 0: return num - 1
    return num


def count_x_stops(k_x, k_y, x_a, x_b, y_a, y_b):
    if (k_x+1) * k_x/2 < x_a:
        return False, y_a
    pos = 0, 0
    maks = y_a
    is_successful = False
    while pos[0] <= x_b:
        if x_a <= pos[0] <= x_b and y_a <= pos[1] <= y_b:
            is_successful = True
        if pos[1] > maks:
            maks = pos[1]
        pos = pos[0] + k_x, pos[1] + k_y
        k_x = closer_to_zero(k_x)
        k_y -= 1
        if pos[1] < y_a: break
    return is_successful, maks

def parse_input(inp):
    inp = inp[15:]
    x, y = inp.split(', y=')
    x_a, x_b = x.split('..')
    y_a, y_b = y.split('..')
    return int(x_a), int(x_b), int(y_a), int(y_b)


if __name__ == '__main__':
    puzzle_input = 'target area: x=57..116, y=-198..-148'
    targets = parse_input(puzzle_input)
    probes = {}
    global_max_y = targets[2]
    for k_x in range(targets[1]+1):
        for k_y in range(targets[2], 1000):
            probes[k_x, k_y] = count_x_stops(k_x, k_y, *targets)
            if probes[k_x, k_y][0]:
                global_max_y = max(global_max_y, probes[k_x, k_y][1])
    probes = {key: value for (key, value) in probes.items() if value[0] }
    print("Answer to 17a:", global_max_y)
    print("Answer to 17b:", len(probes))