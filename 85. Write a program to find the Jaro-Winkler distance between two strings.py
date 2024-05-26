def jaro_distance(s1, s2):
    if s1 == s2:
        return 1.0

    len_s1 = len(s1)
    len_s2 = len(s2)
    match_distance = max(len_s1, len_s2) // 2 - 1

    s1_matches = [False] * len_s1
    s2_matches = [False] * len_s2

    matches = 0
    transpositions = 0

    for i in range(len_s1):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_s2)
        for j in range(start, end):
            if s2_matches[j]:
                continue
            if s1[i] != s2[j]:
                continue
            s1_matches[i] = True
            s2_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    k = 0
    for i in range(len_s1):
        if not s1_matches[i]:
            continue
        while not s2_matches[k]:
            k += 1
        if s1[i] != s2[k]:
            transpositions += 1
        k += 1

    transpositions //= 2

    return (matches / len_s1 + matches / len_s2 + (matches - transpositions) / matches) / 3.0

def jaro_winkler_distance(s1, s2, p=0.1):
    jaro_dist = jaro_distance(s1, s2)

    prefix_length = 0
    max_prefix_length = 4
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix_length += 1
        else:
            break
        if prefix_length == max_prefix_length:
            break

    jaro_winkler_dist = jaro_dist + (prefix_length * p * (1 - jaro_dist))
    return jaro_winkler_dist

# Example usage
str1 = "MARTHA"
str2 = "MARHTA"
print("Jaro-Winkler Distance:", jaro_winkler_distance(str1, str2))
