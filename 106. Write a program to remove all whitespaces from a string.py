def remove_whitespaces(s):
    return s.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")

# Test cases
test_strings = [
    "Hello World!",
    "  Python  ",
    "\tWhitespace\t",
    "New\nLine",
    "Multiple  Whitespaces",
    "  \t\nCombination\t \n "
]

for s in test_strings:
    print(f"Original: '{s}' -> Without whitespaces: '{remove_whitespaces(s)}'")
