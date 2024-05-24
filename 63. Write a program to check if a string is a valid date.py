from datetime import datetime

def date_valid(date):

    try:
        datetime.strptime(date,'%Y-%M-%d')
        return True
    except ValueError:
        return False
    
test_date=['2024-06-09','2024-05-04','2030-03-03'] 

for i in test_date:
    print(i,"is valid",date_valid(i))