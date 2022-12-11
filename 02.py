combos = {
    # Rock
    "A X": 1 + 3, # Rock
    "A Y": 2 + 6, # Paper
    "A Z": 3 + 0, # Scissors
    # Paper
    "B X": 1 + 0, # Rock
    "B Y": 2 + 3, # Paper
    "B Z": 3 + 6, # Scissors
    # Scissors
    "C X": 1 + 6, # Rock
    "C Y": 2 + 0, # Paper
    "C Z": 3 + 3, # Scissors
    '':0 # key error preventor
}

values = [combos[line] for line in open('02.txt').read().split('\n')]
print(sum(values))
