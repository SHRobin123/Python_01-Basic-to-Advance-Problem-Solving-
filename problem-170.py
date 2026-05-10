#Online Quiz System

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):
        for q in self.questions:
            print(q.text)
            user_ans = input("Your Answer: ")

            if user_ans.lower() == q.answer.lower():
                self.score += 1

        print("Quiz Finished!")
        print("Your Score:", self.score)


# system create
q1 = Question("Capital of Bangladesh?", "Dhaka")
q2 = Question("5 + 5 = ?", "10")

quiz = Quiz()

quiz.add_question(q1)
quiz.add_question(q2)

quiz.start_quiz()

'''
output example:-

Capital of Bangladesh?
Your Answer: Dhaka
5 + 5 = ?
Your Answer: 10
Quiz Finished!
Your Score: 2
'''