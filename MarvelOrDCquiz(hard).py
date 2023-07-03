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

answer = input("Is Vision from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer != "A":
  print('Incorrect!')
else:
  print('Correct!')
  correct_score += 1

answer = input("Is The Atom from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Is Red Tornado from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Urthona from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Cypher from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is The Creeper from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Frog Thor from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')
  

answer = input("Is Madcap from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Moondragon from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Plastic Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Black Canary from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Vixen from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Ka-Zar from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Machine Man from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')


answer = input("Is Darkseid from DC or Marvel?   \nA.)Marvel \nB.)DC  \nAnswer Here: ")
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