lines = open('07.txt').read().split('\n')[:-1]

tree = {}
pointer = '/'
directories = {}

# Create a list of file:
for line in lines:
    #print(line)
    if line[0] == '$': # it is a command
        if 'ls' in line:
            continue # We don't actually care
        elif line == '$ cd /':
            pointer = '/'
        elif line == '$ cd ..':
            if len(pointer) == 1:
                continue # can't go any lower than root.
            else:
                pointer = '/'.join(pointer.split('/')[:-2]) + '/'
            print(f'Moved down to {pointer}')
        else:
            print(line)
            pointer += line.split(' ')[2] + '/'
            print(f'Moved up into {pointer}')
        #print('Moved into ' + pointer)
    elif line[0] == 'd': # it is a directory
        tree[pointer+line.split(' ')[1]+'/'] = 'dir'
        directories[pointer+line.split(' ')[1]+'/'] = 0
        #print('Saw a directory ' + pointer+line.split(' ')[1])
    else: # it is a file
        tree[pointer+line.split(' ')[1]] = line.split(' ')[0]
        #print('Saw a file ' + pointer+line.split(' ')[1])

#for f in tree:
#    print(f,tree[f])
for d in directories:
    print(d)

# calculate the sizes of each directory
outs = 0
for directory in directories:
    total = 0
    for f in tree:
        if f.startswith(directory) and tree[f] != 'dir':
            total += int(tree[f])
    directories[directory] = total
    if total < 100000:
        outs += total

print(outs)

# guessed 1659962 but it was to low.
