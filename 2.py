with open('input_file', 'r') as f:
    lines = f.read().splitlines()

dirs = {
    'forward': 0,
    'up': 0,
    'down': 0
}

""" 1a """
# for line in lines:
#     dir, num = line.split()
#     dirs[dir] += int(num)


# print(dirs['forward'] * (dirs['down'] - dirs['up']))

""" 1b """

aim = 0
hor_pos = 0
depth = 0

for line in lines:
    dir_, num_ = line.split()
    if dir_ == 'forward':
        hor_pos += int(num_)
        depth += aim * int(num_)
    if dir_ == 'down':
        aim += int(num_)
    if dir_ == 'up':
        aim -= int(num_)

print(hor_pos*depth)