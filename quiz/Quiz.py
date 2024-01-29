# Quiz game where we will ask about 5 questions to the user and results will be displayed after the game is finished and we will say 'Hey ! you got _ out of 10'

points = 0

questions = [
    'What is the capital city of Nepal?',
    'Who is the founder of spaceX?',
    'Who owns Microsoft?',
    'What is the full name of Gautam Buddha?',
    'What is the height of Mt.Everest?',
    ]

answers = [
    'Kathmandu',
    'Elon Musk',
    'Bill Gates',
    'Siddartha Gautam',
    '8848 meters',
]

for i in range(len(questions)):
  user_input = input(f"{questions[i]}:").strip()

  if user_input.lower() == answers[i].lower():
     points = points + 1
  elif points > 0:
     points = points -1
  else:
     pass   
        
print(f"Hey you got {points} points out of total points !")   