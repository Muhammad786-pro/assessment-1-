answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
else:
    print("Incorrect!")


# quiz (multiple questions)
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "Belgium": "Brussels",
    "Netherlands": "Amsterdam",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Norway": "Oslo",
    
}

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {capital}.")
