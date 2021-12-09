
def get_common_elements(lst):
    commons = lst[0].intersection(lst[1], lst[2])
    _609_uniq = [k - commons for k in lst]
    return _609_uniq[0].union(_609_uniq[1], _609_uniq[2])

def map_to_actual_positions(number, mapping):
    new_number = ''
    for s_ in number:
        s_ = mapping[s_]
        new_number = new_number + s_
    return new_number
def map_set_to_digit(set_):
    if set_ == set('abcefg'): return 0
    if set_ == set('cf'): return 1
    if set_ == set('acdeg'): return 2
    if set_ == set('acdfg'): return 3
    if set_ == set('bcdf'): return 4
    if set_ == set('abdfg'): return 5
    if set_ == set('abdefg'): return 6
    if set_ == set('acf'): return 7
    if set_ == set('abcdefg'): return 8
    if set_ == set('abcdfg'): return 9

if __name__ == '__main__':

    with open('input_file', 'r') as f:
        lines = f.read().splitlines()

    sum_ = 0

    for line in lines:
        a, b = line.split(' | ')
        a = a.strip().split()
        b = b.strip().split()
        sorted_digs = sorted(a, key=lambda x: len(x))
        CF = set(sorted_digs[0])
        A = set(sorted_digs[1]) - CF
        BD = set(sorted_digs[2]) - CF

        # 6, 0, 9
        union_609 = get_common_elements([set(sorted_digs[6]), set(sorted_digs[7]), set(sorted_digs[8])])

        C = union_609.intersection(CF, union_609)
        D = union_609.intersection(BD, union_609)
        B = BD - D
        E = union_609 - C.union(D)

        # 2, 3, 5
        union_235 = get_common_elements([set(sorted_digs[3]), set(sorted_digs[4]), set(sorted_digs[5])])
        F = union_235.intersection(CF, union_235) - C
        G = set(sorted_digs[8]) - union_235.union(union_609, B, A)
        # Create mappings
        mapping = {
            ''.join(A): 'a',
            ''.join(B): 'b',
            ''.join(C): 'c',
            ''.join(D): 'd',
            ''.join(E): 'e',
            ''.join(F): 'f',
            ''.join(G): 'g'
        }
        digits = ''
        for number in b:
            n_ = map_to_actual_positions(number, mapping)
            digits = digits + str(map_set_to_digit(set(n_)))
        sum_ += int(digits)
    print(sum_)