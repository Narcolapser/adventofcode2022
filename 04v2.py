pairs = open('04.txt').read().split('\n')

enclosures = 0
tests = 0
for pair in pairs:
    if pair == '':
        continue
    p1, p2 = pair.split(',')
    p1 = [int(v) for v in p1.split('-')]
    p2 = [int(v) for v in p2.split('-')]
    
    p1 = {i for i in range(p1[0],p1[1]+1)}
    p2 = {i for i in range(p2[0],p2[1]+1)}
    
    union = p1.union(p2)
    if not (len(union) > len(p1) and len(union) > len(p2)):
        enclosures += 1

print(enclosures)
