#function
def animalt(ans,guess):
    score = 0
    using = 'yes'
    while using=='yes':
        if guess == ans:
            score += 1
            print("Congratulations you have gained 1 point by answering this question right!")
            return score
        else:
            print("wrong answer two tries left try again")
            score-=1
            guess = input("Enter your answer here: ")  
            return score
        
#main code
            
print("Hello, This is Crazy Dave's Animal Trivia")
print("Heres how to play Dave's Animal Trivia. #1 You have 3 tries to get the questions right. #2 Your score will be revealed at the end of the game. #3 NO GOOGLE SEARCHES IF YOU DO BUBBA WILL COME FOR YOU")
print("Question 1. How many talons does a eagle have?")
g1 = (input("Enter your answer here:"))
a1=animalt('8',g1)
print("Your score is",a1)

print("Question 2. What is the slowest mammal?")
g1 = (input("Enter your answer here:"))
a2=animalt('sloths',g1)
print("Your score is",a2+a1)

print("Question 3. What is the fastest land mammal?")
g1 = (input("Enter your answer here:"))
a3=animalt('cheetah',g1)
print("Your score is",a3+a2+a1)

print("Question 4. What is the biggest land animal?")
g1 = (input("Enter your answer here:"))
a4=animalt('elephant',g1)
print("Your score is",a4+a3+a2+a1)

print("Question 5. Name a amphibian?")
g1 = (input("Enter your answer here:"))
a5=animalt('frog',g1)
print("Your score is",a5+a4+a3+a2+a1)


