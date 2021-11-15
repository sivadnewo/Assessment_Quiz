# Functions

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            print("Hope you enjoy:)")
            return response

        elif response == "no" or response == "n":
            response = "no"
            print("Too bad so sad, this is a maths quiz.")
            return response

        else:
            print("Please answer yes/no")
            print()

def question_ask(question, answer):
    error = "Please enter a whole number."
    global score
    try:
        response = int(input(question))
        if response == answer:
            print("Correct")
            score += 1
            print("Your current score is:",score)
            return response
        else:
            print("Incorrect")
            print("Your current score is:",score)
    except ValueError:
        print(error)

# introduction on the quiz
yes_no("Do you like maths? ")
print()


# Main rutine
score = 0
q1 = question_ask("What is 2 times 2? ",4)
print()
q2 = question_ask("What is the square root of 4? ",2)
print()
q3 = question_ask("What is 200 divided by 10? ",20)
print()
q4 = question_ask("What is 50 minus 32? ",18)
print()
q5 = question_ask("What is the nearest ten to 123456789? ",123456790)
print()
q6 = question_ask("What is the last number of the alphabet? ",26)
print()
q7 = question_ask("How many multiple of 2's are there in the number 12?",6)
print()
q8 = question_ask("What is 1 plus 1? ",2)
print()
q9 = question_ask("What is 50 times 50? ",2500)
print()
q10 = question_ask("What is (1 + 1)×2×2×2×2×2×2×2×2? ",512)
print()
print("GG YOU FINISHED")
print()
print("Your final score is: {} ".format(score))
print()
if score >= 5:
    print("Good job. Thanks for playing.")
else:
    print("Better luck next time. Thanks for playing")

