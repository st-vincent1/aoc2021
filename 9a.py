import numpy as np

if __name__ == '__main__':

    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
    rows = [[int(x) for x in line] for line in lines]
    arr_ = np.pad(np.array(rows), [(1,), (1,)], mode='constant', constant_values=10)
    result = 0
    for i in range(1, arr_.shape[0]-1):
        for j in range(1, arr_.shape[1]-1):
            val = arr_[i][j]
            neighbours = min([arr_[i-1][j], arr_[i+1][j], arr_[i][j-1], arr_[i][j+1]])
            if val < neighbours:
                result = result + val + 1
    print(result)