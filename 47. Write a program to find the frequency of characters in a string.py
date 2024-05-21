def character_freq(s):
    freq_dict={}

    for char in s:
        freq_dict[char]=freq_dict.get(char,0)+1

    return freq_dict 

input_string="hello world"   

freq_map=character_freq(input_string)
print("character frequencies: ")

for char,freq in freq_map.items():

    print(f"'{char}': {freq}")