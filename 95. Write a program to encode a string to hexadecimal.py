def string_to_hex(s):

    byte_String=s.encode('utf-8')


    hex_string=byte_String.hex()

    return hex_string

original_String="Hello world"

hex_encoded_string=string_to_hex(original_String)

print("origianl string:-",original_String)

print("hexadecimal encoded string:-",hex_encoded_string)
