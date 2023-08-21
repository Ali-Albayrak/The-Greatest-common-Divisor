def gcd_two_numbers(a: int, b: int)->int:
    """
    Calculate GCD of two positive integers using the Euclidean Algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def gcd_numbers(numbers: list[int])->int:
    """
    Calculate GCD of a list of positive integers.
    Uses the gcd_two_numbers function.
    """
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to calculate GCD")
    
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd_two_numbers(result, num)
    
    return result

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
    print(f"your input: {numbers}")
    try:
        result = gcd_numbers(numbers)
        print(f"The Greatest Common Divisor of {numbers} is: {result}")
    except ValueError as e:
        print(f"Value Error: {e}.")
    

if __name__ == "__main__":
    main()
