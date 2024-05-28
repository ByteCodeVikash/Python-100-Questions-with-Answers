import base64

base64_string="SGVsbG8gd29ybGQ="

base64_bytes=base64_string.encode('utf-8')

original_bytes=base64.b64decode(base64_bytes)

origianl_string=original_bytes.decode('utf-8')


print("Original Base64 string:-",base64_string)
print("original string:-",origianl_string)