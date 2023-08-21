def gcd_two_numbers(a: int, b: int)->int:
    """
    Calculate GCD of two positive integers using the Euclidean Algorithm.
    """
    pass

def gcd_numbers(numbers: list[int])->int:
    """
    Calculate GCD of a list of positive integers.
    Uses the gcd_two_numbers function.
    """
    pass

def get_numbers()->list[int]:
    """
    Read a list of positive integers from the user, validate the inputs, and return the list.
    """
    while True:
        try:
            input_str = input("Enter a list of positive integers separated by spaces: ")
            input_numbers = [int(x) for x in input_str.split()]
            
            if any(num <= 0 for num in input_numbers):
                raise ValueError("All numbers must be positive integers")
            
            return input_numbers
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    numbers = get_numbers()
    print("your input list: ",numbers)

if __name__ == "__main__":
    main()
