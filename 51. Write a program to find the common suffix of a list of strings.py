def common_suffix(string):
    if not string:
        return "" 
    
    reversed_string=[s[::-1]for s in string]

    common_reversed_prefix=reversed_string[0]

    for s in reversed_string[1:]:
        while not s.startswith(common_reversed_prefix):
            common_reversed_prefix=common_reversed_prefix[:-1]
            if not common_reversed_prefix:
                return "" 
            
    common_suffix=common_reversed_prefix[::-1]

    return common_suffix


string=["baking","king","walking"]

print("common suffix: ",common_suffix(string))