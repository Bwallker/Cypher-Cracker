import typing
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
        key_char: str = gen.__next__()
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
        key_char: str = gen.__next__()
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
