##########
# FILE: CodeBreaker.py
# WRITER: Tom Nahum, https://www.linkedin.com/in/tom-nachum/
# CONTACT: tom.nachum@gmail.com, +972-54-540-0958
# DESCRIPTION: This program helps Alice to solve the code!
##########

import string
import sys

OUT_OF_RANGE = "Index out of range."
SLASH_ID = -1


def convert_to_decimal(to_convert, in_base):
    """
    A function that translates a given number to decimal, according to a
    given base.
    :param to_convert: A string representing the number to conver to decimal.
    :param in_base: An int representing the base to convert by.
    :return: An int representing the decimal number after converstion.
    """
    to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13}
    number = 0
    for dig in range(len(to_convert)):
        cur_char = to_convert[len(to_convert) - dig - 1]
        if cur_char in to_num:
            cur_char = to_num[cur_char]
        number += int(cur_char) * (in_base ** dig)
    return number


def convert_pattern(p, base):
    """This function gets an array representing the pattern, and return an
    array of the converted pattern, according to the given base."""
    dec_p = []
    for num in p:
        if num == '/':
            dec_p.append(SLASH_ID)
        else:
            dec_p.append(convert_to_decimal(num, base))
    return dec_p


def print_decodes(text_str, pattern_str):
    """The main function of the program. for each base, the function
    translates the given pattern to decimal, and then multiply it by 1-4.
    Then searches the calculated indexes in the text and output the result."""
    for base in range(14, 17):
        print("\n###### Base:", base, "######")
        dec_pattern = convert_pattern(pattern_str, base)
        for mul in range(1, 5):
            attempts = "mul by " + str(mul) + ": "
            if max(dec_pattern) * mul < len(text_str):
                for char in dec_pattern:
                    if char == SLASH_ID:
                        attempts += '/'
                    else:
                        attempts += text_str[char * mul]
            else:
                attempts += OUT_OF_RANGE
            print(attempts)


if __name__ == '__main__':
    text = open(sys.argv[1], 'r')  # chapter 1 of "Alice in wonderland"
    parsed_text = text.read().translate({ord(c): None for c in string.whitespace})
    text.close()

    pattern = open(sys.argv[2], 'r')  # the code we need to decrypt
    parsed_pattern = pattern.read().split(',')
    pattern.close()

    print_decodes(parsed_text, parsed_pattern)
