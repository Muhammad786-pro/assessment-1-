right_password = "12345"
password = ""
while password != right_password:
    password = input("Enter the password: ")
print("Access granted.")

# modification: 5 tries
right_password = "12345"
tries = 5
while tries > 0:
    password = input(f"Enter the password ({tries} tries left): ")
    if password == right_password:
        print("Access granted.")
        break
    tries -= 1
else:
    print("Maximum tries reached. Authorities have been alerted.")