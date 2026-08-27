import random, string


def gen_uuid(len: int = 10):
    _str = ''.join(random.choice(string.ascii_letters) for _ in range(len))
    return _str
