import random
import time

# Prompt1
print ("Welcome to Multiplication Game.")
print ("You will be prompted to solve a math eqution")
print ("And You will need to answer within 3 seconds.")

ready = input("Are you ready to play? (y/n): ").lower()
score = 0

while (ready == 'y' or ready == 'yes'):

  # Prompt3
  num1 = random.randint(0,12)
  num2 = random.randint(0,12)

  for x in range(3):
    print(3 - x)
    time.sleep(0.5)

  # Prompt4
  t1 = time.time()
  question = int(input("\n\n\n" + str(num1) + " x " + str(num2) + " = "))
  # Prompt5
  t2 = time.time()

  print ("\n\n\nYou took " + str(t2 - t1))

  # Prompt6
  if (question == num1 * num2 and t2 - t1 < 3):
    print ("You got it")
    score += 1
  else:
    print ("You failed")

  print ("Score: " + str(score))
  # Prompt2 + 6
  ready = input("Are you ready to play? (y/n): ").lower()

print("Take your time and prepare.")
print ("Total score: " + str(score))