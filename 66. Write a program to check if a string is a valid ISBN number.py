def is_valid_isbn_10(isbn):
    if len(isbn) !=10:
        return False
    
    totel=0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        
        total+=int(isbn[i])*(10-1)


    checksum=isbn[9]
    if checksum=='x':
        total+=10

    elif checksum.isdigit():
        total+=int(checksum)

    else:
        return False

    return total % 11==0


def is_valid_isbn_13(isbn):
    if len(isbn) !=13:
        return False
    
    total =0
    for i in range(12):
        if not isbn[i].isdigit():
            return False
        digit=int(isbn[i])
        if i % 2==0:
            total+=digit*3

    checksum=isbn[12]
    if not checksum.isdigit():
        return False
    total+=int((checksum)) 

    return total %10==0

def is_valid_isbn(isbn):
    if len(isbn)==10:
        return is_valid_isbn_10(isbn)
    elif len(isbn)==13:
        return is_valid_isbn_13(isbn)
    else:
        return False

isbn_10='09785454688'
isbn_13='132434657898000000'
invalid_isbn='6e5rytfuygk90886564' 

print(isbn_10,"is valid",is_valid_isbn(isbn_10))
print(isbn_13,"is valid",is_valid_isbn(isbn_13))
print(invalid_isbn,"is valid",is_valid_isbn(invalid_isbn))