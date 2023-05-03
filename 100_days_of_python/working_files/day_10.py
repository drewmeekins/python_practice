# addition = 5 + 5
# print(addition)

# subtraction = 5 - 3
# print(subtraction)

# multiplication = 5 * 5
# print(multiplication)

# division = 20 / 5
# print(division)

# squared =  5 ** 5
# print(squared)

# modulo = 30 % 4
# print(modulo)

# divisor = 15 // 4
# print(divisor)


my_bill = float(input("What was the bill?: "))
number_of_people = int(input("How many people at the table?: "))
answer = my_bill / number_of_people
answer = round(answer, 2)

print("You all owe", answer)

