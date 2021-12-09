import numpy as np

def calc_distance(x, k):
    score = 0
    for i in range(len(x)):
        diff = 1
        distance = np.absolute(k - x[i])
        while distance:
            score += diff
            diff += 1
            distance -= 1
    return score
with open('input_file', 'r') as f:
    lines = f.read().splitlines()
#
x = lines[0].split(',')
x = np.array([int(s) for s in x])
# candidates = np.arange(max(np.median(x) - 500, 0), np.median(x) + 750)
# best_k = -1
# best_sum = 10000000000
# for k in candidates:
#     print(k)
#     candidates_sums = calc_distance(x, k)
#     if candidates_sums < best_sum:
#         best_sum = candidates_sums
#         best_k = k
#
# print(best_sum, candidates[int(best_k)])
print(np.median(x))
print(np.sum(np.absolute(x - int(np.median(x)))))