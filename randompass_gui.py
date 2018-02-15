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

import tkinter as tk
from tkinter import font
from rndplib.generator import (
    downloader,
    words_stopwords,
    trimmed_words,
    passphrase,
    expanded_passphrase,
    password
)
import string

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2018, Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "0.9"
__email__ = "dev@korvin.eu"
__status__ = "Demo"

# Root window
root = tk.Tk()
root.title("RandomPass")
w = 480
h = 400
root.geometry(f"{w}x{h}")
root.minsize(width=480, height=400)
root.resizable(width=True, height=False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Center root window
root.withdraw()
root.update_idletasks()
x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"+{x}+{y}")
root.deiconify()

# Add font
fn = font.Font(family="monospace", size=9)

# Password type
pass_type = tk.StringVar()
# Password type selector
tk.Label(root, text="Type:").grid(row=0, column=0)
default = tk.Radiobutton(
    root, text="Default", variable=pass_type, value="default")
default.grid(row=1, column=0, sticky="W")
default.select()

alphanumeric = tk.Radiobutton(
    root, text="Alphanumeric", variable=pass_type, value="alphanumeric")
alphanumeric.grid(row=2, column=0, sticky="W")

binary = tk.Radiobutton(
    root, text="Binary", variable=pass_type, value="binary")
binary.grid(row=3, column=0, sticky="W")

octal = tk.Radiobutton(root, text="Octal", variable=pass_type, value="octal")
octal.grid(row=4, column=0, sticky="W")

decimal = tk.Radiobutton(
    root, text="Decimal", variable=pass_type, value="decimal")
decimal.grid(row=5, column=0, sticky="W")

hexadecimal = tk.Radiobutton(
    root, text="Hexadecimal", variable=pass_type, value="hexadecimal")
hexadecimal.grid(row=6, column=0, sticky="W")

words = tk.Radiobutton(root, text="Words", variable=pass_type, value="words")
words.grid(row=7, column=0, sticky="W")

# Extra options
option = tk.StringVar()

# Extra options selector
tk.Label(root, text="Extra characters:").grid(row=0, column=1)
none = tk.Radiobutton(
    root, text="None", variable=option, value="none")
none.grid(row=1, column=1, sticky="W")
none.select()

extra = tk.Radiobutton(
    root, text="ASCII punctuation marks", variable=option, value="ASCII")
extra.grid(row=2, column=1, sticky="W")

custom = tk.Radiobutton(
    root, text="Custom character set:", variable=option, value="custom")
custom.grid(row=3, column=1, sticky="W")

custom_input = tk.Entry(root, font=fn)
custom_input.grid(row=4, column=1, sticky="WE")
cscroll = tk.Scrollbar(root, orient="horizontal")
cscroll.grid(row=5, column=1, sticky="WE")
custom_input.config(xscrollcommand=cscroll.set)
cscroll.config(command=custom_input.xview)

# Number input
tk.Label(root, text="Number of characters or words:").grid(row=7, column=1)

nframe = tk.Frame(root)
nframe.grid(row=8, column=1, pady=10)
number = tk.Entry(nframe)
number.grid(row=0, column=1)


# Number increment and decrement buttons


def increment():
    """Increment number by one"""
    try:
        # Try casting it to int
        n = int(number.get())
        # Make sure it stays positive
        if n < 1:
            n = 0
    except ValueError:
        n = 0
    # Increment
    number.delete("0", tk.END)
    number.insert("0", str(n + 1))


def decrement():
    """Decrement number by one"""
    try:
        # Try casting it to int
        n = int(number.get())
        # Make sure it stays positive
        if n <= 1:
            n = 2
    except ValueError:
        n = 2
    # Decrement
    number.delete("0", tk.END)
    number.insert("0", str(n - 1))


dec = tk.Button(nframe, text="-", command=decrement)
dec.grid(row=0, column=0)
inc = tk.Button(nframe, text="+", command=increment)
inc.grid(row=0, column=2)

# Output
pass_out = tk.Text(root, height=1, wrap="none", font=fn)
pass_out.grid(row=10, columnspan=2, sticky="WE")
pscroll = tk.Scrollbar(root, orient="horizontal")
pscroll.grid(row=11, columnspan=2, sticky="WE")
pass_out.config(xscrollcommand=pscroll.set)
pscroll.config(command=pass_out.xview)


def generate():
    """Generate password or passphrase"""
    global pass_type
    # Clear text field
    pass_out.delete("0.0", tk.END)
    # Get password type and extra option
    t = pass_type.get()
    o = option.get()

    if t == "alphanumeric":
        chars = string.ascii_letters + string.digits
        if o == "ASCII":
            chars += string.punctuation
        elif o == "custom":
            chars += custom_input.get()
    elif t == "binary":
        chars = "01"
        if o == "ASCII":
            chars += string.punctuation
        elif o == "custom":
            chars += custom_input.get()
    elif t == "octal":
        chars = string.octdigits
        if o == "ASCII":
            chars += string.punctuation
        elif o == "custom":
            chars += custom_input.get()
    elif t == "decimal":
        chars = string.digits
        if o == "ASCII":
            chars += string.punctuation
        elif o == "custom":
            chars += custom_input.get()
    elif t == "hexadecimal":
        chars = string.hexdigits
        if o == "ASCII":
            chars += string.punctuation
        elif o == "custom":
            chars += custom_input.get()
    else:
        chars = string.printable.strip()
        if o == "custom":
            chars += custom_input.get()
    # Convert number to int or print error message and set it to zero
    try:
        n = int(number.get())
        if n <= 0:
            pass_out.insert("0.0", "INVALID NUMBER")
    except ValueError:
        pass_out.insert("0.0", "INVALID NUMBER")
        n = 0

    # Type is password
    if t != "words":
        # If n <= zero, there's nothing to do
        if n > 0:
            # Print password
            pass_out.insert("0.0", password(chars, n))

    # Type is passphrase
    else:
        # Get word list
        try:
            word_list, stop_word_list = words_stopwords()
            word_list = trimmed_words(word_list, stop_word_list)
        except LookupError:
            # TODO: make this message appear before download
            pass_out.insert("0.0", "DOWNLOADING WORD LIST...")
            downloader()
            pass_out.delete("0.0", tk.END)
            word_list, stop_word_list = words_stopwords()
            word_list = trimmed_words(word_list, stop_word_list)

        # Set value of ext based on selected extra option
        if o == "ASCII":
            ext = string.punctuation
        elif o == "custom":
            ext = custom_input.get()
        else:
            ext = ""
        # The function expanded_passphrase needs a list
        ext = [i for i in ext]
        # Get passphrase
        p = passphrase(word_list, n)
        # If n == zero, nothing to do
        if n > 0:
            # Expand passphrase with characters from ext if any
            if len(ext) > 0:
                p = expanded_passphrase(p, n, ext)
            # Print passphrase
            pass_out.insert("0.0", p)


# Generate Button
generate_button = tk.Button(root, text="Generate", command=generate)
generate_button.grid(row=9, column=1, pady=20)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=12, column=1, pady=20)

root.mainloop()
