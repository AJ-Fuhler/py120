CHOICE_ABBREVIATIONS = {
    'rock': ['r'],
    'paper': ['p'],
    'scissors': ['s', 'sc'],
    'lizard': ['l'],
    'spock': ['sp'],
}

VALID_CHOICES =  [
    print(item) for key, value in CHOICE_ABBREVIATIONS.items()
         for item in [key] + value]

COMPUTER_CHOICES = list(CHOICE_ABBREVIATIONS.keys())

print(VALID_CHOICES)