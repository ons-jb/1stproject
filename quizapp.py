quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]
# Function to ask a question
def ask_question(question_data):
    print(question_data["question"])  # Display the question
    for i, option in enumerate(question_data["options"], 1):  # Loop through the options
        print(f"{i}. {option}")  # Print the options (1, 2, 3, 4)
    user_answer = input("Your answer (1-4): ")  # Ask the user for their answer
    return user_answer  # Return the user's answer

# Function to check if the answer is correct
def check_answer(user_answer, correct_answer, options):
    return options[int(user_answer) - 1] == correct_answer  # Check if user's choice is correct

# Main function to run the quiz
def run_quiz():
    score = 0  # Variable to track the user's score
    for question_data in quiz_data:  # Loop through each question in quiz_data
        user_answer = ask_question(question_data)  # Ask the question
        if check_answer(user_answer, question_data["answer"], question_data["options"]):  # Check the answer
            score += 1  # Increment the score if correct
            print("Correct!")
        else:
            print("Incorrect!")
    print(f"Your final score is {score}/{len(quiz_data)}")  # Display the final score

# Run the quiz
run_quiz()
