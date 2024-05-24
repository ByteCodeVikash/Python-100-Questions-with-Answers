import re
def is_valid_uuid(uuid_string):
    uuid_regex=re.compile(
        r'^[0-9a-fA-F]{8}-'
        r'[0-9a-fA-F]{4}-'
        r'[0-9a-fA-F]{4}-'
        r'[0-9a-fA-F]{4}-'
        r'[0-9a-fA-F]{12}$'
    )
    return bool(uuid_regex.match(uuid_string))

valid_uuid="123e4567-e89b-12d3-a456-426614174000"
invalid_uuid="123e4567-e89b-12d3-a456-42661417400Z"
another_invalid_uuid="123e4567e89b12d3a456426614174000"

print(valid_uuid,"is valid",is_valid_uuid(valid_uuid))
print(invalid_uuid,"is valid",is_valid_uuid(invalid_uuid))
print(another_invalid_uuid,"is valid",is_valid_uuid(another_invalid_uuid))