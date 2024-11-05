# main.py

# Import custom libraries
from math_operations import add, subtract
from string_operations import reverse_string, capitalize_string

def main():
    # Using math_operations
    result_add = add(5, 3)
    result_subtract = subtract(10, 4)
    
    print(f"Addition result: {result_add}")
    print(f"Subtraction result: {result_subtract}")

    # Using string_operations
    original_string = "hello world"
    reversed_string = reverse_string(original_string)
    capitalized_string = capitalize_string(original_string)
    
    print(f"Reversed string: {reversed_string}")
    print(f"Capitalized string: {capitalized_string}")

if __name__ == "__main__":
    main()
