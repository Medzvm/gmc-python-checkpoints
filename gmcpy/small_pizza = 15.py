print("Welcome to Python Pizza Deliveries")
print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25")
user=input("what is the pizza sie you want(S OR M OR L)?")
price=0
while user not in ["s","m","l"]:
    user=input("what is the pizza sie you want(S OR M OR L)?")

if user.upper()=="S":
    price=price+15
elif user.upper() == "M":
    price=price+20
elif user.upper()=="L":
    price=price+25

print("Pepperoni for Small Pizza: $2+\n Pepperoni for Medium Pizza: $3+\n Pepperoni for Large Pizza: $3+")

pepperoni=input("did you want to add Pepperoni ? answer withyes/no : ")
while pepperoni not in ["yes","no"]:
    pepperoni=input("did you want to add Pepperoni ? answer withyes/no : ")
if pepperoni=="yes" and user.upper()=="S":
    price=price+2
elif pepperoni=="yes" and (user.upper()=="M" or user.upper()=="L"):
    price=price+3

cheese =input("Extra cheese for any size pizza: + $1 did you want to add it ? answer with yes/no : ")
while cheese not in ["yes","no"]:
    cheese =input("Extra cheese for any size pizza: + $1 did you want to add it ? answer with yes/no : ")
if cheese.upper()=="yes":
    price=price+1

print(f"Your final bill is: ${price}")

