import random

name = input("What is your name :- ")
print("\n")
print("Welcome to the game",name,". It is the game of guessing the word")
print("\n")
words = ["apple","banana","orange","grapes","pineapple","watermelon","mango"]

print("You will have to guess only from these words :- " ,words)

word = random.choice(words) # choosing random word from above array
print(word)

print("Now guess the characters ");
guesses = " " #guesses act as a container to store all the guesses made by the user
turn = 7 # we have only 7 turns if we get wrong
while(turn>0):
  filled = 0 
  for char in word: # all character of words arrive through char
    if char in guesses:
      print(char, end  = " ") # the char in guesses will be print
    else:
      print("_") # _ will come if char is not in guesses
      filled +=1 
  print("\n")
  if filled == 0: # if all the char are in guesses then filled will 0
    print("You won")
    print("Your word is ",word)
    break
  guess = input("Write your guess :- ") #taking input char or string
  guesses += guess # adding guess to guesses
  print(guesses)  # only for understanding
  if guess not in word: # doubt if we use guesses instead of guess
    turn -= 1
    print("Wrong guess")
    print("You have",turn,"turns left")
    if turn == 0:
      print("You lose")




