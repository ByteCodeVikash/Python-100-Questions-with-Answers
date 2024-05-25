import json

def check_json(string):
    try:
        json.loads(string)
        return True
    except ValueError:
        return False

string='{"name":"Vikash","age":24}'

if check_json(string):
    print("the string is json")
else:
    print("the string is not valid string")    