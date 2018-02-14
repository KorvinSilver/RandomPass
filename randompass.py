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
import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
import os
import secrets
import shutil
import string
import sys

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2018, Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "dev@korvin.eu"
__status__ = "Production"


def downloader():
    """Replace word and stop-word list"""
    # Get the download directory chosen by nltk
    download_dir = nltk.downloader.Downloader().default_download_dir()
    # Remove directory corpora from it, ignore errors
    download_dir = os.path.join(download_dir, "corpora")
    shutil.rmtree(download_dir, ignore_errors=True)
    # Download word and stop-word list
    nltk.download("words")
    nltk.download("stopwords")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage="%(prog)s [-h|-a|-b|-o|-d|-x|-u] [-e] | [-w] [-e]] "
              "number [custom-set]",
        description="Generate a random password or passphrase")
    parser.add_argument("number", nargs="?",
                        help="number of characters, a positive integer")
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
            downloader()
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
    xor = sum([args.binary, args.octal, args.decimal, args.hexadecimal,
               args.alphanumeric, args.words, args.update_words])
    # Print help message if there's two optional arguments given, except the
    # argument extra-characters
    if xor > 1:
        print("Too many optional arguments given.")
        parser.print_help()
        sys.exit()

    # Make sure to update words even if number is provided
    if args.update_words and args.number:
        downloader()
        sys.exit()

    # Passphrase from words
    if args.words:
        try:
            # Get word list
            word_list = words.words()
            stop_word_list = stopwords.words("english")
        except LookupError:
            # Download if not available
            downloader()
            word_list = words.words()
            stop_word_list = stopwords.words("english")

        # Remove stop words
        word_list = [i for i in word_list if i not in stop_word_list]
        # Remove words shorter than 3 characters
        word_list = [i for i in word_list if len(i) > 2]
        # Remove words with apostrophe
        word_list = [i for i in word_list if "'" not in i]

        # Store the random string
        rnd = ""
        # Get num random words
        for _ in range(num):
            rnd += secrets.choice(word_list) + " "

        # On argument extra-characters
        if args.extra_characters:
            # store extra characters
            ext = ""
            # store indices in rnd
            indices = []
            # get a random number from 0 to num, exclusive
            u = secrets.randbelow(num)
            # make it at least 2
            if u < 2:
                u = 2

            # loop in range of u
            for _ in range(u):
                # get random character from custom-set or string.punctuation
                try:
                    ext += secrets.choice("".join(args.custom_set))
                except IndexError:
                    ext += secrets.choice(string.punctuation)
                # pick a random index in rnd, don't pick the same twice
                r = 0
                while r in indices:
                    r = secrets.randbelow(len(rnd))
                indices.append(r)

            # expand rnd with extra characters at given indexes
            tmp = ""
            j = 0
            for i in range(len(rnd)):
                tmp += rnd[i]
                if i in indices:
                    tmp += ext[j]
                    j += 1
            rnd = tmp

        # Print passphrase
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
            if len(args.custom_set) > 0:
                for i in args.custom_set:
                    chars += i
            else:
                chars += string.punctuation

        # Remove duplicate characters
        chars = "".join(set(chars))
        # Generate and print a random string
        rnd = ""
        for _ in range(num):
            rnd += secrets.choice(chars)

        # Print password
        print(rnd)
