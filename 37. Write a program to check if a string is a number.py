def is_number(input_string):
    try:
        # Try to convert the string to a float
        float(input_string)
        return True
    except ValueError:
        # If an error occurs, it is not a number
        return False

# Example usage
input_str1 = "123.45"
input_str2 = "Hello123"
print(f"Is '{input_str1}' a number? {is_number(input_str1)}")
print(f"Is '{input_str2}' a number? {is_number(input_str2)}")
