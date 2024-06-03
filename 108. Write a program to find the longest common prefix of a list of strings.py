def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the prefix
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for string in strs[1:]:
        # Reduce the prefix length until it matches the start of the string
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        
        # If there's no common prefix, return an empty string
        if not prefix:
            return ""
    
    return prefix

# Test cases
test_lists = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["interstellar", "internet", "internal"],
    ["prefix", "preparation", "prelude"],
    ["apple", "ape", "april"]
]

for strs in test_lists:
    print(f"List: {strs} -> Longest Common Prefix: '{longest_common_prefix(strs)}'")
