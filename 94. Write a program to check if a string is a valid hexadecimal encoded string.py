import re

def is_valid_hexadecimal(s):
    hex_pattern=re.compile(r'^[0-9A-Fa-f]+$')

    if hex_pattern.match(s):
        return True
    else:
        return False
    

test_string=["1A3F", "GHIJ", "123abc", "789XYZ", "abcdef", "123456"]

for s in test_string:
    result=is_valid_hexadecimal(s)
    print(f"'{s}'is'{'a valid' if result else 'an invalid'}hexadeximal string.")