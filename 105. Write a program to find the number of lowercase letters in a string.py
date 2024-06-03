def count_lowercase_letters(s):
    count = 0
    for char in s:
        if char.islower():
            count += 1
    return count

# Test cases
test_strings = [
    "Hello World!",
    "PYTHON",
    "python",
    "12345",
    "Hello, My Name Is GPT-4!",
    "uppercase AND lowercase"
]

for s in test_strings:
    print(f"'{s}': {count_lowercase_letters(s)} lowercase letters")
