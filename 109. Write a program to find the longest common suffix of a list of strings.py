def longest_common_suffix(strs):
    if not strs:
        return ""
    
    # Reverse the strings to find the common prefix in reversed order
    reversed_strs = [s[::-1] for s in strs]
    
    # Start with the first reversed string as the suffix
    suffix = reversed_strs[0]
    
    # Compare the suffix with each reversed string in the list
    for string in reversed_strs[1:]:
        # Reduce the suffix length until it matches the start of the string
        while string[:len(suffix)] != suffix and suffix:
            suffix = suffix[:-1]
        
        # If there's no common suffix, return an empty string
        if not suffix:
            return ""
    
    # Reverse the result back to get the common suffix
    return suffix[::-1]

# Test cases
test_lists = [
    ["running", "jogging", "sprinting"],
    ["baking", "cooking", "looking"],
    ["interstellar", "stellar", "cellar"],
    ["suffix", "affix", "fix"],
    ["apple", "maple", "people"]
]

for strs in test_lists:
    print(f"List: {strs} -> Longest Common Suffix: '{longest_common_suffix(strs)}'")
