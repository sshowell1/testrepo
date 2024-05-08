print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        price = 7
        print(f"Your ticket price is ${price} dollars.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")
