def binary_to_string(binary_string):

    byte_chunks=[binary_string[i:i+8] for i in range(0,len(binary_string),8)]

    byte_string=bytes(int(byte,2)for byte in byte_chunks)

    origainal_string=byte_string.decode('utf-8')

    return origainal_string

binary_encoded_string="0100100001100101011011000110110001101111001000000111011101101111011100100110110001100100"

decoded_string=binary_to_string(binary_encoded_string)

print("Binary encoded string",binary_encoded_string)
print("Decoded original string",decoded_string)