# exam grade calc
# Name of exam
# Max score
# Your Score
# "You got a 79.00% wwhich is a B"

max_score = 100
your_score = float(input("What was your score?: "))

if your_score >= 90:
    print(f"You got {your_score}% which is an A")
elif your_score <= 89 and your_score >= 80:
    print(f"You got {your_score}% which is a B")
elif your_score <= 79 and your_score >= 70:
    print(f"You got {your_score}% which is a C")
elif your_score <= 69 and your_score >= 60:
    print(f"You got {your_score}% which is a D")
else:
    print("You failed")

