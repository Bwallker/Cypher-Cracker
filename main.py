import typing

def decrypt(cypher_text: str, key: int) -> str:
    ASCII_VALUE_OF_CAPITAL_A = 65
    ASCII_VALUE_OF_LOWER_CASE_A = 97
    SIZE_OF_ALPHABET = 26
    message = ""
    for char in cypher_text:
        if char.isupper():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value - key - ASCII_VALUE_OF_CAPITAL_A) % SIZE_OF_ALPHABET + ASCII_VALUE_OF_CAPITAL_A
            message += chr(new_ascii_value)
        elif char.islower():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value - key - ASCII_VALUE_OF_LOWER_CASE_A) % SIZE_OF_ALPHABET + ASCII_VALUE_OF_LOWER_CASE_A
            message += chr(new_ascii_value)
        else:
            message += char
    return message


def encrypt(message: str, key: int) -> str:
    ASCII_VALUE_OF_CAPITAL_A = 65
    ASCII_VALUE_OF_LOWER_CASE_A = 97
    SIZE_OF_ALPHABET = 26
    cypher_text = ""
    for char in message:
        if char.isupper():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value + key - ASCII_VALUE_OF_CAPITAL_A) % SIZE_OF_ALPHABET + ASCII_VALUE_OF_CAPITAL_A
            cypher_text += chr(new_ascii_value)
        elif char.islower():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value + key - ASCII_VALUE_OF_LOWER_CASE_A) % SIZE_OF_ALPHABET + ASCII_VALUE_OF_LOWER_CASE_A
            cypher_text += chr(new_ascii_value)
        else:
            cypher_text += char
    return cypher_text


def break_shift_crypt(cypher_text: str) -> None:
    for i in range(26):
        print(decrypt(cypher_text, i+1))


def main() -> None:
    while True:
        print("What would you like to do?")
        print("e: encrypt, d: decrypt, q: quit, b: break")
        choice = input("> ")
        choice = choice.lower().strip()

        if choice == "q":
            print("Quiting...")
            input("Press enter to exit")
            break
        elif choice == "e":
            message = get_message()
            key = get_key()
            encrypted = encrypt(message, key)
            print("Encrypted message:")
            print(encrypted)
            print()
        elif choice == "d":
            message = get_cypher_text()
            key = get_key()
            decrypted = decrypt(message, key)
            print("Decrypted message:")
            print(decrypted)
            print()
        elif choice == "b":
            cypher_text = get_cypher_text()
            print("Here are all 26 decypherings")
            break_shift_crypt(cypher_text)
            print()
        else:
            print(f"Unknown command: {choice}")
            print("Try again.")
            print()
            continue


def get_cypher_text() -> str:
    print("What is your cypher text?")
    cypher_text = input("> ")
    print()
    return cypher_text


def get_message() -> str:
    print("What is your message?")
    message = input("> ")
    print()
    return message


def get_key() -> int:
    while True:
        try:
            print("What is your key?")
            key = int(input("> "))
            print()
            return key
        except ValueError:
            print("Key must be an integer")
            print("Try again.")
            print()


if __name__ == '__main__':
    main()

# Vignere solution
# Also encrypts lower case chars, which is arguably out of spec.
# let a and b = 2 arbitrary chars
# a keyed with b will have the same result as a keyed with upper(b) and a keyed with lower(b)

def next_char(string: str) -> typing.Generator:
    i = 0
    while True:
        try:
            yield string[i]
            i += 1
        except IndexError:
            yield string[0]
            i = 1
        
def vignere_encrypt(message: str, key: str) -> str:
    key = key.replace(' ', '')
    cypher_text = ""
    gen = next_char(key)
    
    for char in message:
        if not char.islower() and not char.isupper():
            cypher_text += char
            continue
        key_char_offset_from_a: int
        key_char: str = next(gen)
        if key_char.islower():
            key_char_offset_from_a = ord(key_char) - 97
        elif key_char.isupper():
            key_char_offset_from_a = ord(key_char) - 65
        else:
            cypher_text += char
            continue
        
        char_offset_from_a: int
        if char.islower():
            char_offset_from_a = ord(char) - 97
        else:
            char_offset_from_a = ord(char) - 65
        
        new_offset = (char_offset_from_a + key_char_offset_from_a) % 26
        
        if char.islower():
            new_char = chr(new_offset + 97)
        else:
            new_char = chr(new_offset + 65)
        
        cypher_text += new_char
    
    
    return cypher_text


def vignere_decrypt(cypher_text: str, key: str) -> str:
    key = key.replace(' ', '')
    gen = next_char(key)
    message = ""
    for char in cypher_text:
        if not char.islower() and not char.isupper():
            message += char
            continue
        key_char_offset_from_a: int
        key_char: str = next(gen)
        if key_char.islower():
            key_char_offset_from_a = ord(key_char) - 97
        elif key_char.isupper():
            key_char_offset_from_a = ord(key_char) - 65
        else:
            message += char
            continue

        char_offset_from_a: int
        if char.islower():
            char_offset_from_a = ord(char) - 97
        else:
            char_offset_from_a = ord(char) - 65

        new_offset = (char_offset_from_a - key_char_offset_from_a) % 26

        if char.islower():
            new_char = chr(new_offset + 97)
        else:
            new_char = chr(new_offset + 65)

        message += new_char

    return message
