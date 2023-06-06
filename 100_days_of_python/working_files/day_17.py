# Continue statement

# direction game
while True:
    print("You are a in a corridor, do you go left or right?")
    direction = input("Answer: ")
    if direction == "left":
        print("You've fallen to your death")
        break
    elif direction == "right":
        continue
        # takes us back to the beginning of loop
    else:
        print("Ahh! You're a genius, you've won!")
        exit()
print("Game over! You've failed")