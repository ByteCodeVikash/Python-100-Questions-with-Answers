def remove_spaces(input_string):
    # Use the replace method to remove all spaces
    return input_string.replace(" ", "")

# Example usage
input_str = "This is a sample string."
output_str = remove_spaces(input_str)
print(f"Original string: '{input_str}'")
print(f"String without spaces: '{output_str}'")
