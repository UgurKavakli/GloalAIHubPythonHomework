from words import word_list
import random    

def PickWord():
    word = random.choice(word_list)
    return word.upper()

def PlayGame(word):
    hidden = "_" * len(word)        
    is_guessed = False
    guessed_letters = []
    attempts = 6
    
    print(f"Number of attempts left: {attempts}")
    print(hidden)
    print("\n")
    
    while not is_guessed and attempts > 0:
        guess = input("Your guess is: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed {guess}")
                print(f"Number of attempts left: {attempts}")
                print(hidden)
                print("\n")
            elif guess not in word:
                print("Wrong guess")
                guessed_letters.append(guess)
                attempts -= 1
                print(f"Number of attempts left: {attempts}")
                print(hidden)
                print("\n")
            else:
                print("Good guess!")
                guessed_letters.append(guess)
                hidden_list = list(hidden)
                indicies = [i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    hidden_list[index] = guess
                hidden = "".join(hidden_list)
                print(f"Number of attempts left: {attempts}")
                print(hidden)
                print("\n")
                if "_" not in hidden:
                    is_guessed = True
        else:
            print("Not a valid input.")
            print(hidden)
            print(f"Number of attempts left: {attempts}")
            print("\n")
    if is_guessed:
        print("Congrats! You've guessed the word correctly")
    else:
        print(f"Sorry but the man is hanged. the word was {word}")

def Game():
    player = input("Please enter your name: ")

    while True:
        y_or_n = input(f"Welcome {player}. Are you ready to play hangman? (y/n)")
        if y_or_n.upper() == "Y":
            print("\n")
            break
        else:
            continue
    word = PickWord()
    PlayGame(word)
    while input("Would you like to try again? (Y/N) ").upper() == "Y":
        word = PickWord()
        PlayGame(word)
        
    
Game()
    


    