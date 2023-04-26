tv_show = input("What's your favorite TV show? ")

if tv_show == "The Wire":
    print("Good taste")
    fav_character = input("So who's your favorite character?")
    if fav_character == "Omar":
        print("Damn, RIP Omar")
    else:
        print("Eh, I guess")
elif tv_show == "The Sopranos":
    print("A GOAT show")
else:
    print("Get some help man!")