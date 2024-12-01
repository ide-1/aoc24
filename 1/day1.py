with open("input.txt") as file:
    input = file.read()
    input = input.splitlines()

left = []
right = []


for line in input:
    line = line.split(" ")
    #print(line)
    left.append(int(line[0]))
    right.append(int(line[-1]))

left.sort()
right.sort()

diffs = []

for i in range(len(left)):
    num = abs(left[i] - right[i])
    diffs.append(num)


sums = sum(diffs)

print(sums)

### part 2 

sims = []

for i in range(len(left)):
    sims.append(left[i]*right.count(left[i]))

print(sum(sims))