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
    download_words,
    word_list,
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


class MainWindow(tk.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title("RandomPass")
        self.w = 480
        self.h = 400
        self.geometry(f"{self.w}x{self.h}")
        self.minsize(width=self.w, height=self.h)
        self.resizable(width=True, height=False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Center root window
        self.withdraw()
        self.update_idletasks()
        self.x = (self.winfo_screenwidth() - self.w) // 2
        self.y = (self.winfo_screenheight() - self.h) // 2
        self.geometry(f"+{self.x}+{self.y}")
        self.deiconify()

        # Add font
        self.fn = font.Font(family="monospace", size=9)

        # Password or passphrase type
        self.pass_type = tk.StringVar()
        # Extra option type
        self.option = tk.StringVar()

        # Type selector
        # Label
        tk.Label(self, text="Type:").grid(row=0, column=0)
        # Radio button
        self.default = tk.Radiobutton(
            self, text="Default", variable=self.pass_type, value="default")
        self.default.grid(row=1, column=0, sticky="W")
        self.default.select()
        # Radio button
        self.alphanumeric = tk.Radiobutton(
            self,
            text="Alphanumeric",
            variable=self.pass_type,
            value="alphanumeric")
        self.alphanumeric.grid(row=2, column=0, sticky="W")
        # Radio button
        self.binary = tk.Radiobutton(
            self,
            text="Binary",
            variable=self.pass_type,
            value="binary")
        self.binary.grid(row=3, column=0, sticky="W")
        # Radio button
        self.octal = tk.Radiobutton(
            self, text="Octal", variable=self.pass_type, value="octal")
        self.octal.grid(row=4, column=0, sticky="W")
        # Radio button
        self.decimal = tk.Radiobutton(
            self, text="Decimal", variable=self.pass_type, value="decimal")
        self.decimal.grid(row=5, column=0, sticky="W")
        # Radio button
        self.hexadecimal = tk.Radiobutton(
            self,
            text="Hexadecimal",
            variable=self.pass_type,
            value="hexadecimal")
        self.hexadecimal.grid(row=6, column=0, sticky="W")
        # Radio button
        self.words = tk.Radiobutton(
            self, text="Words", variable=self.pass_type, value="words")
        self.words.grid(row=7, column=0, sticky="W")

        # Extra option selector
        # Label
        tk.Label(self, text="Extra characters:").grid(row=0, column=1)
        # Radio button
        self.none = tk.Radiobutton(
            self, text="None", variable=self.option, value="none")
        self.none.grid(row=1, column=1, sticky="W")
        self.none.select()
        # Radio button
        self.extra = tk.Radiobutton(
            self,
            text="ASCII punctuation marks",
            variable=self.option,
            value="ASCII")
        self.extra.grid(row=2, column=1, sticky="W")
        # Radio button
        self.custom = tk.Radiobutton(
            self,
            text="Custom character set:",
            variable=self.option,
            value="custom")
        self.custom.grid(row=3, column=1, sticky="W")

        # Custom characters input field
        self.input = tk.Entry(self, font=self.fn)
        self.input.grid(row=4, column=1, sticky="WE")
        self.cscroll = tk.Scrollbar(self, orient="horizontal")
        self.cscroll.grid(row=5, column=1, sticky="WE")
        self.input.config(xscrollcommand=self.cscroll.set)
        self.cscroll.config(command=self.input.xview)

        # Number input field
        # Label
        tk.Label(
            self, text="Number of characters or words:").grid(row=7, column=1)
        # Frame of decrement button, number input field and increment button
        self.nframe = tk.Frame(self)
        self.nframe.grid(row=8, column=1, pady=10)
        self.number = tk.Entry(self.nframe)
        self.number.grid(row=0, column=1)
        # Number increment and decrement buttons
        self.dec = tk.Button(self.nframe, text="-", command=self.decrement)
        self.dec.grid(row=0, column=0)
        self.inc = tk.Button(self.nframe, text="+", command=self.increment)
        self.inc.grid(row=0, column=2)

        # Output field
        # Text field
        self.pass_out = tk.Text(self, height=1, wrap="none", font=self.fn)
        self.pass_out.grid(row=10, columnspan=2, sticky="WE")
        # Scrollbar
        self.pscroll = tk.Scrollbar(self, orient="horizontal")
        self.pscroll.grid(row=11, columnspan=2, sticky="WE")
        # Connect text field to scrollbar
        self.pass_out.config(xscrollcommand=self.pscroll.set)
        self.pscroll.config(command=self.pass_out.xview)

        # Generate Button
        self.generate_button = tk.Button(
            self, text="Generate", command=self.generate)
        self.generate_button.grid(row=9, column=1, pady=20)

        # Exit Button
        self.exit_button = tk.Button(self, text="Exit", command=self.destroy)
        self.exit_button.grid(row=12, column=1, pady=20)

    def increment(self):
        """Increment number by one"""
        try:
            # Try casting it to int
            n = int(self.number.get())
            # Make sure it stays positive
            if n < 1:
                n = 0
        except ValueError:
            n = 0
        # Increment
        self.number.delete("0", tk.END)
        self.number.insert("0", str(n + 1))

    def decrement(self):
        """Decrement number by one"""
        try:
            # Try casting it to int
            n = int(self.number.get())
            # Make sure it stays positive
            if n <= 1:
                n = 2
        except ValueError:
            n = 2
        # Decrement
        self.number.delete("0", tk.END)
        self.number.insert("0", str(n - 1))

    def generate(self):
        """Generate password or passphrase"""
        # Clear text field
        self.pass_out.delete("0.0", tk.END)
        # Get password type and extra option
        t = self.pass_type.get()
        o = self.option.get()

        if t == "alphanumeric":
            chars = string.ascii_letters + string.digits
            if o == "ASCII":
                chars += string.punctuation
            elif o == "custom":
                chars += self.input.get()
        elif t == "binary":
            chars = "01"
            if o == "ASCII":
                chars += string.punctuation
            elif o == "custom":
                chars += self.input.get()
        elif t == "octal":
            chars = string.octdigits
            if o == "ASCII":
                chars += string.punctuation
            elif o == "custom":
                chars += self.input.get()
        elif t == "decimal":
            chars = string.digits
            if o == "ASCII":
                chars += string.punctuation
            elif o == "custom":
                chars += self.input.get()
        elif t == "hexadecimal":
            chars = string.hexdigits.upper()
            if o == "ASCII":
                chars += string.punctuation
            elif o == "custom":
                chars += self.input.get()
        else:
            chars = string.printable.strip()
            if o == "custom":
                chars += self.input.get()
        # Convert number to int or print error message and set it to zero
        try:
            n = int(self.number.get())
            if n <= 0:
                self.pass_out.insert("0.0", "INVALID NUMBER")
        except ValueError:
            self.pass_out.insert("0.0", "INVALID NUMBER")
            n = 0

        # Type is password
        if t != "words":
            # If n <= zero, there's nothing to do
            if n > 0:
                # Print password
                self.pass_out.insert("0.0", password(chars, n))

        # Type is passphrase
        else:
            # Get word list
            try:
                w = word_list()
            except LookupError:
                # TODO: make this message appear before download
                self.pass_out.insert("0.0", "DOWNLOADING WORD LIST...")
                download_words()
                self.pass_out.delete("0.0", tk.END)
                w = word_list()

            # Set value of ext based on selected extra option
            if o == "ASCII":
                ext = string.punctuation
            elif o == "custom":
                ext = self.input.get()
            else:
                ext = ""
            # The function expanded_passphrase needs a list
            ext = [i for i in ext]
            # Get passphrase
            p = passphrase(w, n)
            # If n == zero, nothing to do
            if n > 0:
                # Expand passphrase with characters from ext if any
                if len(ext) > 0:
                    p = expanded_passphrase(p, n, ext)
                # Print passphrase
                self.pass_out.insert("0.0", p)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    root = MainWindow()
    root.run()
