#Use of this page is optional. If you use code here, make sure either import page2 or from page2 import * appear on your main.py page.

print("At the Arcade")
questions = ['plural noun', 'a plural noun','verb', 'noun','in verb',"plural noun",'noun','plural noun']
answers = [] # empty list
for item in questions:
 response = input("Please type in " + item + ": ")
 answers.append(response)

def vowelcheck(anword):
  if anword.startswith("a"):
    aan=("an")
  elif anword.startswith("e"):
    aan=("an")
  elif anword.startswith("i"):
    aan=("an")
  elif anword.startswith("o"):
    aan=("an")
  elif anword.startswith("u"):
   aan=("an")
  else:
    aan=("a")
  return aan

story=("When I go to the arcade with my "+answers[0]+" there are lots of games to play. I spend lots of time there with my friends. In the game X-Men you can be different "+answers[1]+". The point of the game is to "+answers[2]+" every robot. You also need to save people. Then you can go to the next level. In the game Star Wars you are Luke Skywalker and you try to destroy every "+answers[3]+". In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are "+answers[4]+" against. There are a whole lot of other cool games. When you play some games you win "+answers[5]+" for certain scores. Once you're done you can cash in your tickets to get a big "+answers[6]+". You can save your "+answers[7]+" for another time. When I went to this arcade I didn't believe how much fun it would be. So far I have had a lot of fun every time I've been to this great arcade! ")
print (story)

