from class_example import Student, Question
from Chef import Chef
from ChineseChef import ChineseChef

student_1 = Student('Jim Carry', 'Perform Art', 3.9, False)
student_2 = Student('Natalie Portman', 'Astronomy', 2.2, True)

print(student_1)
print(student_2.name)

question_promts = [
    "What color are apples?\n(a) Red/Green \n(b) Purple \n(c) Orange \n\n",
    "What color are Bananas? \n(a)Teal \n(b)Magenta \n(c) Yellow\n\n",
    "What color are strawberries? \n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)

myChef = Chef()
myChef.makes_special_dish()

myChineseChef = ChineseChef()
myChineseChef.makes_special_dish()