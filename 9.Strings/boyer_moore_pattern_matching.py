"""
Roughly based on https://web.cs.ucdavis.edu/~gusfield/cs224f11/bnotes.pdf
"""

from typing import List
import string

ALPHABET = tuple(string.printable)


def find_prefixes(input_string: str) -> List[int]:
    """
    prepare a list of prefixes for an input string, output will be a list of the same length as the input string
    containing for every index i position a length of common prefix for substring [i, n] with an entire original
    string.
    :param input_string: string to prepare list of prefixes for
    :return:
    """
    prefixes_list = [0] * len(input_string)
    for i in range(len(input_string)):
        k = i
        j = 0
        while k < len(input_string):
            if input_string[k] != input_string[j]:
                break
            prefixes_list[i] += 1
            j += 1
            k += 1
    return prefixes_list


def prepare_good_suffix_heuristic_list(pattern: str) -> List[int]:
    """
    Computes a list of L'(i) values.
    :param pattern:
    :return:
    """
    m = len(pattern)
    good_suffix_list = [-1] * m
    right_to_left_prefixes = find_prefixes(pattern[::-1])
    reversed_prefixes = list(reversed(right_to_left_prefixes))
    for j in range(m - 1):
        i = m - reversed_prefixes[j]
        if i != m:
            good_suffix_list[i] = j
    return good_suffix_list


def prepare_bad_character_heuristic_table(pattern: str, alphabet: str = ALPHABET) -> List[List[int]]:
    """
    Computes a list of R(x) values.
    Discovers for each position i in pattern and for each character x in the alphabet, the position of
    the closest occurrence of x in pattern to the left of i. So when a mismatch occurs at position i of pattern and the
    mismatching character in text is x, we look up the (i, index_of(x)) entry in the array.
    :param pattern:
    :param alphabet:
    :return:
    """
    bad_character_table = [[-1] * len(alphabet) for _ in range(len(pattern))]
    support = [-1] * len(alphabet)
    charset = set()
    for i in range(len(pattern)):
        support[alphabet.index(pattern[i])] = i
        for ch in charset:
            ch_index = alphabet.index(ch)
            bad_character_table[i][ch_index] = support[ch_index]
        charset.add(pattern[i])
    return bad_character_table


def prepare_full_shift_list(pattern: str) -> List[int]:
    """
    Computes a list of l(x) values.
    :param pattern:
    :return:
    """
    full_shift_list = [0] * len(pattern)
    left_to_right_prefixes = find_prefixes(pattern)
    reversed_prefixes = list(reversed(left_to_right_prefixes))
    longest = 0
    for i in range(len(reversed_prefixes)):
        if reversed_prefixes[i] == i + 1:
            longest = max(reversed_prefixes[i], longest)
        full_shift_list[-i - 1] = longest
    return full_shift_list


def boyer_moore(text: str, pattern: str) -> List[int]:
    """
    Returns a list of integers corresponding to indices of pattern matches in the provided string
    :param text:
    :param pattern:
    :return:
    """
    matches = []

    lt = len(text)
    lp = len(pattern)

    if not text or not pattern or lt < lp:
        return matches

    bc = prepare_bad_character_heuristic_table(pattern)
    gs = prepare_good_suffix_heuristic_list(pattern)
    fs = prepare_full_shift_list(pattern)

    k = lp - 1

    while k < lt:
        i = lp - 1
        h = k
        while i >= 0 and text[h] == pattern[i]:
            i -= 1
            h -= 1

        if i == -1:
            matches.append(h + 1)
            k += lp
        else:
            char_shift = i - bc[i][ALPHABET.index(text[h])]
            if i == lp - 1:
                suffix_shift = 1
            elif gs[i + 1] == -1:
                suffix_shift = lp - fs[i + 1]
            else:
                suffix_shift = lp - gs[i + 1] - 1
            k += max(char_shift, suffix_shift)

    return matches
