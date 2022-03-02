print ("Welcom to the IQ test")

                                                        #asking the user if they want to play
print ("Do you want to play?")                                                     
playing = input("Press 'Y' to continue: ")               #promt
if playing.lower() != "y" :
    quit()

name = input("Please enter you name: ")                 #name

print("Okay " +name+ ", lets start your test")
score = 0                                               #score
                                                        #question 1
answer = input("What does 'www' stands for?\n")
if answer.lower() == "world wide web" :
    print("Correct!")
    score += 1
else:
    print("Incorrect")
                                                        #question 2
answer = input("What is fear of spiders called?\n")
if answer.lower() == "arachnophobia" :
    print("Correct!")
    score += 1 
else:
    print("Incorrect")
                                                        #question 3
answer = input("In little red riding hood, who does the wolf dress up as?\n")
if answer.lower() == "grandmother" :
    print("Correct!")
    score += 1
else:
    print("Incorrect")
                                                        #question 4
answer = input("How many bones are there in human body?\n")
if answer.lower() == "206" :
    print("Correct!")
    score += 1
else:
    print("Incorrect")
                                                        #question 5
answer = input("What is Earth's largest continent?\n")
if answer.lower() == "asia" : 
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print ("Congratulations! You got " + str((score/5)*100) + "% of the questions correct")
print ("Your score is " + str(score*5) + " marks")
print ("Thank you for taking the test.")