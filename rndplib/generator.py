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

import nltk
from nltk.corpus import stopwords
from nltk.corpus import words
import os
import secrets
import shutil
import string

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2018, Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "dev@korvin.eu"
__status__ = "Production"


def download_words():
    """Replace word and stop-word list"""
    # Get the download directory chosen by nltk
    download_dir = nltk.downloader.Downloader().default_download_dir()
    # Remove directory corpora from it, ignore errors
    download_dir = os.path.join(download_dir, "corpora")
    shutil.rmtree(download_dir, ignore_errors=True)
    # Download word and stop-word list
    nltk.download("words")
    nltk.download("stopwords")


def word_list():
    """
    Return English words minus short words, stop-words and words with
    apostrophe

    :return: English words
    :rtype: list
    """
    w = words.words()
    sw = stopwords.words("english")
    # Remove stop words
    w = [i for i in w if i not in sw]
    # Remove words shorter than 3 characters
    w = [i for i in w if len(i) > 2]
    # Remove words with apostrophe
    w = [i for i in w if "'" not in i]
    return w


def passphrase(w, n):
    """
    Generate passphrase

    :param w: word list
    :type w: list
    :param n: number of words
    :type n: int
    :return: passphrase
    :rtype: str
    """
    # Store the random string
    rd = ""
    # Get n random words
    for _ in range(n):
        rd += secrets.choice(w) + " "
    return rd


def expanded_passphrase(rd, n, cset):
    """
    Mix extra characters into passphrase

    :param rd: passphrase
    :type rd: str
    :param n: number of words
    :type n: int
    :param cset: extra character set
    :type cset: lsit
    :return: passphrase with extra characters
    :rtype: str
    """
    # Store extra characters if any
    ext = ""
    # Store indices of rd
    indices = []
    # Get a random number from 0 to n, exclusive
    u = secrets.randbelow(n)
    # Make it at least 2
    if u < 2:
        u = 2
    # Loop in range of u
    for _ in range(u):
        # Get random character from cset or string.punctuation
        try:
            ext += secrets.choice("".join(cset))
        except IndexError:
            ext += secrets.choice(string.punctuation)
        # Pick a random index in rd, don't pick the same twice
        r = 0
        while r in indices:
            r = secrets.randbelow(len(rd))
        indices.append(r)
    # Expand rd with extra characters at given indices
    tmp = ""
    j = 0
    for i in range(len(rd)):
        tmp += rd[i]
        if i in indices:
            tmp += ext[j]
            j += 1
    return tmp


def expanded_chars(ch, cset):
    """
    Add extra characters or ASCII punctuation marks to initial character set

    :param ch: initial character set
    :type ch: str
    :param cset: extra characters
    :type cset: list
    :return: final character set
    :rtype: str
    """
    if len(cset) > 0:
        # Add extra characters
        for i in cset:
            ch += i
    else:
        # Add ASCII punctuation marks
        ch += string.punctuation
    return ch


def password(ch, n):
    """
    Generate password

    :param ch: character set
    :type ch: str
    :param n: number of characters
    :type n: int
    :return: password
    :rtype: str
    """
    # Remove duplicate characters
    ch = "".join(set(ch))
    # Store password
    rd = ""
    # Pick random characters from ch
    for _ in range(n):
        rd += secrets.choice(ch)
    return rd
