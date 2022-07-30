from sha256 import sha256

modified_init_hash_table = [0xcbbb9d5d, 0x629a292a, 0x9159015a,
                            0x152fecd8, 0x67332667, 0x8eb44a87, 0xdb0c2e0d, 0x47b5481d]


def test_standard_sha256_Hello_World():
    assert sha256(
        'Hello World') == 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e'


def test_Hello_World():
    assert sha256(
        'Hello World', modified_init_hash_table) == 'a46c1943a4998dcba1b77e972f3a448a9807b98dc322d1202db41cd3308b7663'


def test_sentence():
    test_input = "When I find myself in times of troubles, Mother Mary comes to me, Speaking words of wisdom, Let it be."
    assert sha256(
        test_input, modified_init_hash_table) == 'f8986bbc315ee3fd0050a44ae7df5bcfe9f4318251295d8ca4714f588582860e'


def test_complex_command():
    assert sha256(
        'import hashlib;print(hashlib.sha256(input().encode()).hexdigest())', modified_init_hash_table) == '2c19865bdbd63947c3b234e34a8c245a10efde21aa55e1eae4d64d35a7bf3922'
