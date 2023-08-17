secret_word = 'pronounciation'
lives = 6
letter = input#("Enter a letter: ")
final_guess=secret_word


for i in range(0,14):
65    letter = input("Enter a letter: ")

    if letter in secret_word:
        print('Your answer is',letter in secret_word)
        lives=lives+1
        print(lives,"You gained a life!")
        if lives == 0:
            print("You lost Oh No:(")
            break

    else:
        print('Your answer is',letter in secret_word)
        lives=lives-1
        print(lives,"You lost a life:(")
        if lives == 0:
            print("You lost Oh No:(")
            break

final_guess=input("Enter your FINAL GUESS")
final_guess==secret_word
print('Your Final GUESS is',final_guess in secret_word)





##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##letter = input("Enter a letter: ")
##print('Your answer is',letter in secret_word)
##final_guess = input("Enter your final guess ")

