combos = {
    # Rock
    "A X": 3 + 0, # lose, choose scissors
    "A Y": 1 + 3, # tie, choose rock
    "A Z": 2 + 6, # win, choose paper
    # Paper
    "B X": 1 + 0, # lose, choose rock
    "B Y": 2 + 3, # tie, choose paper
    "B Z": 3 + 6, # win, choose scissors
    # Scissors
    "C X": 2 + 0, # lose, choose paper
    "C Y": 3 + 3, # tie, choose scissors
    "C Z": 1 + 6, # win, choose rock
    '':0 # key error preventor
}

values = [combos[line] for line in open('02.txt').read().split('\n')]
print(values)
print(sum(values))
