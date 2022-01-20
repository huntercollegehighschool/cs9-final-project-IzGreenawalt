print ("The First Day of School")
questions = ['noun', 'adjective','number', 'adjective','noun',"proper noun",'proper noun','plural noun',"ing verb.", "plural noun", "adjective","adverb"]
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
aan1=vowelcheck(answers[1])

story= (' One very nice morning near the end of summer, my mother woke me up at 4:00 A.M. and said, "Wake up and smell the grass, sleepy head! Today is your first day of school and you cant be late." I groaned in my bed for twenty seconds, but eventually I got dressed. I wore a blue and white striped, long sleeve '+answers[0]+' with a collar on it, a red tie, dark gray pants, white socks, black shoes, and '+aan1+ ' '+answers[1]+' hat. In ten minutes I made lunch and ate my breakfast. '+answers[2]+'minutes later, the bus came. A few minutes later, I was at school. In school, I met two really '+answers[3]+' kids. All of us became friends very fast. That day we had Science, and luckily my friends and I were at the same'+answers[4]+ 'My friends names are' + answers[5]+ 'and' +answers[6]+ '. In Math we werent together, and that really bugged me. We learned what' +answers[7]+' were, and when to use them. At snack and recess, we played a game together. It was extremely fun. At P. E., we were' +answers[8]+ 'off of the ropes onto' +answers[9] + 'I thought it was a very' +answers[10] + 'idea. In swimming class, we needed to swim extremely' +answers[11]+ ', or else we would have to swim longer. Before I knew it, school was over. I grabbed all my belongings and put them into my backpack. In two minutes, the bus came. As I stepped into the bus I shouted, "Goodbye, adios amigos, and shalom," to my friends. Then I went into the bus. In a flash, I was back home. This day was an extremely exciting day!')
print(story) 


