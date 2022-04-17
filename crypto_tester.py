"""CISC 320 - Programming Assignment 2 - Tester.

This program constructs random encodings to test cryptograph decryption.
"""

from pathlib import Path
from string import ascii_lowercase

import argparse
import random
import subprocess
import sys


def build_dict() -> dict[int, list[str]]:
    """Build a map of wordlength to list of words from a dictionary file."""
    dict_file = Path("dictionary.txt")
    if not dict_file.exists():
        print("Error: File dictionary.txt not found.")
        sys.exit(1)

    word_dict: dict[int, list[str]] = {}
    with open(dict_file, "r") as f:
        for line in f:
            word = line.strip()
            word_len = len(word)
            if word_len not in word_dict:
                word_dict[word_len] = []
            word_dict[word_len].append(word)
    return word_dict


def construct_cipher() -> dict[str, str]:
    """Construct a random cipher."""
    cipher = {}
    targets = list(ascii_lowercase)
    for c in list(ascii_lowercase):
        t = targets.pop(random.randrange(len(targets)))
        cipher[c] = t
    return cipher


def test_words(
    cipher: dict[str, str], word_count: int, word_dict: dict[int, list[str]]
) -> None:
    """Test a random string of given length."""
    decoded_list = []
    for _ in range(word_count):
        words: int = random.choice(list(word_dict.keys()))
        word = random.choice(word_dict[words])
        decoded_list.append(word)

    encoded_list = []
    for word in decoded_list:
        encoded = ""
        for c in word:
            encoded += cipher[c]
        encoded_list.append(encoded)

    decoded = " ".join(decoded_list)
    encoded = " ".join(encoded_list)
    print(f"Looking for: {decoded}, with: {encoded} , ", end="", flush=True)
    run_cap = subprocess.run(
        f"python cryptoback.py {encoded}",
        shell=True,
        capture_output=True,
        text=True,
    )
    if decoded in run_cap.stdout:
        print("Success")
    else:
        print("...Failure...")


def main():
    """Initialize the program."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--num_tests", type=int, default=5, help="number of tests"
    )
    parser.add_argument("-w", "--words", type=int, default=2, help="number of words")
    args = parser.parse_args()

    word_dict = build_dict()

    for _ in range(args.num_tests):
        cipher = construct_cipher()
        test_words(cipher, args.words, word_dict)


if __name__ == "__main__":
    sys.exit(main())
