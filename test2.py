
import random
use = 'y'
adjectives = ['sleepy','slow','smelly','wet','fat','red','orange','purple','green','blue','yellow','fluffy','white','proud','brave']
nouns = ['apple', 'dinosaur', 'ball','toaster', 'goat', 'dragon','hammer', 'duck', 'panda']
punctuations = ['#','.','@','!','?','/',]
while use == 'y':
    adjective = random.choice(adjectives)
    #print(adjective)
    noun = random.choice(nouns)
    #print(noun)
    num = random.randrange(0,99)
    #print(num)
    punctuation=random.choice(punctuations)
    #print(punctuation)
    print(adjective+noun+punctuation+str(num))
    choice = input("enter y to continue and n to stop(y/n)")
    if choice == 'y':
        print(adjective+noun+punctuation+str(num))
    else:
        print("incorect input recieved")
        break
 
