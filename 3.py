import numpy as np
import copy

with open('input_file', 'r') as f:
    lines = f.read().splitlines()


dim_0, dim_1 = len(lines[0]), len(lines)
print(dim_0)
x = [int(a) for line in lines for a in line]
x = np.reshape(np.array(x), (-1, dim_0))

""" 3a """
counts = np.apply_along_axis(lambda z: np.bincount(z), 0, x)
gamma = np.apply_along_axis(lambda z: np.argmax(z), 0, counts)
epsilon = np.apply_along_axis(lambda z: np.argmin(z), 0, counts)
gamma_ = int(''.join([str(s) for s in gamma]), 2)
epsilon_ = int(''.join([str(s) for s in epsilon]), 2)
print(gamma_ * epsilon_)

threshold = dim_1 // 2
threshold_most = threshold
threshold_least = threshold
least_ = x
most_ = copy.deepcopy(x)
""" 3b """
for k in range(dim_0):
    # print(most_, threshold_most)
    if np.count_nonzero(most_[:, k]) >= threshold_most:
        # Dropping rows with one
        most_ = most_[most_[:,k] == 1]
    else:
        most_ = most_[most_[:, k] == 0]
    if most_.shape[0] == 1:
        print(most_[0])
        break
    threshold_most = most_.shape[0] / 2
for k in range(dim_0):
    # print(least_, threshold_least)
    if np.count_nonzero(least_[:, k]) < threshold_least:
        # Dropping rows with one
        least_ = least_[least_[:, k] == 1]
    else:
        least_ = least_[least_[:, k] == 0]
    if least_.shape[0] == 1:
        print(least_[0])
        break
    threshold_least = least_.shape[0] / 2


gamma_ = int(''.join([str(s) for s in least_[0]]), 2)
epsilon_ = int(''.join([str(s) for s in most_[0]]), 2)
print(gamma_ * epsilon_)