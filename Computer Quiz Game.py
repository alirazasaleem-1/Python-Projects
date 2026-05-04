# Computer Quiz Game

questions = {
        "CPU stands for?": "central processing unit",
        "GPU stands for?": "graphics processing unit",
        "RAM stands for?": "random access memory",
        "PSU stands for?": "power supply unit"
    }

def start_game():
    print("Welcome to my Computer Quiz Game. ")

    playing = input("Do you want to play? ")

    if playing != "yes":
        quit()

    score = 0

    print("Okay! Let's Play :)")

    for question, correct_answer in questions.items():
        answer = input(question + " ").lower()

        if answer == correct_answer:
            print("Correct! 🍬")
            score += 1
        else:
            print("Incorrect ❌")

    print("\nGame Over 🎯")    
    print("You got " + str(score ) + " questions right. ")
    print("You got " + str((score/len(questions)) * 100 ) + " %")

start_game()