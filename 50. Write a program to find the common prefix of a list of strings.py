def common_prefix(string):
    if not string:
        return ""
    
    prefix=string[0]

    for s in string[1:]:
        while not s.startswith(prefix):
            prefix=prefix[:-1]

            if not prefix:
                return "" 
    return prefix  

string=["flower","flow","flight"]

print("common Prefix",common_prefix(string))