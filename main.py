
import random
#generate random inital number
num = random.randrange(1000, 10000)
print(num)
#check if first guess is the same as initial number
firstInput = int(input("What is your first guess? "))
if (firstInput == num):
  print(" you are the mastermind on the first attempt")
else: 
  times = 0 
#check the correct digits
  while (firstInput != num):
    times += 1 
    count = 0
    num = str(num)
    firstInput = str(firstInput)
    correct = []
    for i in range (0,4):
      if(firstInput[i]==num[i]):
        count += 1
        correct.append(firstInput[i])
      else:
        continue
#the conditions after checking correct digits
    if (count < 4) and (count != 0):
      print("Not quite the number. But you did get ",
                count, " digit(s) correct!")
      print("Also these numbers in your input were correct.")
      for k in correct:
        print(k, end=' ')
      print('\n')
      firstInput = int(input("Enter your next choice of numbers: "))
    elif (count == 0):
      print("None of the numbers in your input match.")       
      firstInput = int(input("Enter your next choice of numbers: "))
  if firstInput == num:
      print("You are a Mastermind")
      print("It took you", times, "tries.")
        

