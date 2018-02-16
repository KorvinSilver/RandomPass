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
__version__ = "0.9"
__email__ = "dev@korvin.eu"
__status__ = "Demo"


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
            text="A program to create various types of passwords and "
                 "passphrases")
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


class DocWindow(BasicWindow):
    pass


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
        license_text = \
            "\n                                 Apache License\n            " \
            " " \
            "              Version 2.0, January 2004\n                      " \
            " " \
            " http://www.apache.org/licenses/\n\n   TERMS AND CONDITIONS FOR" \
            " " \
            "USE, REPRODUCTION, AND DISTRIBUTION\n\n   1. Definitions.\n\n  " \
            " " \
            "   \"License\" shall mean the terms and conditions for use, " \
            "reproduction,\n      and distribution as defined by Sections 1 " \
            "through 9 of this document.\n\n      \"Licensor\" shall mean " \
            "the copyright owner or entity authorized by\n      the " \
            "copyright owner that is granting the License.\n\n      \"Legal " \
            "Entity\" shall mean the union of the acting entity and all\n   " \
            " " \
            "  other entities that control, are controlled by, or are under " \
            "common\n      control with that entity. For the purposes of " \
            "this definition,\n      \"control\" means (i) the power, " \
            "direct or indirect, to cause the\n      direction or management" \
            " " \
            "of such entity, whether by contract or\n      otherwise, " \
            "or (ii) ownership of fifty percent (50%) or more of the\n      " \
            "outstanding shares, or (iii) beneficial ownership of such " \
            "entity.\n\n      \"You\" (or \"Your\") shall mean an individual" \
            " " \
            "or Legal Entity\n      exercising permissions granted by this " \
            "License.\n\n      \"Source\" form shall mean the preferred form" \
            " " \
            "for making modifications,\n      including but not limited to " \
            "software source code, documentation\n      source, " \
            "and configuration files.\n\n      \"Object\" form shall mean " \
            "any form resulting from mechanical\n      transformation or " \
            "translation of a Source form, including but\n      not limited " \
            "to compiled object code, generated documentation,\n      and " \
            "conversions to other media types.\n\n      \"Work\" shall mean " \
            "the work of authorship, whether in Source or\n      Object " \
            "form, made available under the License, as indicated by a\n    " \
            " " \
            " copyright notice that is included in or attached to the work\n" \
            " " \
            "     (an example is provided in the Appendix below).\n\n      " \
            "\"Derivative Works\" shall mean any work, whether in Source or " \
            "Object\n      form, that is based on (or derived from) the Work" \
            " " \
            "and for which the\n      editorial revisions, annotations, " \
            "elaborations, or other modifications\n      represent, " \
            "as a whole, an original work of authorship. For the purposes\n " \
            " " \
            "    of this License, Derivative Works shall not include works " \
            "that remain\n      separable from, or merely link (or bind by " \
            "name) to the interfaces of,\n      the Work and Derivative " \
            "Works thereof.\n\n      \"Contribution\" shall mean any work of" \
            " " \
            "authorship, including\n      the original version of the Work " \
            "and any modifications or additions\n      to that Work or " \
            "Derivative Works thereof, that is intentionally\n      " \
            "submitted to Licensor for inclusion in the Work by the " \
            "copyright owner\n      or by an individual or Legal Entity " \
            "authorized to submit on behalf of\n      the copyright owner. " \
            "For the purposes of this definition, \"submitted\"\n      means" \
            " " \
            "any form of electronic, verbal, or written communication sent\n" \
            " " \
            "     to the Licensor or its representatives, including but not " \
            "limited to\n      communication on electronic mailing lists, " \
            "source code control systems,\n      and issue tracking systems " \
            "that are managed by, or on behalf of, the\n      Licensor for " \
            "the purpose of discussing and improving the Work, but\n      " \
            "excluding communication that is conspicuously marked or " \
            "otherwise\n      designated in writing by the copyright owner " \
            "as \"Not a Contribution.\"\n\n      \"Contributor\" shall mean " \
            "Licensor and any individual or Legal Entity\n      on behalf of" \
            " " \
            "whom a Contribution has been received by Licensor and\n      " \
            "subsequently incorporated within the Work.\n\n   2. Grant of " \
            "Copyright License. Subject to the terms and conditions of\n    " \
            " " \
            " this License, each Contributor hereby grants to You a " \
            "perpetual,\n      worldwide, non-exclusive, no-charge, " \
            "royalty-free, irrevocable\n      copyright license to " \
            "reproduce, prepare Derivative Works of,\n      publicly " \
            "display, publicly perform, sublicense, and distribute the\n    " \
            " " \
            " Work and such Derivative Works in Source or Object form.\n\n  " \
            " " \
            "3. Grant of Patent License. Subject to the terms and conditions" \
            " " \
            "of\n      this License, each Contributor hereby grants to You a" \
            " " \
            "perpetual,\n      worldwide, non-exclusive, no-charge, " \
            "royalty-free, irrevocable\n      (except as stated in this " \
            "section) patent license to make, have made,\n      use, " \
            "offer to sell, sell, import, and otherwise transfer the Work," \
            "\n      where such license applies only to those patent claims " \
            "licensable\n      by such Contributor that are necessarily " \
            "infringed by their\n      Contribution(s) alone or by " \
            "combination of their Contribution(s)\n      with the Work to " \
            "which such Contribution(s) was submitted. If You\n      " \
            "institute patent litigation against any entity (including a\n  " \
            " " \
            "   cross-claim or counterclaim in a lawsuit) alleging that the " \
            "Work\n      or a Contribution incorporated within the Work " \
            "constitutes direct\n      or contributory patent infringement, " \
            "then any patent licenses\n      granted to You under this " \
            "License for that Work shall terminate\n      as of the date " \
            "such litigation is filed.\n\n   4. Redistribution. You may " \
            "reproduce and distribute copies of the\n      Work or " \
            "Derivative Works thereof in any medium, with or without\n      " \
            "modifications, and in Source or Object form, provided that " \
            "You\n      meet the following conditions:\n\n      (a) You must" \
            " " \
            "give any other recipients of the Work or\n          Derivative " \
            "Works a copy of this License; and\n\n      (b) You must cause " \
            "any modified files to carry prominent notices\n          " \
            "stating that You changed the files; and\n\n      (c) You must " \
            "retain, in the Source form of any Derivative Works\n          " \
            "that You distribute, all copyright, patent, trademark, and\n   " \
            " " \
            "      attribution notices from the Source form of the Work," \
            "\n          excluding those notices that do not pertain to any " \
            "part of\n          the Derivative Works; and\n\n      (d) If " \
            "the Work includes a \"NOTICE\" text file as part of its\n      " \
            " " \
            "   distribution, then any Derivative Works that You distribute " \
            "must\n          include a readable copy of the attribution " \
            "notices contained\n          within such NOTICE file, excluding" \
            " " \
            "those notices that do not\n          pertain to any part of the" \
            " " \
            "Derivative Works, in at least one\n          of the following " \
            "places: within a NOTICE text file distributed\n          as " \
            "part of the Derivative Works; within the Source form or\n      " \
            " " \
            "   documentation, if provided along with the Derivative Works; " \
            "or,\n          within a display generated by the Derivative " \
            "Works, if and\n          wherever such third-party notices " \
            "normally appear. The contents\n          of the NOTICE file are" \
            " " \
            "for informational purposes only and\n          do not modify " \
            "the License. You may add Your own attribution\n          " \
            "notices within Derivative Works that You distribute, " \
            "alongside\n          or as an addendum to the NOTICE text from " \
            "the Work, provided\n          that such additional attribution " \
            "notices cannot be construed\n          as modifying the " \
            "License.\n\n      You may add Your own copyright statement to " \
            "Your modifications and\n      may provide additional or " \
            "different license terms and conditions\n      for use, " \
            "reproduction, or distribution of Your modifications, or\n      " \
            "for any such Derivative Works as a whole, provided Your use," \
            "\n      reproduction, and distribution of the Work otherwise " \
            "complies with\n      the conditions stated in this License.\n\n" \
            " " \
            "  5. Submission of Contributions. Unless You explicitly state " \
            "otherwise,\n      any Contribution intentionally submitted for " \
            "inclusion in the Work\n      by You to the Licensor shall be " \
            "under the terms and conditions of\n      this License, without " \
            "any additional terms or conditions.\n      Notwithstanding the " \
            "above, nothing herein shall supersede or modify\n      the " \
            "terms of any separate license agreement you may have executed\n" \
            " " \
            "     with Licensor regarding such Contributions.\n\n   6. " \
            "Trademarks. This License does not grant permission to use the " \
            "trade\n      names, trademarks, service marks, or product names" \
            " " \
            "of the Licensor,\n      except as required for reasonable and " \
            "customary use in describing the\n      origin of the Work and " \
            "reproducing the content of the NOTICE file.\n\n   7. Disclaimer" \
            " " \
            "of Warranty. Unless required by applicable law or\n      agreed" \
            " " \
            "to in writing, Licensor provides the Work (and each\n      " \
            "Contributor provides its Contributions) on an \"AS IS\" BASIS," \
            "\n      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either " \
            "express or\n      implied, including, without limitation, " \
            "any warranties or conditions\n      of TITLE, NON-INFRINGEMENT," \
            " " \
            "MERCHANTABILITY, or FITNESS FOR A\n      PARTICULAR PURPOSE. " \
            "You are solely responsible for determining the\n      " \
            "appropriateness of using or redistributing the Work and assume " \
            "any\n      risks associated with Your exercise of permissions " \
            "under this License.\n\n   8. Limitation of Liability. In no " \
            "event and under no legal theory,\n      whether in tort (" \
            "including negligence), contract, or otherwise,\n      unless " \
            "required by applicable law (such as deliberate and grossly\n   " \
            " " \
            "  negligent acts) or agreed to in writing, shall any " \
            "Contributor be\n      liable to You for damages, including any " \
            "direct, indirect, special,\n      incidental, or consequential " \
            "damages of any character arising as a\n      result of this " \
            "License or out of the use or inability to use the\n      Work (" \
            "including but not limited to damages for loss of goodwill," \
            "\n      work stoppage, computer failure or malfunction, or any " \
            "and all\n      other commercial damages or losses), even if " \
            "such Contributor\n      has been advised of the possibility of " \
            "such damages.\n\n   9. Accepting Warranty or Additional " \
            "Liability. While redistributing\n      the Work or Derivative " \
            "Works thereof, You may choose to offer,\n      and charge a fee" \
            " " \
            "for, acceptance of support, warranty, indemnity,\n      or " \
            "other liability obligations and/or rights consistent with " \
            "this\n      License. However, in accepting such obligations, " \
            "You may act only\n      on Your own behalf and on Your sole " \
            "responsibility, not on behalf\n      of any other Contributor, " \
            "and only if You agree to indemnify,\n      defend, and hold " \
            "each Contributor harmless for any liability\n      incurred by," \
            " " \
            "or claims asserted against, such Contributor by reason\n      " \
            "of your accepting any such warranty or additional " \
            "liability.\n\n   END OF TERMS AND CONDITIONS\n"
        # Display license in text field and disable it
        text.insert("0.0", license_text)
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

        def doc_window():
            """Open documentation window"""
            # TODO: finish this when README is ready
            pass

        help_.add_command(label="Documentation", command=doc_window)
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
