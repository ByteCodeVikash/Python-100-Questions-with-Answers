def string_to_binary(s):

    byte_String=s.encode('utf-8')

    binray_string=''.join(format(byte,'08b')for byte in byte_String)

    return byte_String

original_String="Hello world"

binary_encoded_string=string_to_binary(original_String)

print("original string:",original_String)
print("Binary encoded string:",binary_encoded_string)