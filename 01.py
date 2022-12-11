print(max([sum([int(line) for line in chunk.split('\n') if line.isdigit()]) for chunk in open('01.txt').read().split('\n\n')]))
