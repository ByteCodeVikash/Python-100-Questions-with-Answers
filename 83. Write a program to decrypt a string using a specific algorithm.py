def caesar_cipher_decrypt(text,shift):
    result=""


    for char in text:
        if char.isupper():
            result+=chr((ord(char)-shift-65)%26+65)
        elif char.islower():
            result+=chr((ord(char)-shift-97)%26+97)
        else:
            result+=char
    return result

encrypted_text="Khoor,Zruog!"
shift=3
decrypted_text=caesar_cipher_decrypt(encrypted_text,shift)
print("Encrypted Text:",encrypted_text)
print("Decrypted Text:",decrypted_text)                