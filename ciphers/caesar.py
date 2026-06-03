def encrypt(text: str, shift: int) -> str:
    encrypted = ""

    for character in text:
        if character.isalpha():
            if character.islower():
                new_char = (ord(character) - ord('a') + shift) % 26
                new_char = chr(new_char + ord('a'))
            else:
                new_char = (ord(character) - ord('A') + shift) % 26
                new_char = chr(new_char + ord('A'))

            encrypted += new_char
        else:
            encrypted += character

    return encrypted

def decrypt(text: str, shift: int) -> str:
    decrypted = ""
    
    for character in text:
        if character.isalpha():
            if character.islower():
                new_char = (ord(character) - ord('a') - shift) % 26
                new_char = chr(new_char + ord('a'))
            else:
                new_char = (ord(character) - ord('A') - shift) % 26
                new_char = chr(new_char + ord('A'))

            decrypted += new_char
        else:
            decrypted += character

    return decrypted
