import random 
Number= random.randint(1,100)
guesse = 5
for _ in range(guesse):
  Guess = int(input('input the guess'))
  if Guess>Number:
    print('go lower')
  elif Guess<Number:
    print('go higer')
  elif Guess == Number:
    print('how the F You got it bro')
    break
  else:
   print('you ran out of guesses')
  