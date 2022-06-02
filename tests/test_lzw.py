import pytest

from src.lzw import encode, decode


def test_compress():
    to_compress = "aaaaaaalalalalalalaeksandar"

    try:
        encoded = encode(to_compress)
    except Exception as e:
        pytest.fail(f"Error while encoding: {e}")

    assert len(encoded) <= len(to_compress)


def test_decompress():
    to_compress = "aaaaaaalalalalalalaeksandar"

    try:
        decoded = decode(encode(to_compress))
    except Exception as e:
        pytest.fail(f"Error while decoding: {e}")

    assert decoded == to_compress


def test_unique_chars():
    to_compress = "abcdefghijklmnopqrstuvwxyz"

    try:
        encoded = encode(to_compress)
    except Exception as e:
        pytest.fail(f"Error while encoding: {e}")

    assert len(encoded) == len(to_compress)
