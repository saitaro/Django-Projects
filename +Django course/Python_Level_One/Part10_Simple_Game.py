import random
digits = list(range(10))
random.shuffle(digits)
code = digits[:3]

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

while True:
    guess = input("What is your guess? ")
    if not guess.isdigit() or len(guess) != 3:
        print('It should be 3 digits!')
        continue
    guess = [int(char) for char in guess]
    if guess == code:
        print("Congratulations! You've broken the code!")
        break
    if set(guess) & set(code):
        for i in range(3):
            if guess[i] == code[i]:
                print('Match')
                break
        else:
            print('Close')
    else:
        print('Nope')
