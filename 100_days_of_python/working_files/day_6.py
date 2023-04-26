print("USER LOGIN")
username = input("Username > ")
password = input("Password > ")

if username == "phillydam" and password == "password": 
    print("Welcome administrator!")
elif username == "Drew" and password == "1234":
    print("secret names only!")
elif username == "Kara":
    print("how do you know about this?")
else:
    print("Access denied!!")