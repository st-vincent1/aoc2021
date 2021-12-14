from collections import Counter

def count_score(sc):
    print(sc.most_common()[0][1] - sc.most_common()[-1][1])
def step(r, pc, sc):
    # increase single count by the middle element
    new_pc = {k_: 0 for k_ in pc.keys()}
    new_sc = {k_: 0 for k_ in sc.keys()}
    for key, (pair_a, pair_b, middle) in r.items():
        if pc[key] > 0:
            # this pair is in the polymer
            new_pc[pair_a] += pc[key]
            new_pc[pair_b] += pc[key]
            new_sc[middle] += pc[key]
            new_pc[key] -= pc[key]
    pc = Counter(pc)
    new_pc = Counter(new_pc)
    pc.update(new_pc)

    sc = Counter(sc)
    new_sc = Counter(new_sc)
    sc.update(new_sc)
    return pc, sc

if __name__ == '__main__':
    with open('input_file', 'r') as f:
        lines = f.read().splitlines()
    polymer = lines[0]
    rules = {}
    sc = {k_: 0 for k_ in polymer}
    for c in polymer:
        sc[c] += 1
    for line in lines[2:]:
        a,b = line.split(' -> ')
        rules[a] = (a[0] + b, b + a[1], b)
        if b not in sc.keys():
            sc.update({b: 0})
    pc = {k_: 0 for k_ in rules.keys()}

    for k in range(2, len(polymer)+1):
        pc[polymer[k-2:k]] += 1

    for k in range(40):
        pc, sc = step(rules, pc, sc)

    count_score(sc)