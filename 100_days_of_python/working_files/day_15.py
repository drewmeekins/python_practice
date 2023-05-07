# while loops
# numbers
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1

# text
# exit = ""
# while exit != "yes":
#     print("😂")
#     exit = input("Exit?: ")

# kids game
# Ask kids what animal they want and print out that sound
animal = ""
exit = ""
while exit != "yes":
    animal = input("What animal do you like?: ")
    if animal == "Dog":
        print("Bark!")
    elif animal == "Cat":
        print("Meow")
    elif animal == "Cow":
        print("Moo")
    elif animal == "Bird":
        print("Chirp")
    else:
        print("I don't know what that is.")
    exit = input("Exit?: ")
