lines = open('07.txt').read().split('\n')[:-1]

cmds = ['rm -rf 07made','mkdir 07made','cd 07made']
for line in lines[1:]:
    if line.startswith('$ cd'):
        cmds.append(line[2:])
    elif line.startswith('dir'):
        cmds.append('mk'+line)
    elif line.split(' ')[0].isdigit():
        size, name = line.split(' ')
        cmds.append(f'/usr/bin/python3 "/home/toben/Code/Advent of Code/07filler.py" {size} {name}')

cmds.append('cd "/home/toben/Code/Advent of Code/"')
open('07maker.bash','w').write('\n'.join(cmds))
