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

print("Ok, let's play")

answer = input("What is spider-man's real name?   \nA.)Peter Porker   \nB.)Peter Parker   \nC.)Tony Stark   \nD.)Steve   \nAnswer Here: ")
answer = textclean(answer)
if answer != "B":
  print('Incorrect!')
else:
  print('Correct!')
  correct_score += 1

answer = input("Is Iron Man rich or poor?   \nA.)Rich   \nB.)Poor  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Was Captian America ever an Avenger? \nA.)No   \nB.)Defnitely Not   \nC.)Maybe   \nD.)Yes   \nAnswer Here: ")
answer = textclean(answer)
if answer == "D":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Is Thor from Asgard or Earth? \nA.)Asgard  \nB.)Earth  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Can any other avenger lift Thor's hammer? \nA.)No   \nB.)Yes  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Who fixed Ultron? \nA.)Spider Man  \nB.)Tony Stark   \nC.)Einstein  \nD.)Brianna Caza   \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("In Spider-Man Homecoming, is Spider Man in High School, College, Middle School, or none? \nA.)High School   \nB.)College   \nC.)None   \nD.)Middle School   \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')
  
answer = input("In Civil War, who's team does Spider Man join? \nA.)Aunt May   \nB.)Hulk  \nC.)Iron Man   \nD.)Captain America   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Does Hawkeye have children? \nA.)Yes  \nB.)No  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("How long was Captain America frozen for? \nA.)12 years   \nB.)4 years  \nC.)300 years   \nD.)66 years   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Who is Thor's brother? \nA.)Captain America   \nB.)Captain Marvel  \nC.)Loki   \nD.)Odin   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("What is Hulk's real name? \nA.)Bruce Banter   \nB.)Bruce Baner   \nC.)Bruce Banner   \nD.)Bruce Bannner   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("What color is Hulk's skin? \nA.)Green   \nB.)Purple   \nC.)Blue   \nD.)Rainbow  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Does Captain America approve of curse words? \nA.)No  \nB.)Yes   \nc.)Sometimes  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("How many Infinity Stones are there? \nA.)4   \nB.)5  \nC.)3   \nD.)6  \nAnswer Here: ")
answer = textclean(answer)
if answer == "D":
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