
score = 0
# Asks user for input

question_1 = input("Is a tomato a fruit? ").strip().lower()

answer_1 = "yes"

if question_1 == answer_1:
    print("Congratulations you got it correct")
    score += 1
else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")

print()
print("Score:{}".format(score))
print()

question_2 = input("Is the sky red? ").strip().lower()

answer_2 = "no"

if question_2 == answer_2:
    print("Congratulations you got it correct")
    score += 1
else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")

print()
print("Score:{}".format(score))
print()

question_3 = input("1 plus 1 is 2? ").strip().lower()

answer_3 = "yes"

if question_3 == answer_3:
    print("Congratulations you got it correct")
    score += 1
else:
    print("Sorry thats incorrect, make sure you answer with yes or no.")

print()
print("Score:{}".format(score))
print()
print("You got {} out of 3 correct.".format(score))


