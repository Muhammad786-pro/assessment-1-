bio = {"name": "Muhammad Adil Imran", "hometown": "Ajman", "age": 16}
print(f"Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")

# asking user for input

name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# determining if age is an integer

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Sorry, enter a numeric value.")

bio = {"name": "Muhammad Adil Imran", "hometown": "Ajman", "age": 16}
print(f"Name: {bio['name']}\nHometown: {bio['hometown']}\nAge: {bio['age']}")


