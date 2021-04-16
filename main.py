from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests 

question_bank = []
# url = 'https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean'
# response = requests.get(url).json()
# question_data = response['results']

for q in question_data:
	newq = Question(q['question'], q['correct_answer'])
	question_bank.append(newq)

quiz_master = QuizBrain(question_bank)
while(quiz_master.still_has_questions()):
	quiz_master.next_question()
print(f'Quiz Complete!\nYour score was:\t{quiz_master.corrects}/{len(question_bank)}')