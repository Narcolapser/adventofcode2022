pairs = open('04.txt').read().split('\n')

duplicate = 0
tests = 0
for pair in pairs:
    if pair == '':
        continue
    p1, p2 = pair.split(',')
    p1 = [int(v) for v in p1.split('-')]
    p2 = [int(v) for v in p2.split('-')]
    
    p1 = {i for i in range(p1[0],p1[1]+1)}
    p2 = {i for i in range(p2[0],p2[1]+1)}
    
    intersect = p1.intersection(p2)
    if len(intersect) > 0:
        duplicate += 1

print(duplicate)
