import unittest
from io import StringIO
from unittest.mock import patch

# The functions to test
def check_answer(user_answer, correct_answer, options):
    return options[int(user_answer) - 1] == correct_answer

# Create the quiz_data structure for testing
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

# Test class for the quiz
class TestQuizApp(unittest.TestCase):
    
    # Test the check_answer function
    def test_check_answer_correct(self):
        result = check_answer("1", "Paris", ["Paris", "London", "Rome", "Berlin"])
        self.assertTrue(result)  # Expecting True because "Paris" is the correct answer
    
    def test_check_answer_incorrect(self):
        result = check_answer("2", "Paris", ["Paris", "London", "Rome", "Berlin"])
        self.assertFalse(result)  # Expecting False because "London" is not the correct answer
    
    # Test the quiz data structure (question, options, and correct answer)
    def test_quiz_data_structure(self):
        for question_data in quiz_data:
            self.assertIn("question", question_data)  # Ensure "question" exists
            self.assertIn("options", question_data)   # Ensure "options" exists
            self.assertIn("answer", question_data)    # Ensure "answer" exists
            self.assertIsInstance(question_data["options"], list)  # Ensure options is a list
            self.assertIsInstance(question_data["answer"], str)  # Ensure answer is a string
    
    # Test ask_question function (simulated user input)
    @patch("builtins.input", side_effect=["1", "2"])  # Mock user input
    @patch("sys.stdout", new_callable=StringIO)  # Capture printed output
    def test_ask_question(self, mock_stdout, mock_input):
        question_data = quiz_data[0]  # Use the first question
        # Simulate asking the question and getting user input
        gask_question(question_data)
        output = mock_stdout.getvalue()
        
        # Ensure that the output contains the question and the options
        self.assertIn(question_data["question"], output)
        for option in question_data["options"]:
            self.assertIn(option, output)

    # Additional test to check the final score calculation (optional)
    def test_final_score(self):
        score = 0
        for question_data in quiz_data:
            if check_answer("1", question_data["answer"], question_data["options"]):
                score += 1
        self.assertEqual(score, 2)  # Expecting score to be 2 because both answers are correct


# Run the tests
if __name__ == "__main__":
    unittest.main()

