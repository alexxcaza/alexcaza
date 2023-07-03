def textclean(message, LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "):
  message = message.upper()
  new = ''
  for char in message:
    if char in LETTERS:
      new += char
  return(new)
correct_score = 0
print('Welcome to the DC quiz!' )


playing = input('Do you want to play? ')
playing = textclean(playing)

if playing != "YES":
    quit()

print("Ok, let's play")

answer = input("What is Super Man's real name?   \nA.)Justin Rodgers   \nB.)Bruce Wayne   \nC.)Clark Kent   \nD.)Super Man is his real name   \nAnswer Here: ")
answer = textclean(answer)
if answer != "C":
  print('Incorrect!')
else:
  print('Correct!')
  correct_score += 1

answer = input("What happened to Batman's parents?   \nA.)They put him up for adoption   \nB.)They were robbed and killed   \nC.)Nothin happened \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("How did Flash get his powers? \nA.)He was born with them   \nB.)He is an alien   \nC.)A science expiriment gone wrong   \nD.)It is technology   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("What is Super Man's weakness? \nA.)He has none  \nB.)Kryptonite \nC.)Water \nD.)Aluminum  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Who raised Batman? \nA.)Nobody, he had to raise himself   \nB.)Alfred \nC.)Superman \nD.)His uncle  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Are there other's with powers like Green Lantern? \nA.)No  \nB.)Yes    \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Who fights Batman and ends up snapping and breaking his back? \nA.)Bane   \nB.)Joker   \nC.)Brianna Caza   \nD.)Lex Luthor   \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')
  
answer = input("Where does Superman work? \nA.)The Daily Bugle   \nB.)New York Times  \nC.)The Daily Bugle   \nD.)LAPD   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("How far can Darkseid teleport? \nA.)Throughout space and time  \nB.)Between planets \nC.)To other countries \nD.)Across cities  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Has anyone ever broken a Green Lantern ring? \nA.)No   \nB.)Yes     \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Why did Penguin become evil? \nA.)He was born into a family of crime   \nB.)He just felt like it  \nC.)He was bullied for being short and having a long nose   \nD.)His friend made him   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("What is the Riddler's birth name? \nA.)Bruce   \nB.)Liam   \nC.)Edward   \nD.)Brian   \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Who is Batman's arch-enemy? \nA.)Bane   \nB.)Joker   \nC.)Riddler   \nD.)Penguin  \nAnswer Here: ")
answer = textclean(answer)
if answer == "B":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Where did Batman train? \nA.)At a karate dojo in Gotham  \nB.)His parents taught him   \nc.)a monestery in the mountains \nD.)He looked up youtube videos \nAnswer Here: ")
answer = textclean(answer)
if answer == "C":
  print('Correct!')
  correct_score += 1
else:
  print('Incorrect!')

answer = input("Who did Robin become? \nA.)Jason Todd   \nB.)Joker  \nC.)Riddler   \nD.)He took on a regular life  \nAnswer Here: ")
answer = textclean(answer)
if answer == "A":
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