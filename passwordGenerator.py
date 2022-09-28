import random

numberOfLetters = 0
numberOfSymbols = 0
numberOfNumbers = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
generatoredPassword = []
passwordGenerated = ''

welcomeMessage = 'Welcome to password generator.\n'
numberOfLetters = int(input('How many Letters will you like in your password?'))
numberOfSymbols = int(input('How many Symbols will you like in your password?'))
numberOfNumbers = int(input('How many Numbers will you like in your password?'))
passwordLength = numberOfLetters + numberOfNumbers + numberOfSymbols

for i in range(1, passwordLength+1):
    if numberOfLetters > 0:
        generatoredPassword.append(random.choice(letters))
        numberOfLetters -= 1
    elif numberOfSymbols > 0:
        generatoredPassword.append(random.choice(symbols))	
        numberOfSymbols -= 1
    elif numberOfNumbers > 0:
        generatoredPassword.append(random.choice(numbers))	
        numberOfNumbers -= 1
random.shuffle(generatoredPassword)
print(f'Your secure user generated password is,\n{passwordGenerated.join(generatoredPassword)}')