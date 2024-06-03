def contains_pattern(s, pattern):
    return pattern in s

# Test cases
test_strings = [
    "Hello World!",
    "Python programming",
    "Regular expressions are powerful",
    "Check for a pattern",
    "Specific substring check"
]

pattern = "pattern"

for s in test_strings:
    print(f"'{s}' contains '{pattern}': {contains_pattern(s, pattern)}")
