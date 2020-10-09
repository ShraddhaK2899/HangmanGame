import random
# Library that to choose random words from a list of words




name = input("What is your name? ") 
print("Good Luck ", name)
 
words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks'] 
print("Guess the Word")
 
#from Wordsforhangman import word_list
#import random

#To select any random word from the list
def get_word():
  word = random.choice(words)
  return word.upper() #Transfers the output to some other variable

#To actually play the game
def play(word):
  word_completion = "_" * len(word)
  print(word_completion)
  guessed = False
  guessed_letter = []
  guessed_word = []
  tries = 6

  print("Lets play Hangman!! ")
  print(word_completion)
  print(display_hangman(tries))
  print(word_completion)
  print("\n")

  while not guessed and tries > 0:
    guess = input('Enter your guess: ').upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letter:
        print(f'You have already guessed the letter', guess)
      elif guess not in word:
        print(guess, "is not in the word. ")
        tries -= 1
        guessed_letter.append(guess)
      #Heart of the Program - Converts Blank into Letter (Replacing)
      else:
        print("Good Job!", guess, "is the word!")
        guessed_letters.append(guess)
        word_as_list = list(word_completion) #Converson into list
        
        #for i, letter in enumerate(word):
        #  if letter == guess:
        #    indices.append(i)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_complerion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True
      print(word_completion)

    #Checks length of word given as input with actual word
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed.word:
        print("You have already guessed the word", guess)
      # Checkinh 'test != 'text'
      elif guess !=word:
        print(guess, "is not the word.")
        tries -= 1
        guessed_word.append(guess)
      else:
        guessed = True
        word_completion = word
        print("You guessed the word right! Its ", guess)
    else:
      print('Not A Valid Guess.')
      
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
      if guessed:
        print("Congrats, you guessed the word! You win!")
      else:
        print("Sorry, you ran out of tries. the word was ", word)


#diplaying the hangman 
def displayHangman(tries):
  stages = [
            #6 Final State: Head, Torso, Both Arms and Both Legs
        """
           --------
           |    | 
           |    O
           |   \\|/
           |    |
           |   / \\
           -
        """,
            #5 Head, Torso, Both Arms and One Leg
        """
           --------
           |    | 
           |    O
           |   \\|/
           |    |
           |   / 
           -
        """,
            #4 Head, Torso, Both Arms
        """
           --------
           |    | 
           |    O
           |   \\|/
           |    |
           |  
           -
        """,
            #3 Head, Torso, One Arm
        """
           --------
           |    | 
           |    O
           |   \\|
           |    
           |   
           -
        """,
            #2 Head and Torso
        """
           --------
           |    | 
           |    O
           |   \\|/
           |    |
           |   / \\
           -
        """,
            #1 Head
        """
           --------
           |    | 
           |    O
           |    
           |    
           |   
           -
        """,
            #0 Initial Empty State
        """
           --------
           |    | 
           |  
           |  
           |  
           |  
           -
        """
  ]     
  return stages[tries]


def main():
  word = getRandom()
  print(word)
  play(word)
  
  while input('Do you want to play again? (Y/N: ').upper == 'Y':
    word = getRandom()
    play(word)
  else:
    print('See you next time! Bye!')
    
main()