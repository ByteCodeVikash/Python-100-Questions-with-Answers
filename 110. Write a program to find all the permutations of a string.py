def generate_permutations(s):
    if len(s) == 0:
        return ['']
    
    permutations = []
    for i in range(len(s)):
        # Fix the current character
        fixed_char = s[i]
        
        # Generate permutations of the remaining characters
        remaining_chars = s[:i] + s[i+1:]
        remaining_permutations = generate_permutations(remaining_chars)
        
        # Append the fixed character to each permutation of the remaining characters
        for permutation in remaining_permutations:
            permutations.append(fixed_char + permutation)
    
    return permutations

# Test case
test_string = "abc"

print(f"All permutations of '{test_string}':")
for permutation in generate_permutations(test_string):
    print(permutation)
