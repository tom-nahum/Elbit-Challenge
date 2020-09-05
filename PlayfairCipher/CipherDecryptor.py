##########
# FILE: CipherDecryptor.py
# WRITER: Tom Nahum, CS Student at the Hebrew University of Jerusalem
# DESCRIPTION: A program that decodes a text file using Playfair Cipher
# algorithm.
##########

import string
import sys

O_FILE_NAME = "decryption.txt"
TABLE_SIZE = 5


def generate_key(key):
    """
    This function generates the matrix which we decode by.
    :param key: A string representing the key of the matrix.
    """
    matrix = [['' for k in range(TABLE_SIZE)] for m in range(TABLE_SIZE)]
    col, row = 0, 0
    # fill matrix with given key:
    for letter in key:
        matrix[row][col] = letter
        col += 1
        if col == TABLE_SIZE:
            col = 0
            row += 1
    # fill matrix with left letters except 'j':
    for letter in range(ord('a'), ord('z') + 1):
        if (chr(letter) not in key) and (chr(letter) != 'j'):
            matrix[row][col] = chr(letter)
            col += 1
            if col == TABLE_SIZE:
                col = 0
                row += 1
    return matrix


# def print_table(table):
#     table_str = ""
#     for i in range(TABLE_SIZE):
#         for j in range(TABLE_SIZE):
#             table_str += table[i][j]
#             table_str += ' '
#         table_str += '\n'


def parse_data(data):
    """Gets a string, and returns a new string with no white spaces and
    lower case."""
    data_ns = data.translate({ord(c): None for c in string.whitespace})
    parsed_data = data_ns.lower()
    return parsed_data


def get_position(letter, key_square):
    """Gets a letter and returns it's location in the key matrix"""
    comp = letter
    if comp == 'j':
        comp = 'i'
    for i in range(TABLE_SIZE):
        for j in range(TABLE_SIZE):
            if key_square[i][j] == comp:
                return i, j


def decrypt_pair(l1, l2, key_square):
    """A helper function for decrypt. This function gets a pair of
    letters, and decrypt it according to Playfair Cipher algorithm."""
    r1, c1 = get_position(l1, key_square)
    r2, c2 = get_position(l2, key_square)
    if c1 == c2:  # if the letters in the same column:
        return key_square[r1 - 1][c1], key_square[r2 - 1][c2]
    elif r1 == r2:  # if the letters in the same row:
        return key_square[r1][c1 - 1], key_square[r2][c2 - 1]
    else:
        return key_square[r1][c2], key_square[r2][c1]


def decrypt(pairs_arr, key_square):
    """
    The main function of Playfair Cipher algorithm.
    :param pairs_arr: An array of pairs to translate.
    :param key_square: A matrix representing the grid in which we encrypt by.
    :return: A string representing the decrypted text.
    """
    decrypted_str = ""
    for pair in pairs_arr:
        x, y = decrypt_pair(pair[0], pair[1], key_square)
        decrypted_str += x + y
    return decrypted_str


def output_decryption(decryption):
    """Gets a string and output it's content to a file, according to the
    form of the given text. In order to output logical translation."""
    to_file = ""
    i, j = 0, 0
    while j < len(all_chars) and i < len(decryption):
        if all_chars[j] == ' ':
            to_file += ' '
            j += 1
        else:
            to_file += decryption[i]
            i += 1
            j += 1
    decrypted_file = open(O_FILE_NAME, "w+")
    decrypted_file.write(to_file)
    decrypted_file.close()


def split_to_pairs(data):
    """Gets a string and returns an array with pairs of letters from the
    string, by order."""
    return [(data[i:i + 1], data[i + 1:i + 2]) for i in
            range(0, len(data), 2)]


def file_to_chars(file):
    """Gets a file and returns an array of all the chars in the file."""
    chars = []
    for line in file:
        lower_line = line.lower()
        for c in lower_line:
            chars.append(c)
    return chars


if __name__ == '__main__':
    encrypted_file = open(sys.argv[1], 'r')  # Lyon's letter

    parsed_file = parse_data(encrypted_file.read())
    pairs = split_to_pairs(parsed_file)
    encrypted_file.seek(0, 0)
    all_chars = file_to_chars(encrypted_file)
    encrypted_file.close()

    given_key = parse_data(sys.argv[2])  # alice
    key_matrix = generate_key(given_key)

    decryption_str = decrypt(pairs, key_matrix)
    output_decryption(decryption_str)
