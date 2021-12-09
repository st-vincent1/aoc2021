with open('input_file', 'r') as f:
    lines = f.read().splitlines()

""" 1b """
sum_3 = []

for x in range(len(lines)-2):
    sum_3.append(int(lines[x]))
    for c in range(1,3):
        sum_3[x] += int(lines[x+c])

lines = sum_3
print(lines)
""" 1a """
increased = 0
for x in range(1, len(lines)):
    if int(lines[x-1]) < int(lines[x]):
        increased += 1

print(increased)


