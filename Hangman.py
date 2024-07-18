"""
This program will play games of hangman with the user. 
The user can select a difficulty, earn a win streak, and play for as long as they desire.
"""

import random
print("Let's play hangman!")
print("I'm assuming you know how to play this game already, so let me explain how it's gonna work here.")
print("You can only get 5 strikes for each word. Everytime you make a wrong guess, you gain 1 strike. If you reach the strike limit, you lose.")
print("You also begin with a certain amount hints, which will reveal a singular letter of the word. Use them wisely!")
print("By getting multiple words correct in a row, you can earn a win streak. Your streak will go up by 1 for each word.")
print("However, the higher your win streak is, the harder it'll be to maintain it!")
print("You will be able to make less and less mistakes as you keep winning.")
print("How far will you be able to go?")
print("---------------------------------------------------------------------------")
print("There's three difficulties for you to choose from: ")
print("Easy: Shorter words no longer than 4 letters, 10 hints")
print("Medium: A mix of short and medium length words no longer than 6 letters, 15 hints")
print("Hard: Words longer than 7 letters, 20 hints")
print("")

# making the game loop
while True: 

    # actually making the game
    while True:
        diff_choice = input("Select difficulty (Enter E/M/H): ")
        # each of these diff variables store the name of a .txt file, which will then be used to open that file, as seen on line 44
        if diff_choice.upper() == "E":
            diff = "easy_words.txt"
            print("You chose easy difficulty.")
            break
        elif diff_choice.upper() == "M":
            diff = "med_words.txt"
            print("You chose medium difficulty.")
            break
        elif diff_choice.upper() == "H":
            diff = "hard_words.txt"
            print("You chose hard difficulty.")
            break
        else:
            print("Please enter a valid input.")

    print("Let's begin!")
    print("===========================================================================")

    # obtaining word from word list, and defining streak and strike limit variables
    word_list = open(diff)
    choose_word = word_list.readlines()
    streak = 0
    strike_limit = 5

    # defining a function for replayability
    def replay():
        while True:
            choice = input("Would you like to play again?(Y/N): ")
            if choice.upper() == "Y":
                # clearing the user's win streak if they lost and chose to replay
                if strikes == strike_limit:
                    print("Your win streak of has been reset.")
                print("Alright, let's go again!")
                print("===========================================================================")
                return True
            elif choice.upper() == "N":
                if "_" not in letters:
                    print("You finished with a win streak of " + str(streak) + ".")
                    print(win_streak_response())
                    print("")
                return False
            else:
                print("Please enter a valid input.")

    # defining a function for responses to the win streak
    def win_streak_response():
        if streak == 0:
            return "That's alright, you can always try again."
        elif streak > 0 and streak <= 5:
            return "Nice job!"
        elif streak > 5 and streak <= 10:
            return "Great job!"
        elif streak > 10 and streak <= 15:
            return "Excellent job!!"
        elif streak > 15 and streak <= 20:
            return "Amazing job!!!"
        elif streak > 20:
            return "PHENOMINAL job!!!!"

    # the program will not end unless the user wants it to
    while True:

        # defining vars (and closing the .txt file)
        word = choose_word[random.randint(0, 199)].strip().upper()
        word_list.close()
        letters = ""
        crosses = ""
        strikes = 0
        used_guesses = []

        # defining the hint var
        if streak == 0:
            if diff == "easy_words.txt":
                hints = 10
            elif diff == "med_words.txt":
                hints = 15
            elif diff == "hard_words.txt":
                hints = 20

        # changing the strike limit
        # every time you get 5 wins in a row, you'll get 1 less mistake, up until 20 wins, after which you'd only get to make 1 mistake
        if streak % 5 == 0 and streak != 0 and streak <= 20:
            if strike_limit != 1:
                strike_limit -= 1
                if strike_limit == 1:
                    print("Wow, good job making it this far! You get only 1 strike now. Only perfection from here on out!")
                    print("")
                else:
                    print("Let's make things a little more challenging! You can now only get " + str(strike_limit) + " strikes before losing!")
                    print("")

        # creating the letter placeholders
        for i in range(len(word)):
            letters += "_"

        print("The word is " + str(len(word)) + " letters long.")
        print(letters)
        print("")

        # the user will lose if they get 5 strikes
        while strikes < strike_limit:
            print("You have " + str(hints) + " hints remaining.")

            # getting the user's input
            while True:
                # saving the user's guess as an uppercase letter so it's easier to compare to the word
                guess = input("Enter a single letter as a guess, or enter 'hint' to reveal one of the letters: ").upper()
                # generating a hint
                if guess == "HINT":
                    if hints > 0:
                        hints -= 1
                        print("")
                        print("You used one of your hints.")
                        while True:
                            hint_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                            if hint_letter in used_guesses or hint_letter not in word:
                                continue
                            else:
                                break
                        print("The letter " + hint_letter + " is in the word!")
                        letters = list(letters)
                        for i in range(len(word)):
                            if hint_letter == word[i]:
                                letters[i] = hint_letter
                        letters = ("").join(letters)
                        print(letters)
                        print("---------------------------------------------------------------------------")
                        used_guesses += hint_letter
                        break
                    elif hints == 0:
                        print("You're out of hints!")
                        continue
                
                elif len(guess) != 1 or guess == "":
                    print("Your guess must be a single letter.")
                    continue
                elif guess.isalpha() != True:
                    print("Your guess must be a letter.")
                    continue
                elif guess in used_guesses:
                    print("You already guessed the letter " + guess + ".")
                    continue
                else:
                    used_guesses += guess
                    break

            # checking if the guess is in the word
            if guess in word:
                print("")
                print("The letter " + guess + " is in the word!")
                letters = list(letters)
                for i in range(len(word)):
                    if guess == word[i]:
                        letters[i] = guess
                letters = ("").join(letters)
                print(letters)
                print("---------------------------------------------------------------------------")

            # if the guess is not in the word, the user will get a strike
            elif guess not in word and guess != "HINT":
                print("")
                strikes += 1
                print("The letter " + guess + " is not in the word.")
                print("Strike " + str(strikes) + "!")
                crosses += "X"
                print(crosses)
                print("---------------------------------------------------------------------------")

            # if there's no brackets in the letters variable, that must mean that the user has won
            # the game must end in this case 
            if "_" not in letters:
                break
        
        word = ("").join(word)

        # response if user wins
        if strikes < strike_limit:
            print("YOU WIN!")
            print("You have guessed the word! It was " + word + ".")
            streak += 1
            print("You now have a win streak of " + str(streak) + "!")

        # response if the user loses
        elif strikes == strike_limit:
            print("YOU LOSE!")
            print("You ran out of attempts! The word was " + word + ".")
            print("You lost with a win streak of " + str(streak) + ".")
            print(win_streak_response())
            streak = 0
            strike_limit = 5

        # if the user chooses to not replay, break out of the loop and end the program
        if replay() == False:
            break

    end = input("Do you want to choose a new difficulty and play again? (Y/N):").upper()
    if end == "Y":
        print("===========================================================================")
        continue
    elif end == "N":
        print("Thanks for playing!")
        print("===========================================================================")
        break
    else:
        print("Invalid input. Ending the program by default.")
        print("Thanks for playing!")
        print("===========================================================================")
        break