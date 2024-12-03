import re
with open("test.txt") as file:
    input = file.read()
    #input = input.splitlines()

'''    
strs = re.findall('(?<=mul\()(\d+,\d+\))', input)

muls = []
for mul in strs:
    (one, snd) = mul.split(",")
    snd = snd[:-1]
    mul = (int(one), int(snd))
    print(mul)
    muls.append(mul)

print(muls)

sums = 0
for mul in muls:
    sums += mul[0] * mul[1]

print(sums)

'''

strs = re.findall('((?<=mul\()(\d+,\d+\)))|(do()|don\'t())', input)