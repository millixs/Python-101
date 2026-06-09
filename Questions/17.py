# Program to create a Quiz Game

# EXPLANATION :-
# The `questions` tuple holds fixed quiz questions, making it ideal for read-only use. `options` is a 2D tuple where each sub-tuple
# contains four answer choices (A–B-C-D) for each question—again using a tuple since the data doesn't change. `answers` is another
# fixed tuple storing the correct options. On the other hand, `guesses` is a list because it collects user input dynamically using
# `.append()` as the quiz runs. `score` is initialized to 0, and `question_num` tracks the current question. A `for` loop iterates
# through each question, prints it with its options, & collects the user’s input in uppercase. The input is compared to the correct
# answer; if correct, score increases by 1, otherwise the correct answer is shown. After all questions, the program prints both the
# correct answers and user guesses, then calculates and displays the final score as a percentage.

questions = ("Who invented the Periodic Table?: ",
             "Which planet is known as the Morning Star?: ",
             "Which of these is a version control system?: ",
             "The Starry Night was created by which artist?: ",
             "When did Lionel Messi win his 1st Ballond'Or?: ")

options = (("A. Antoine Lavoisier", "B. John Dalton", "C. Dmitri Mendeleev", "D. Marie Curie"),
           ("A. Mars", "B. Venus", "C. Saturn", "D. Mercury"),
           ("A. Git", "B. SQL", "C. CSS", "D. HTML"),
           ("A. Pablo Picasso", "B. Leonardo da Vinci", "C. Claude Monet", "D. Vincent van Gogh"),
           ("A. 2005", "B. 2007", "C. 2009", "D. 2011"),)

answers = ("C", "B", "A", "D", "C")
guesses = []
score = int()  # Initializes score to 0, because calling int() with no arguments returns 0 by default in python
question_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------------------------------")
print("                   RESULTS                   ")
print("---------------------------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
