#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.
print ("The Fun Park!")
questions = ['an adjective', 'a plural noun','a noun', 'an adverb','a number',"a past tense verb",'a superlative adjective','a past tense verb','an adverb','an adjective']
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

aan1=vowelcheck(answers[0])
aan2=vowelcheck(answers[9])


story=('Today, my fabulous camp group went to '+aan1+' '+answers[0]+' amusement park. It was a fun park with lots of cool '+answers[1]+" and enjoyable play structures. When we got there, my kind counselor shouted loudly, Everybody off the "+answers[2]+" We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary roller coaster I really liked so, I "+answers[3]+" ran over to get in the long line that had about "+answers[4]+" people in it. When I finally got on the roller coaster I was "+answers[5]+". In fact I was so nervous my two knees were knocking together. This was the "+answers[6]+" ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little "+answers[7]+" but I was proud of myself. The rest of the day went "+answers[8]+". It was "+aan2+" "+answers[9]+" day at the fun park.")
print(story)