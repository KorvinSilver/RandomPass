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

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2018, Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "0.1a"
__email__ = "dev@korvin.eu"
__status__ = "Preview"

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
dec = tk.Button(nframe, text="-")
dec.grid(row=0, column=0)
inc = tk.Button(nframe, text="+")
inc.grid(row=0, column=2)

# Ok Button
ok_button = tk.Button(root, text="Generate")
ok_button.grid(row=9, column=1, pady=20)

# Password or passphrase
password = tk.StringVar()
# Output
password_out = tk.Text(root, height=1, wrap="none", font=fn)
password_out.grid(row=10, columnspan=2, sticky="WE")
pscroll = tk.Scrollbar(root, orient="horizontal")
pscroll.grid(row=11, columnspan=2, sticky="WE")
password_out.config(xscrollcommand=pscroll.set)
pscroll.config(command=password_out.xview)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=12, column=1, pady=20)

root.mainloop()
