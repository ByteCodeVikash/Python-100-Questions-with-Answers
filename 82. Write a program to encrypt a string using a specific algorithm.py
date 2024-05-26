def caesar_cipher_encrypt(text,shift):
    result=""

    for char in text:
        if char.isupper():
            result+=chr((ord(char)+shift-65)%26+65)
        elif char.islower():
            result+=chr((ord(char)+shift-97)%26+97)
        else:
            result+=char
    return result

plain_text="Hello , world!"
shift=3
encrypted_text=caesar_cipher_encrypt(plain_text,shift)
print("Original Text: ",plain_text)
print("Encrypted Text: ",encrypted_text)


