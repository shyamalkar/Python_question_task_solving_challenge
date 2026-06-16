# Capstone Project: Interactive "Mad Libs" Story Generator
# step 1 : gather inoutes 

adjective = input("Enter an adjective:")

animal = input("Enter an animal: ")
place = input("Enter a place:")
hero_name = str(input("Enter a hero name:"))

# fevorite number and arithmetic 
fav_number = int(input("Enter your fevorite number:"))
magic_number = fav_number * 3 

# Draft and output the story 

story  = f"""
One day , the {adjective} {animal} appeared in {place}.
Everyone was scared untill the brave hero, {hero_name}, arrived.

using the magical number {magic_number}, {hero_name} defeated the {animal} and saved {place}.
 
from that day on, the people of {place}
celebrated the legendary {hero_name} and the amazing {adjective} adventure !
"""

print("\n ======= MAD LIBS STORY ====== ")

print(story)