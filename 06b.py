lines = open('06.txt').read().split('\n')[:-1]

for line in lines:
    buf = list(line)
    trim = []
    marker = []
    while len(set(marker)) < 14:
        if len(marker) >= 14:
            trim.append(marker.pop(0))
        marker.append(buf.pop(0))
    print(len(trim)+14)
