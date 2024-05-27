import base64
import re

def is_base64(s):
    if len(s)%4!=0:
        return False
    
    base64_regex=re.compile(r'^[A-Za-z0-9+/]*={0,2}$')
    if not base64_regex.match(s):
        return False
    try:
        base64.b64decode(s,validate=True)
        return True
    except Exception:
        return False
    

test_string_1 = "SGVsbG8gV29ybGQh"  # "Hello World!" in Base64
test_string_2 = "SGVsbG8gV29ybGQh=="  # Valid Base64 with padding
test_string_3 = "NotBase64=="

print(is_base64(test_string_1))
print(is_base64(test_string_2))
print(is_base64(test_string_3))