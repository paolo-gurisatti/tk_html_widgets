import os
import sys
import tkinter as tk
from argparse import ArgumentParser

sys.path.insert(0, '..')
from tk_html_widgets import HTMLText, HTMLScrolledText, HTMLLabel

def start_gui(html):
    #----------------------------------------------------------------------------------------------
    root = tk.Tk()
    text = HTMLText(root)
    text.pack(fill="both", expand=True)
    text.set_html(html)
    text.fit_height()
    return root.mainloop()


if __name__ == "__main__":
    #----------------------------------------------------------------------------------------------
    parser = ArgumentParser(usage="python3 %s <html_file>" % __file__)

    parser.add_argument('html_file', help='Set html file to load')

    args = parser.parse_args()

    if os.path.exists(args.html_file):
        sys.exit(start_gui(open(args.html_file, "r" ).read()))
    else:
        print("File not found")
        sys.exit(1)
    
