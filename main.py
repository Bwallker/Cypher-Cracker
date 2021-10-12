import time

def decrypt(cypher_text: str, key: int) -> str:
    message = ""
    for char in cypher_text:
        if char.isupper():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value - key - 65) % 26 + 65
            message += chr(new_ascii_value)
        elif char.islower():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value - key - 97) % 26 + 97
            message += chr(new_ascii_value)
        else:
            message += char
    return message

def encrypt(message: str, key: int) -> str:
    cypher_text = ""
    for char in message:
        if char.isupper():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value + key - 65) % 26 + 65
            cypher_text += chr(new_ascii_value)
        elif char.islower():
            ascii_value = ord(char)
            new_ascii_value = (ascii_value + key - 97) % 26 + 97
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
        if len(choice) > 1:
            print("Your choice should contain one character")
            print("Try again")
            print()
            continue

        if choice == "q":
            print("Quiting...")
            time.sleep(1)
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
