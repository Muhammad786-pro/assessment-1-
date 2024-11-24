names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
if "Sam" in names:
    print("'Sam' found!")
else:
    print("'Sam' not found.")

# asking for user input
search_name = input("Enter the name to search for: ")
if search_name in names:
    print(f"'{search_name}' found!")
else:
    print(f"'{search_name}' not found.")
