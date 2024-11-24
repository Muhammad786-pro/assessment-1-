def is_it_even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"

def main():
# asking user
        number = int(input("Enter a number: "))
        result = is_it_even_or_odd(number)
        print(f"The number {number} is {result}.")

main()
