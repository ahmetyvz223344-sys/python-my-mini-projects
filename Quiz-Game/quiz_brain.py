class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(f"Q.{self.question_number}:{current_question.text} (True/False):").lower()
        self.check_answer(choice, current_question.answer)

    def check_answer(self, choice, correct_answer):
        if choice.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("You got it wrong!")
            print(f"Correct answer: {correct_answer}")
            print("\n" * 2)



