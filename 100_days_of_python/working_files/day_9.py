# my_score = int(input("Your score: "))

# if my_score > 100000:
#     print("Winner!")
# else:
#     print("Try again")

your_age = int(input("What is your birth year? "))

if your_age >= 1925 and your_age <= 1946:
    print("You're a traditionalist")
elif your_age >= 1947 and your_age <= 1964:
    print("You're a Boomer")
elif your_age >= 1965 and your_age <= 1981:
    print("You're a Gen Xer")
elif your_age >= 1982 and your_age <= 1995:
    print("You're a Millenial")
elif your_age >= 1996 and your_age <= 2023:
    print("You're a Gen Zer")
else:
    print("You're really old")
