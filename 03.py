lines = open('03.txt').read().split('\n')
total = 0
for line in lines:
    half = int(len(line)/2)
    first = {char for char in line[:half]}
    second = {char for char in line[half:]}
    mistake_set = first.intersection(second)
    if len(mistake_set) == 0:
        continue
    value = ord(mistake_set.pop())
    if value > 90:
        print(value-96)
        total += value-96
    else:
        print(value-64+26)
        total += value-64+26
        
print(total)
