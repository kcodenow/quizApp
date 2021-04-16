# question_data = [
# {"text": "A slug's blood is green.", "answer": "True"},
# {"text": "The loudest animal is the African Elephant.", "answer": "False"},
# {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
# {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
# {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
# {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
# {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
# {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
# {"text": "Google was originally called 'Backrub'.", "answer": "True"},
# {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
# {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
# {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

import requests
url = 'https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean'
response = requests.get(url).json()
question_data = response['results']
# https://opentdb.com/
# https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean
# question_data = [
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"Seoul is the capital of North Korea.","correct_answer":"False","incorrect_answers":["True"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"There are no roads in\/out of Juneau, Alaska.","correct_answer":"True","incorrect_answers":["False"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"The longest place named in the United States is Lake Chargoggagoggmanchauggagoggchaubunagungamaugg, located near Webster, MA.","correct_answer":"True","incorrect_answers":["False"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"The Southeast Asian island of Borneo is politically divided among 3 countries.","correct_answer":"True","incorrect_answers":["False"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"Vietnam is the only country in the world that starts with V. ","correct_answer":"False","incorrect_answers":["True"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"There exists an island named &quot;Java&quot;.","correct_answer":"True","incorrect_answers":["False"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"Antarctica is the largest desert in the world.","correct_answer":"True","incorrect_answers":["False"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"You could walk from Norway to North Korea while only passing through Russia.","correct_answer":"True","incorrect_answers":["False"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"Norway has a larger land area than Sweden.","correct_answer":"False","incorrect_answers":["True"]},
# 		{"category":"Geography","type":"boolean","difficulty":"medium","question":"The title of the 1969 film &quot;Krakatoa, East_of Java&quot; is incorrect, as Krakatoa is in fact west of Java.","correct_answer":"True","incorrect_answers":["False"]}
# 	]