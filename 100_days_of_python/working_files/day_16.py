# while true loops
# while True:
#     print("this program is running smoothly")
#     go_again = input("Go again?: ")
#     if go_again == "no":
#         break #breaks out of the loop
# print("Too bad, I was having fun")

# simple calculator
counter = 0
while True:
    answer = int(input("Enter a number: "))
    print("Adding up the numbers!")
    counter += answer
    print(f"Current total is, {counter}")
    add_another = input("Add another? (y/n): ")
    if add_another == "n":
        break
print(f"Your grand total is {counter}. Goodbye!")