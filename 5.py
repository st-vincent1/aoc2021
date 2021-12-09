import copy
import numpy as np

with open('input_file') as f:
    lines = f.read().splitlines()

board = np.zeros((1000, 1000))
for line in lines:
    a, b = line.split(' -> ')
    x1, y1 = a.split(',')
    x2, y2 = b.split(',')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if x1 == x2 or y1 == y2:
        y1_, y2_ = min(y1, y2), max(y1, y2)
        x1_, x2_ = min(x1, x2), max(x1, x2)
        # print('lol')
        board[y1_:y2_+1, x1_:x2_+1] += 1
    else:
        if x1 > x2 and y1 > y2:
            (x1, y1), (x2, y2) = (x2, y2), (x1, y1)
        if x1 < x2 and y1 < y2:
            np.fill_diagonal(board[y1:y2 + 1, x1:x2 + 1], board[y1:y2 + 1, x1:x2 + 1].diagonal() + 1)
        else:
            if x1 > x2 and y1 < y2:
                (x2, y2), (x1, y1) = (x1, y2), (x2, y1)
            elif x1 < x2 and y1 > y2:
                (x1, y1), (x2, y2) = (x1, y2), (x2, y1)
            np.fill_diagonal(np.fliplr(board[y1:y2+2, x1:x2 + 1]),
                             np.fliplr(board[y1:y2+2, x1:x2 + 1]).diagonal() + 1)

print(np.sum(board >= 2))