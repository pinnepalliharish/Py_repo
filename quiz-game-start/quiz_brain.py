
class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
        current_q=self.question_list[self.question_number]
        self.question_number+=1
        option=input(f"Q.{self.question_number}..{current_q.text}..(true/false) : ")
        self.check_answer(option,current_q.answer)
    def check_answer(self,option,correct_answer):
        if option.lower()==correct_answer.lower():
            print("you are right!!")
            self.score+=1
        else:
            print("that's wrong :(")
        print("the correct answer is "+correct_answer)
        print(f"your sore is {self.score}/{self.question_number}\n")
    def game_is_over(self):
        print("your Quiz is Over" )
        print(f"your final score is {self.score}/{self.question_number}")