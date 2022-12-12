lines = open('03.txt').read().split('\n')
total = 0

while len(lines) >= 3:
    first = set(lines.pop(0))
    second = set(lines.pop(0))
    third = set(lines.pop(0))
    common = first.intersection(second).intersection(third)
    if len(common) == 0:
        continue
    value = ord(common.pop())
    if value > 90:
        total += value-96
    else:
        total += value-64+26
        
print(total)
