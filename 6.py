with open('input_file', 'r') as f:
    lines = f.read().splitlines()

x = lines[0].split(',')
x = [int(s) for s in x]

y = [0] * 9
for a in x:
    y[a] += 1

for k in range(256):
    print(y)
    temp_null = y[0]
    for val in range(1,9):
        y[val-1] = y[val]
    y[8] = temp_null
    y[6] += temp_null

print(sum(y))