import random

name=input("What is your name")
print (name + "Marvin")

adjectives = ["Sneaky", "Brave", "Happy", "Mysterious", "Swift", "Witty"]
animals = ["Otter", "Tiger", "Panda", "Eagle", "Dolphin", "Fox"]

codename = random.choice(adjectives) + " " + random.choice(animals)
print ("Your code name is: " + codename)

lucky_number = random.randint(1, 100)
print ("Your lucky number is:", lucky_number)