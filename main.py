print('Welcome to my quiz!')

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok, lets play!")

answer = input("What is the name of the pub at the entrance to Diagon Alley? ")
answer = answer.lower()

if answer == "the leaky cauldron" or answer == "leaky cauldron": 
    print('Correct!')
else: 
    print("Incorrect")


answer = input("What is the name of Harry's Owl? ")
answer = answer.lower()

if answer == "hedwig": 
    print('Correct!')
else: 
    print("Incorrect")


answer = input("What are the code names for Remus Lupin, Peter Pettigrew, Sirius Black, James Potter? ")
answer = answer.lower().replace(",", "")
code_names = [name.strip() for name in answer.split()]

required_code_names = ["moony", "wormtail", "padfoot", "prongs"]

if set(code_names) == set(required_code_names):
    print('Correct!')
else:
    print('Incorrect')

answer = input("What is Voldemort's full real name? ")
answer = answer.lower()
if answer == "tom marvolo riddle":
     
    print('Correct!')
else: 
    print("Incorrect")

answer = input("What painting guards the entrance to the Gryffindor common room? ")
answer = answer.lower()
if answer == "the fat lady" or answer == "fat lady": 
    print('Correct!')
else: 
    print("Incorrect")


answer = input("Where in Kings Cross Station does the Hogwarts Express stop? ")
answer = answer.lower()
if answer == "platform 9 3/4" or answer == "platform nine and three quarters": 
    print('Correct!')
else: 
    print("Incorrect")


answer = input("The wizarding version of marbles is called what? ")
answer = answer.lower()
if answer == "gobstones": 
    print('Correct!')
else: 
    print("Incorrect")

answer = input("What is the name of the Weasley twins' magical joke store? ")
answer = answer.lower().replace("'", "")
required_answer = "weasleys' wizard wheezes"

if answer == required_answer.replace("'", ""):
    print('Correct!')
else:
    print('Incorrect')



answer = input("In book 5, Snape is assigned to teach what kind of magic? ")
answer = answer.lower()
if answer == "occlumency": 
    print('Correct!')
else: 
    print("Incorrect")


answer = input("What does O.W.L.s for one of the main wizarding exams stand for? ")
answer = answer.lower()
if answer == "ordinary wizarding level": 
    print('Correct!')
else: 
    print("Incorrect")

