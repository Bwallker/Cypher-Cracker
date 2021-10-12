from main import decrypt, encrypt
import string
import random
CHARS = string.ascii_lowercase + string.ascii_uppercase + "., -*\t\n"


def test_shift_encrypt() -> None:
    assert encrypt("my_test_str", 3) == "pb_whvw_vwu"
    assert encrypt("MY_TEST_STR", 3) == "PB_WHVW_VWU"
    assert encrypt("hubub", 7) == "obibi"
    assert encrypt("HUBUB", 7) == "OBIBI"


def test_shift_decrypt() -> None:
    assert decrypt("pb_whvw_vwu", 3) == "my_test_str"
    assert decrypt("PB_WHVW_VWU", 3) == "MY_TEST_STR"
    assert decrypt("obibi", 7) == "hubub"
    assert decrypt("OBIBI", 7) == "HUBUB"


def test_encrypt_and_decrypt() -> None:
    for _ in range(100):
        random_str = create_random_str(100)
        random_key = random.randint(1, 26)
        assert decrypt(encrypt(
            random_str, random_key), random_key) == random_str
    pass


def create_random_str(length: int) -> str:
    return "".join(random.choice(CHARS) for _ in range(length))
