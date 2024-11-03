import json

# Function to load questions from a JSON file
def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Function to ask questions and get user answers
def ask_questions(questions):
    score = 0
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        answer = input("Your answer (1-4): ")
        
        if int(answer) - 1 == question['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question['options'][question['answer']]}\n")
    return score

# Function to evaluate the user's score and print the result
def evaluate_score(score, total_questions):
    percentage = (score / total_questions) * 100
    print(f"You scored {score} out of {total_questions} ({percentage:.2f}%)")
    
    if percentage >= 60:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry, you failed the quiz. Better luck next time!")

# Main function to run the quiz application
def main():
    questions = load_questions('questions.json')
    score = ask_questions(questions)
    evaluate_score(score, len(questions))

if __name__ == "__main__":
    main()