  
#Use of this page is optional. If you use code here, make sure either import page3 or from page3 import * appear on your main.py page.

print("A Day At The Zoo!")

questions = ['an adjective', 'noun','past tense verb', 'adverb',' an adjective','noun','noun','adjective','verb','adverb','past tense verb','adjective']
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
#Here we created a function that checks for whether we should use a or an in the story, which allows for a more immersive experience.
print("Today I went to the zoo. I saw "+aan1+ " " +answers[0]+ " " + answers[1]+ " jumping up and down in its tree. He " + answers[2]+" " +answers[3] + " through the large tunnel that led to its " + answers[4]+" " + answers[5] + ". I got some peanuts and passed them through the cage to a gigantic gray " + answers[6] +" towering above my head. Feeding that animal made me hungry. I went to get a " + answers[7]+ " scoop of ice cream. It filled my stomach. Afterwards I had to " +answers[8] + " " +answers[9] + " to catch our bus. When I got home I " + answers[10] + " my mom for a " + answers[11]+ " day at the zoo.")

