from random import randint

def main():
  level = int(input("how many digits? "))
  number = randint(10**(level-1), (10**level)-1)
  while True:
    guess = int(input("Guess: "))
    if guess == number:
       print("Correct")
       break
    elif guess > number:
       print("Low")
    elif guess < number:
       print('higher')


main()
