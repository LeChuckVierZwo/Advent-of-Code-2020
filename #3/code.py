import fileinput

input = []

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for line in fileinput.input("input"):
    input.append(list(line.strip()))

trees = 1
for (_right, _down) in slopes:
    down = 0
    right = 0
    sum = 0
    while down+1 < len(input):
        right += _right
        down += _down
        if input[down][right%len(input[down])] == "#":
            sum += 1
    trees *= sum
print(trees)