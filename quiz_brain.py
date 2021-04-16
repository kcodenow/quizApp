class QuizBrain:
	def __init__(self, questions):
		self.question_number = 0
		self.questions = questions
		self.corrects = 0

	def still_has_questions(self):
		return self.question_number < len(self.questions)

	def next_question(self):
		current_q = self.questions[self.question_number]
		self.question_number+=1
		resp = input(f"Q.{self.question_number}. {current_q.text}\t (True/False)?\t")
		self.check_answer(current_q, resp)

	def check_answer(self, question, response):
		if(question.answer.lower() == response.lower()):
			self.corrects+=1
			print('Correct!')
		else:
			print('Wrong!')
		print(f'Current score:\t{self.corrects}/{self.question_number}.\n')
