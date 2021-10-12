from vignere import vignere_decrypt, vignere_encrypt
import random
import string

CHARS = string.ascii_lowercase + string.ascii_uppercase + "., -*\t\n"


def test_vignere_encrypt() -> None:
    assert vignere_encrypt("TO BE OR NOT TO BE THAT IS THE QUESTION",
                           "RELATIONS") == "KS ME HZ BBL KS ME MPOG AJ XSE JCSFLZSY"


def test_vignere_decrypt() -> None:
    assert vignere_decrypt(
        "KS ME HZ BBL KS ME MPOG AJ XSE JCSFLZSY", "RELATIONS") == "TO BE OR NOT TO BE THAT IS THE QUESTION"


def test_encrypt_and_decrypt() -> None:
    for _ in range(100):
        random_str = create_random_str(100)
        random_key = create_random_str(100)
        assert vignere_decrypt(vignere_encrypt(
            random_str, random_key), random_key) == random_str

def create_random_str(length: int) -> str:
    return "".join(random.choice(CHARS) for _ in range(length))
