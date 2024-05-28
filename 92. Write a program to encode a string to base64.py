import base64

original_string="Hello world"

byte_string=original_string.encode('utf-8')

base64_byte=base64.b64encode(byte_string)

base64_string=base64_byte.decode('utf-8')

print("original string:-",original_string)
print("Base64 Encoded string:-",base64_string)