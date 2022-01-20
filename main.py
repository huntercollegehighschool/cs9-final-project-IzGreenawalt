"""
Name(s): Iz and Miles 
Name of Project:MadLibs
"""
import random
#Write the main part of your program here. Use of the other pages is optional.
print("Mad Libs!")
program=random.randint(1,4) 
if program==1:
  import Story1
elif program==2:
  import Story2
elif program==3:
  import Story3
elif program==4:
  import Story4
print (program)




