names_string = input("Give me everyone's names, separated by a comma. ")
names = names_string.split(", ")

#Choose who is going to buy a meal
import random
random_name = random.randint(0, len(names)-1)
print(f"{names[random_name]} is going to buy the meal today!")

#Another option - using choice function
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")
