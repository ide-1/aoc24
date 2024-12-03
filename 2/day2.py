with open("test.txt") as file:
    input = file.read()
    input = input.splitlines()

for l in range(len(input)):
    input[l] = input[l].split(" ")
    #print (line)
    for i in range(len(input[l])):
        input[l][i] = int(input[l][i])
    #print(line)
#print(input)
'''
safes = 0
for line in input:
    prev = line[0]
    safe = True

    if prev - line[1] <=0:
        increasing = True
    else: 
        increasing = False
    for i in range(1, len(line)): 
        curr = line[i]

        if increasing:
            if prev > curr:
                safe = False
                break
            elif (curr - prev) <= 3 and (curr - prev) >= 1:
                prev = curr
            else:
                safe = False
                break
        else:
            if prev < curr:
                safe = False
                break
            elif (prev - curr) <= 3 and (prev - curr) >= 1:
                prev = curr
            else:
                safe = False
                break
    if safe:
        safes +=1
        print(line)

    #print(safes)
'''

### part 2 
def return_unsafes(line):
    unsafes = [0]*len(line)
    prev = line[0]
    curr = 0
    if len(line) >= 2:
        curr = line[1]
    if prev - curr <=0:
        increasing = True
    else: 
        increasing = False
    for i in range(1 ,len(line)):
        curr = line[i]
        if increasing:
            if (curr - prev) <= 3 and (curr - prev) >= 1:
                prev = curr
            else:
                unsafes[i] = 1
                unsafes[i-1] = 1
                prev = curr
        else:
            if (prev - curr) <= 3 and (prev - curr) >= 1:
                prev = curr
            else:
                unsafes[i] = 1
                unsafes[i-1] = 1
                prev = curr

    return unsafes


unsafes = [0]*len(input)
for l in range(len(input)):
    prev = input[l][0]
    safe = True

    if prev - input[l][1] <=0:
        increasing = True
    else: 
        increasing = False
    for i in range(1, len(input[l])): 
        curr = input[l][i]

        if increasing:
            if prev > curr:
                safe = False
                break
            elif (curr - prev) <= 3 and (curr - prev) >= 1:
                prev = curr
            else:
                safe = False
                break
        else:
            if prev < curr:
                safe = False
                break
            elif (prev - curr) <= 3 and (prev - curr) >= 1:
                prev = curr
            else:
                safe = False
                break    
    if not safe:
        unsafes[l] = 1
#510
safes = 2
for l in unsafes:
    if l == 1:
        unsafes = return_unsafes(input[l])
        for u in range(len(unsafes)):
            if u == 1:
                test = input[l]
                print(input[l])
                test.pop(u)
                if return_unsafes(test).count(1) == 0:
                    safes +=1
                    print(input[l])
                    print(test)
                    break
                else:
                    continue
            else: 
                continue
    else:
        continue

print(safes)
       
        


                
#print(return_unsafes([1, 3, 2, 4, 5]))
