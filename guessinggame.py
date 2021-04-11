import random

number = random.randint(1, 9)

chance = 0

while chance < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
          print("You have guessed correctly!")
          break

    elif guess > number:
         print("The number is less than", guess)

    else:
         print("The number is greater than", guess)

    chance = chance + 1
if chance > 5:
     print("You have lost")
