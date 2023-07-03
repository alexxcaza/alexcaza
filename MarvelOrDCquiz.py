def textclean(message, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "):
  message = message.upper()
  new = ''
  for char in message:
    if char in LETTERS:
      new += char
  return(new)
correct_score = 0
print('Welcome to the Marvel quiz!' )


playing = input('Do you want to play? ')
playing = textclean(playing)

if playing != "YES":
    quit()

print("Ok, let's play! In this game you will choose if a character is from the DC Universe or the Marvel Universe!")

answer = input("Is Aquaman from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer != "B":
  print('Incorrect!')
else:
  print('Correct!')
  correct_score += 1

answer = input("Is Black Panther from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Is Groot from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Blue Beetle from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Green Lantern from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Star Lord from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Thanos from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')
  

answer = input("Is Riddler from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Superman from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Spider Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Iron Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Scarlet Witch from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Captain America from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Joker from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Batman from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

print("You got " + str(correct_score) + " questions correct")
print("You got " + str(correct_score / 15 *100) + "%")
if correct_score >= 12:
  print("Amazing job! ")
if correct_score ==11 :
  print("Good job!")
if correct_score ==110 :
  print("Good job!")
if correct_score ==19 :
  print("Good job!")
if correct_score <= 8:
  print("It's ok, keep trying!")