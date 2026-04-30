print("Welcome to my Computer Quiz Game. ")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

score = 0

print("Okay! Let's Play :)")
answer = input("What does CPU stands for: ").lower()
if answer == "central processing unit":
    print("Correct! Here is your candy: 🍬")  
    score += 1
else:
    print("Incorrect. ")  

answer = input("What does GPU stands for: ").lower()
if answer == "graphics processing unit":
    print("Correct! Here is your candy: 🍬")
    score += 1  
else:
    print("Incorrect. ")  

answer = input("What does RAM stands for: ").lower()
if answer == "random access memory":
    print("Correct! Here is your candy: 🍬")
    score += 1  
else:
    print("Incorrect. ")  

answer = input("What does PSU stands for: ").lower()
if answer == "power supply unit":
    print("Correct! Here is your candy: 🍬")
    score += 1  
else:
    print("Incorrect. ")  

print("You got " + str(score ) + " questions right. ")
print("You got" + str((score/4) * 100 ) + " %")