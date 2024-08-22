quiz_questions = {
    "What is the capital of India?": {
        "A": "Delhi",
        "B": "London",
        "C": "Berlin",
        "D": "Rome",
        "Answer": "A"
    },
    "What is sun?": {
        "A": "Earth",
        "B": "Star",
        "C": "Planet",
        "D": "Galaxy",
        "Answer": "B"
    },
    "What is the color of a banana?": {
        "A": "Yellow",
        "B": "Orange",
        "C": "Pink",
        "D": "Blue",
        "Answer": "A"
    }
}

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question, options in questions.items():
        print(question)
        for option, value in options.items():
            if option != "Answer":
                print(f"{option}: {value}")
        answer = input("Choose your answer (A, B, C, D): ")
        if answer.upper() == options["Answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {options['Answer']}.")
    print(f"\nQuiz finished! Your final score is {score} out of {len(questions)}.")

# Run the quiz
run_quiz(quiz_questions)