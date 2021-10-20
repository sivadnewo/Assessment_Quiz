# Functions
def q1 ():
    question = input("What colour is an  apple ").strip().lower()

    answer = "red"

    if question == answer:
        print("Congratulations you got it correct")
        score += 1
    else:
        print("Sorry thats incorrect")

    print()
    print("Score:{}".format(score))

def q2 ():
    question = input("Is a tomato a fruit? ").strip().lower()

    answer = "yes"

    if question == answer:
        print("Congratulations you got it correct")
        score += 1
    else:
        print("Sorry thats incorrect")

    print()
    print("Score:{}".format(score))



# Main routine goes here

# Score
score = 0

q1()


