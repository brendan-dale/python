import random
print('H A N G M A N')
print('Type "play" to play the game, "exit" to quit:')
play_or_quit = input()
if play_or_quit == quit:
    quit()

word_list = ['python', 'java', 'kotlin', 'javascript']
word = list(random.choice(word_list))
hidden_word = list('-' * len(word))
mistakes = 0
all_letters = ""

while mistakes < 8:
    print()
    print(''.join(hidden_word))
    letter = input('Input a letter:')

    if letter in all_letters:
        print("You've already guessed this letter")
        continue
    
    if len(letter) > 1:
        print("You should input a single letter")
        continue
    
    if letter in hidden_word:
        print("No improvements")
        #mistakes += 1
    
    if not letter.islower():
        print("Please enter a lowercase English letter")
        continue
    
    if letter not in word:
        print("That letter doesn't appear in the word")
        mistakes += 1
        all_letters += letter
    else: 
        for i in range(len(word)):
            if word[i] == letter:
                hidden_word[i] = letter
        all_letters += letter

    if hidden_word == word:
        print("You guessed the word! \n You survived!")
        quit()
print("You lost!")