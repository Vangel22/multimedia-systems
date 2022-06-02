import pytest
from decimal import Decimal

from src.arithmetic import encode, decode


def test_compress():
    to_compress = "vangelelel"

    try:
        encoded, _ = encode(to_compress)
    except Exception as e:
        pytest.fail(f"Error while encoding: {e}")

    assert isinstance(encoded, Decimal)


def test_decompress():
    to_decompress = "vangelelel"

    try:
        encoded, encoded_len = encode(to_decompress)
    except Exception as e:
        pytest.fail(f"Error while encoding: {e}")

    decoded = decode(encoded, encoded_len)
    assert decoded == to_decompress


def test_unique_chars():
    to_compress = "abcdefghijklmnopqrstuvwxyz"

    try:
        encoded, _ = encode(to_compress)
    except Exception as e:
        pytest.fail(f"Error while encoding: {e}")

    assert isinstance(encoded, Decimal)
