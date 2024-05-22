def is_alphanumeric(an):
    return an.isalnum()


alphanumeric=["ab123","hello12","123hello"]

for alpha in alphanumeric:
    print(alpha,"is contain",is_alphanumeric(alpha))


