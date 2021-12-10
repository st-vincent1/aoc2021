import queue


def is_open(bracket):
    return bracket in ['[', '<', '{', '(']


def get_points(b):
    points_ = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return points_[b]


def match(b_o, b_c):
    if (b_o, b_c) in [
        ('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')
    ]:
        return True
    return False


def get_matching(b):
    match_ = {
        '{': '}',
        '(': ')',
        '<': '>',
        '[': ']'
    }
    return match_[b]


if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
        lines = [[c for c in line] for line in lines]

    result_cor, result_inc_ = 0, []

    for line in lines:
        result_inc = 0
        q1 = queue.LifoQueue()
        corrupted = False
        for b in line:
            if is_open(b):
                q1.put(b)
            elif not match(q1.get(), b):
                corrupted = True
                result_cor += get_points(b)
                break
        # End of input
        if not q1.empty() and not corrupted:
            while not q1.empty():
                result_inc = result_inc * 5 + get_points(q1.get())
            result_inc_.append(result_inc)

    print("10a answer:", result_cor)
    print("10b answer:", sorted(result_inc_)[len(result_inc_) // 2])
