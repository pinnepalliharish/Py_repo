from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for k in question_data:
    new_q=Question(k["question"],k["correct_answer"])
    question_bank.append(new_q)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

quiz.game_is_over()
