def is_armstrong(num):
    # Count number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of cubes of each digit
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Example usage
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
