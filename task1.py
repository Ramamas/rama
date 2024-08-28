def is_palindrome(s):
    # Normalize the string to lower case
    s = s.lower()
    
    # Check if the string is a palindrome
    is_palindrome = s == s[::-1]
    
    # Count the frequency of each character using dictionary comprehension
    frequency = {char: s.count(char) for char in s}
    
    return is_palindrome, frequency

# Example usage
print(is_palindrome("radar"))  # Output: (True, {'r': 2, 'a': 2, 'd': 1})

import math

def is_prime(n):
    if n < 2:
        return [(True, 1)]
    return [(n % i == 0, i) for i in range(2, int(math.sqrt(n)) + 1)]

# Example usage
print(is_prime(11))  # Output: [(False, 2), (False, 3)]

def main_program():
    results = []
    errors = []
    
    for _ in range(3):  # Retry mechanism for up to 3 attempts
        try:
            user_string = input("Enter a string to check if it's a palindrome: ")
            palindrome_result = is_palindrome(user_string)
            
            user_number = int(input("Enter a number to check if it's prime: "))
            prime_result = is_prime(user_number)
            
            results.append({
                'input_string': user_string,
                'palindrome_result': palindrome_result,
                'input_number': user_number,
                'prime_result': prime_result
            })
            break  # Exit loop if successful
        except ValueError as ve:
            errors.append((user_number, str(ve)))
            print(f"Invalid input. Please try again. {3 - len(errors)} attempts left.")
    
    print("Results:", results)
    print("Errors:", errors)


main_program()