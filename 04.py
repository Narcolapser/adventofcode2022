pairs = open('04.txt').read().split('\n')

enclosures = 0
tests = 0
for pair in pairs:
    if pair == '':
        continue
    p1, p2 = pair.split(',')
    p1 = [int(v) for v in p1.split('-')]
    p2 = [int(v) for v in p2.split('-')]
    
    if p1[0] <= p2[0]:
        if p1[1] >= p2[1]:
            enclosures += 1
            print(f'{p1} and {p2} enclose1')
        else:
            print(f'{p1} and {p2} do not enclose2')
    else:
        if p1[1] <= p2[1]:
            enclosures += 1
            print(f'{p1} and {p2} enclose3')
        else:
            print(f'{p1} and {p2} do not enclose4')
    tests += 1
#    input()

print(enclosures,tests)
