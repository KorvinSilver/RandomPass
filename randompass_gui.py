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

from rndplib.license import full_license_text
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from rndplib.generator import (
    download_words,
    word_list,
    passphrase,
    expanded_passphrase,
    password
)
import string
import webbrowser

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2018, Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "dev@korvin.eu"
__status__ = "Production"


class BasicWindow(tk.Tk):
    def __init__(self):
        super(BasicWindow, self).__init__()
        self.w = 600
        self.h = 400
        self.geometry(f"{self.w}x{self.h}")
        self.minsize(width=self.w, height=self.h)
        self.resizable(width=True, height=True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Center root window
        self.withdraw()
        self.update_idletasks()
        self.x = (self.winfo_screenwidth() - self.w) // 2
        self.y = (self.winfo_screenheight() - self.h) // 2
        self.geometry(f"+{self.x}+{self.y}")
        self.deiconify()

    def run(self):
        self.mainloop()


class AboutWindow(BasicWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.title("About")

        # Set bigger font
        fn = font.Font(size=14)

        # Title label
        label = tk.Label(
            self, text=f"RandomPass version {__version__}", font=fn)
        label.grid(row=0, columnspan=2, pady=20, padx=10)
        # Label with program description
        label2 = tk.Label(
            self,
            text=f"A program to generate various types of passwords and "
                 f"passphrases\n{__copyright__}\nLicensed under {__license__}")
        label2.grid(row=1, columnspan=2, padx=10, pady=10)

        def callback_python(event):
            """Open web browser to python.org"""
            webbrowser.open_new("https://www.python.org")

        # Label link to python.org
        label3 = tk.Label(
            self, text="Written in Python", fg="blue", cursor="hand2")
        label3.bind("<Button-1>", callback_python)
        label3.grid(row=2, columnspan=2, padx=10, pady=10)

        def callback_source(event):
            """Open web browser to source code"""
            webbrowser.open_new("https://gitlab.com/KorvinSilver/RandomPass")

        # Label link to source code
        label4 = tk.Label(
            self, text="View source code", fg="blue", cursor="hand2")
        label4.bind("<Button-1>", callback_source)
        label4.grid(row=3, columnspan=2, padx=10, pady=10)

        # Close button
        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.grid(row=4, columnspan=2, pady=20)


class DescWindow(BasicWindow):
    def __init__(self):
        super(DescWindow, self).__init__()
        self.title("Description")

        # Description
        desc = "\nThe program can generate various passwords with random " \
               "characters or\npassphrases with random English words.\n\n" \
               "You have the option to generate passwords or passphrases " \
               "containing the\nfollowing sets:\n\n" \
               "- ASCII characters from 33 to 126\n" \
               "- alphanumeric only -- ASCII 48-57, 65-90, and 97-122\n" \
               "- binary only -- digits from 0 to 1\n" \
               "- octal only -- digits from 0 to 7\n" \
               "- decimal only -- digits from 0 to 9\n" \
               "- hexadecimal only -- digits from 0 to F\n" \
               "- words -- randomly chosen English words from a dictionary " \
               "of over 236000 words\n\n" \
               "You can add your own characters to each and have the " \
               "program randomly pick\nfrom those as well. In case of a " \
               "passphrase, a random number of them will be\npicked and " \
               "placed at random positions into the passphrase."
        text = tk.Text(self, width=80)
        text.grid(row=0, columnspan=2)
        text.insert("0.0", desc)
        text.config(state="disabled")

        # Close button
        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.grid(row=1, columnspan=2, pady=10)


class LicenseWindow(BasicWindow):
    def __init__(self):
        super(LicenseWindow, self).__init__()
        self.title("License")

        # Group text field and scrollbar into a frame
        frame = tk.Frame(self)
        frame.grid(row=0, columnspan=2)
        # Text field, 80 characters wide
        text = tk.Text(frame, width=80)
        text.grid(row=0, column=0)
        # Scrollbar
        scroll = tk.Scrollbar(frame, orient="vertical")
        scroll.grid(row=0, column=1, sticky="NS")
        # Connect text field and scrollbar
        text.config(yscrollcommand=scroll.set)
        scroll.config(command=text.yview)

        # Full license text
        full_license = full_license_text()
        # Display license in text field and disable it
        text.insert("0.0", full_license)
        text.config(state="disabled")

        # Close button
        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.grid(row=1, columnspan=2, pady=10)


class MainWindow(BasicWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title("RandomPass")

        # Add font
        self.fn = font.Font(family="monospace", size=9)

        # Menu bar
        menu = tk.Menu(self)
        # File menu
        file = tk.Menu(menu, tearoff=0)
        file.add_command(
            label="Update word list", command=self.update_words)
        file.add_separator()
        file.add_command(label="Exit", command=self.destroy)
        menu.add_cascade(label="File", menu=file)
        # Help menu
        help_ = tk.Menu(menu, tearoff=0)

        def about_window():
            """Open the about window"""
            win = AboutWindow()
            win.run()

        def license_window():
            """Open the license window"""
            win = LicenseWindow()
            win.run()

        def desc_window():
            """Open description window"""
            win = DescWindow()
            win.run()

        help_.add_command(label="Description", command=desc_window)
        help_.add_command(label="License", command=license_window)
        help_.add_command(label="About", command=about_window)
        menu.add_cascade(label="Help", menu=help_)
        self.config(menu=menu)

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
        # Entry field
        self.input = tk.Entry(self, font=self.fn)
        self.input.grid(row=4, column=1, sticky="WE", padx=10)
        # Scrollbar
        self.cscroll = tk.Scrollbar(self, orient="horizontal")
        self.cscroll.grid(row=5, column=1, sticky="WE", padx=10)
        # Connect entry field and scrollbar
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
        self.pass_out.grid(row=10, columnspan=2, sticky="WE", padx=10)
        # Scrollbar
        self.pscroll = tk.Scrollbar(self, orient="horizontal")
        self.pscroll.grid(row=11, columnspan=2, sticky="WE", padx=10)
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
                self.pass_out.insert("0.0", "DOWNLOADING WORD LIST...")
                self.update_idletasks()
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

    def update_words(self):
        """Update word list"""
        self.pass_out.delete("0.0", tk.END)
        self.pass_out.insert("0.0", "UPDATING WORD LIST...")
        self.update_idletasks()
        download_words()
        self.pass_out.delete("0.0", tk.END)

    @staticmethod
    def pop_up(tt, tx):
        messagebox.showinfo(tt, tx)


if __name__ == "__main__":
    root = MainWindow()
    root.run()
