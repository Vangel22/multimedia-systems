import string
from typing import Tuple
import decimal
from decimal import Decimal

decimal.getcontext().prec = 100


def encode(encode_str: str, precision: int = 3) -> Tuple[Decimal, int]:
    """Function to compress data using Arithmetic Coding algorithm

    :param encode_str: Data to compress
    :type encode_str: str
    :param precision: Encoding precision, defaults to 3
    :type precision: int, optional
    :return: Encoded data (arbitrary-precision fraction q) and length of the uncompressed data
    :rtype: Tuple[Decimal, int]
    """

    count = dict.fromkeys(string.ascii_lowercase, 1)
    cdf_range = dict.fromkeys(string.ascii_lowercase, 0)
    pdf = dict.fromkeys(string.ascii_lowercase, 0)
    alphabet_length = len(string.ascii_lowercase)

    low = 0
    high = Decimal(1) / Decimal(alphabet_length)

    for key, _ in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1) / Decimal(alphabet_length)

    for key, _ in sorted(pdf.items()):
        pdf[key] = Decimal(1) / Decimal(alphabet_length)

    i = alphabet_length

    lower_bound = 0
    upper_bound = 1

    u = 0

    for sym in encode_str:
        i += 1
        u += 1
        count[sym] += 1

        curr_range = upper_bound - lower_bound
        upper_bound = lower_bound + (curr_range * cdf_range[sym][1])
        lower_bound = lower_bound + (curr_range * cdf_range[sym][0])

        if u == precision:
            u = 0

            for key in sorted(pdf.keys()):
                pdf[key] = Decimal(count[key]) / Decimal(i)

            low = 0
            for key in sorted(cdf_range.keys()):
                high = pdf[key] + low
                cdf_range[key] = [low, high]
                low = high

    return lower_bound, len(encode_str)


def decode(compressed_data: Decimal, encoded_len: str, precision: int = 3) -> str:
    """Function to decompress data previously compressed using the Arithmetic Coding algorithm

    :param compressed_data: Compressed data
    :type compressed_data: Decimal
    :param encoded_len: Length of the uncompressed data
    :type encoded_len: str
    :param precision: Encoding precision, defaults to 3
    :type precision: int, optional
    :return: Decompressed data (original string)
    :rtype: str
    """

    decoded_str = ""
    alphabet_length = len(string.ascii_lowercase)
    count = dict.fromkeys(string.ascii_lowercase, 1)
    cdf_range = dict.fromkeys(string.ascii_lowercase, 0)
    pdf = dict.fromkeys(string.ascii_lowercase, 0)

    low = 0
    high = Decimal(1) / Decimal(alphabet_length)

    for key in sorted(cdf_range.keys()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1) / Decimal(alphabet_length)

    for key in sorted(pdf.keys()):
        pdf[key] = Decimal(1) / Decimal(alphabet_length)

    lower_bound = 0
    upper_bound = 1

    k = 0

    while encoded_len != len(decoded_str):
        for key in sorted(pdf.keys()):
            curr_range = upper_bound - lower_bound
            upper_cand = lower_bound + (curr_range * cdf_range[key][1])
            lower_cand = lower_bound + (curr_range * cdf_range[key][0])

            if lower_cand <= compressed_data < upper_cand:
                k += 1
                decoded_str += key

                if encoded_len == len(decoded_str):
                    break

                upper_bound = upper_cand
                lower_bound = lower_cand

                count[key] += 1

                if k == precision:
                    k = 0
                    for key in sorted(pdf.keys()):
                        pdf[key] = Decimal(count[key]) / Decimal(
                            alphabet_length + len(decoded_str)
                        )

                    low = 0
                    for key in sorted(cdf_range.keys()):
                        high = pdf[key] + low
                        cdf_range[key] = [low, high]
                        low = high

    return decoded_str
