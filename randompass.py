#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project: RandomPass

Copyright 2018, Korvin F. Ezüst

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import string
import sys
from rndplib.generator import (
    download_words,
    word_list,
    passphrase,
    expanded_passphrase,
    expanded_chars,
    password)

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2018, Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "dev@korvin.eu"
__status__ = "Production"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="%(prog)s [-h|-a|-b|-o|-d|-x|-u] [-e] | [-w] [-e]] "
              "number [custom-set]",
        description="Generate a random password or passphrase")
    parser.add_argument("number", nargs="?",
                        help="number of characters or words, a positive "
                             "integer")
    parser.add_argument("custom_set", metavar="custom-set", nargs="*",
                        help="a custom set of characters")
    parser.add_argument("-a", "--alphanumeric", action="store_true",
                        help="use alphanumeric ASCII only")
    parser.add_argument("-b", "--binary", action="store_true",
                        help="use binary digits only")
    parser.add_argument("-o", "--octal", action="store_true",
                        help="use octal digits only")
    parser.add_argument("-d", "--decimal", action="store_true",
                        help="use decimal digits only")
    parser.add_argument("-x", "--hexadecimal", action="store_true",
                        help="use hexadecimal digits only")
    parser.add_argument("-w", "--words", action="store_true",
                        help="create passphrase from English words")
    parser.add_argument("-e", "--extra-characters", action="store_true",
                        help="mix extra characters in. Use "
                             "custom-set if provided or fall back to "
                             "ASCII punctuation marks")
    parser.add_argument("-u", "--update-words", action="store_true",
                        help="update word list and exit")
    args = parser.parse_args()

    try:
        # Try to convert number to an integer
        num = int(args.number)
    except ValueError:
        parser.print_help()
        sys.exit()
    except TypeError:
        # No positional argument is given
        if args.update_words:
            # update word list
            download_words()
            sys.exit()
        else:
            parser.print_help()
            sys.exit()

    # num can only be positive
    if num <= 0:
        parser.print_help()
        sys.exit()

    # sum int value of arguments: binary, octal, decimal, hexadecimal,
    # alphanumeric, words and update-words
    exclusive_argument_count = sum(
        [args.binary, args.octal, args.decimal, args.hexadecimal,
         args.alphanumeric, args.words, args.update_words])
    # Print help message if there's two optional arguments given, except the
    # argument extra-characters
    if exclusive_argument_count > 1:
        print("Too many optional arguments given.")
        parser.print_help()
        sys.exit()

    # Make sure to update words even if number is provided
    if args.update_words and args.number:
        download_words()
        sys.exit()

    # Passphrase from words
    if args.words:
        try:
            # Get word list
            words = word_list()
        except LookupError:
            # Download if not available
            download_words()
            words = word_list()

        # Print passphrase with or without extra chars
        rnd = passphrase(words, num)

        if args.extra_characters:
            print(expanded_passphrase(rnd, num, args.custom_set))
        else:
            print(rnd)

    # Password from characters
    else:
        # Default characters
        chars = string.printable.strip()  # without strip() it has white spaces

        # Modify chars based on arguments
        if args.alphanumeric:
            chars = string.ascii_letters + string.digits
        if args.binary:
            chars = "01"
        if args.octal:
            chars = string.octdigits
        if args.decimal:
            chars = string.digits
        if args.hexadecimal:
            chars = string.hexdigits.upper()

        # Add custom set of characters if any or fall back to ASCII
        # punctuation marks
        if args.extra_characters:
            chars = expanded_chars(chars, args.custom_set)

        # Generate and print the password
        print(password(chars, num))
