from datetime import datetime

def valid_time(t):

    try:
        datetime.strptime(t,'%H-%M-%S')
        return True
    except ValueError:
        return False
    
test_time=['23-32-32','23-3','32-32-32']

for i in test_time:
    print(i,'is valid',valid_time(i))
