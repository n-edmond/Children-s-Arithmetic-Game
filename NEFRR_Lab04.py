#Nehesia Edmond
#Lab Week 4
#CS 101 L 001
#Due 13 September
import random
import operator
'''initilize the playAgain, and score'''
playAgain = 'y'


'''This part of the program aims to randomize the operators, randomize the numbers, and identify a solution. '''
while playAgain == 'y':
  score = 0
  for x in range(5):
    operations = {'+': operator.add, '-': operator.sub
    }
    x = random.randint(1,10)
    y = random.randint(1,10)
    sign = random.choice(list(operations.keys()))
    solution = operations.get(sign)(x,y)

    '''This portion of the program is aiming to initially ask the user the math problem'''

    mathQuestion = print('What is %d %s %d?'%(x,sign,y)) 

    '''The next portion loops to determine how many guesses a user has made and if the user answer provided is correct. Inform user if corret/incorrect'''  
    for guess in range(1,4):
      print('Guess #%d ==>' %guess)
      userAnswer = int(input())
      if guess == 3 and userAnswer !=solution:    
        print('The correct answer is %d not %d' %(solution,userAnswer))
        print()
      if userAnswer == solution:
        print('You are correct')
        score+=1
        print()
        break

  '''Offer results to user. Ask if they want to play agian. Loop if Y quit if N '''  
  percentage = (score/ 5) * 100
  print("You got %d out of 5." %score)
  print("That's",percentage,"%")
  playAgain = input('Do you want to play again? Y to continue, N to quit ==>')
  playAgain = playAgain.lower()

  '''Informs user that entry is invalid. Promts for answer again '''
  while playAgain != 'y' and playAgain !='n':
    print('Invalid entry')
    playAgain = input('Do you want to play again? Y to continue, N to quit ==>')
    playAgain = playAgain.lower()
    
  
