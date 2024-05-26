def levenshtein_distance(str1,str2):
    len_str1=len(str1)
    len_str2=len(str2)

    dp=[[0 for x in range(len_str2+1)]for x in range(len_str1+1)]


    for i in range(len_str1+1):
        dp[i][0]=i
    for j in range(len_str2+1):
        dp[0][j]=j

    for i in range(1,len_str1+1):
        for j in range(1,len_str2+1):
            if str1[i-1]==str2[j-1]:
                cost=0
            else:
                cost=1

            dp[i][j]=min(dp[i-1][j]+1,
                         dp[i][j-1]+1,
                         dp[i-1][j-1]+cost)

    return dp[len_str1][len_str2]

str1="kitten"
str2="sitting"
print("Levenshtein Distance:",levenshtein_distance(str1,str2))                       