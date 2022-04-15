"""CISC 320 - Programming Assignment 2 - Scott Fones."""

import sys
from pathlib import Path


def backtrack_word_search(
    word_dict: dict[int, list[str]],
    word_chain: list[str],
    user_list: list[str],
    user_index: int,
    results: list[str],
) -> list[str]:
    """Perform backtracking search through the dictionary to find valid decryptions."""
    results = []
    for word in word_dict[len(user_list[user_index])]:
        if user_index + 1 == len(user_list):
            encoded = " ".join(user_list)
            decoded = " ".join(word_chain + [word])

            if is_good_cipher(decoded, encoded):
                results.append(decoded)
        else:
            results.extend(
                backtrack_word_search(
                    word_dict,
                    word_chain + [word],
                    user_list,
                    user_index + 1,
                    results,
                )
            )
    return results


def build_dict() -> dict[int, list[str]]:
    """Build a map of wordlength to list of words from a dictionary file."""
    word_dict: dict[int, list[str]] = {}

    dict_file = Path("dictionary.txt")

    if not dict_file.exists():
        print("Error: File dictionary.txt not found.")
        sys.exit(1)

    with open("dictionary.txt", "r") as f:
        for line in f:
            word = line.strip()
            word_len = len(word)
            if word_len not in word_dict:
                word_dict[word_len] = []
            word_dict[word_len].append(word)
    return word_dict


def is_good_cipher(decoded: str, encoded: str) -> bool:
    """Check if the decoded string is valid.

    Create a map for each indexed position. A valid decoding must be a one-to-one mapping.
    """
    cipher_map: dict[str, str] = {}
    for (enc, dec) in zip(encoded, decoded):
        if enc not in cipher_map:
            cipher_map[enc] = dec
        elif cipher_map[enc] != dec:
            return False
    if len(set(decoded)) != len(set(encoded)):
        return False
    return True


def main():
    """Initialize the program."""
    word_dict = build_dict()
    user_list = sys.argv[1:]
    results = backtrack_word_search(word_dict, [], user_list, 0, [])
    print(len(results))
    for res in results:
        print(res)


if __name__ == "__main__":
    sys.exit(main())
