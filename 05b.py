lines = open('05.txt').read().split('\n')

# Create the stacks:
line = lines.pop(0)
stacks = [[] for i in range(int((len(line)+1)/4))]
while '[' in line:
    for i,stack in enumerate(stacks):
        if line[i*4+1] != ' ':
            stack.append(line[i*4+1])
    line = lines.pop(0)

# Remove blank lines
lines.pop(0)
lines.pop()

print(stacks)
for line in lines:
    _, amount, _, origin, _, dest = line.split(' ')
    temp = []
    for i in range(int(amount)):
        temp.insert(0, stacks[int(origin)-1].pop(0))
    for i in temp:
        stacks[int(dest)-1].insert(0,i)
    print(stacks)

for stack in stacks:
    print(stack[0], end='')
