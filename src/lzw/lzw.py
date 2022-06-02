from typing import List


def encode(data: str, bitcount: int = 8, dictionary_size: int = 256) -> List[int]:
    """Function to compress data using LZW algorithm

    :param data: Data to compress
    :type data: str
    :param bitcount: Number of bits used in the data encoding, defaults to 8
    :type bitcount: int, optional
    :param dictionary_size: Size of the dictionary, defaults to 256
    :type dictionary_size: int, optional
    :return: Compressed data, in a list of integers, each representing a code
    :rtype: List[int]
    """

    maximum_table_size = pow(2, int(bitcount))
    dictionary = {chr(i): i for i in range(dictionary_size)}
    string = ""
    compressed_data = []

    for symbol in data:
        string_plus_symbol = string + symbol
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if len(dictionary) <= maximum_table_size:
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    return compressed_data


def decode(
    compressed_data: List[int], bitcount: int = 8, dictionary_size: int = 256
) -> str:
    """Function to decompress data previously compressed using the LZW algorithm

    :param compressed_data: Compressed data (list of integers)
    :type compressed_data: List[int]
    :param bitcount: Number of bits used in the data encoding, defaults to 8
    :type bitcount: int, optional
    :param dictionary_size: Size of the dictionary, defaults to 256
    :type dictionary_size: int, optional
    :return: Decompressed data (original string)
    :rtype: str
    """

    next_code = pow(2, int(bitcount))
    decompressed_data, string = "", ""
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])

    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]

    return decompressed_data
