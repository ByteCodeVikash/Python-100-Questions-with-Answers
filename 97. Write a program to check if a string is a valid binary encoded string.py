import re

def hex_to_string(hex_string):

    byte_string=bytes.fromhex(hex_string)

    original_string=byte_string.decode('utf-8')

    return original_string

hex_encoded_string="48656c6c6f20776f726c64"
decoded_string=hex_to_string(hex_encoded_string)

print("Hexadecimal encoded string:",hex_encoded_string)
print("Decoded original string:",decoded_string)