def longest_substring_length(s):
    max_length=0
    start=0
    char_index_map={}

    for i ,char in enumerate(s):
        if char in char_index_map and char_index_map[char]>=start:
            start=char_index_map[char]+1



        char_index_map[char]=i

        max_length=max(max_length,i - start+1)

    return max_length

input_string="abcabcbb"
result=longest_substring_length(input_string)
print("the lenght of the lonest substring without repeating character in",result)        