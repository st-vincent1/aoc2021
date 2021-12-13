import pprint as pp
import numpy as np
import itertools
import sys

def fold_along(indices, axis, loc):
    for idx in range(len(indices)):
        pos = 0 if axis == 'x' else 1
        a = indices[idx][pos]
        if a > loc:
            a = 2*loc - a
            indices[idx][pos] = a
    return indices

if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
    folds = []
    indices = []

    max_x = -1
    max_y = -1
    for line in lines:
        if 'fold' in line:
            _, _, a = line.split()
            folds.append(a.split('='))
        elif ',' in line:
            x,y = line.split(',')
            indices.append([int(x),int(y)])

    """ 13a """
    indices_ = fold_along(indices, folds[0][0], int(folds[0][1]))
    indices_.sort()
    print(len(list(k for k, _ in itertools.groupby(indices))))

    """ 13b """
    for fold in folds:
        indices = fold_along(indices, fold[0], int(fold[1]))

    x = np.chararray((6, 40))
    x[:] = '.'
    indices.sort()
    for x_, y_ in list(k for k, _ in itertools.groupby(indices)):
        x[y_, x_] = '#'

    for a in x:
        for k in a:
            print(str(k, 'utf-8'), end='')
        print()