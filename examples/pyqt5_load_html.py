import os
import sys
from argparse import ArgumentParser

from PyQt5.QtWidgets import QApplication, QTextBrowser
from PyQt5 import QtGui

#__________________________________________________________________________________________________
# Terminal Tab viewer

def start_gui(argv, html):
    #----------------------------------------------------------------------------------------------
    app = QApplication(argv)
    text = QTextBrowser()
    text.setOpenLinks(False)
    text.setReadOnly(True)
    text.setHtml(html)
    text.show()
    return app.exec_()


if __name__ == "__main__":
    #----------------------------------------------------------------------------------------------
    parser = ArgumentParser(usage="python3 %s <html_file>" % __file__)

    parser.add_argument('html_file', help='Set html file to load')

    args = parser.parse_args()

    if os.path.exists(args.html_file):
        sys.exit(start_gui(sys.argv, open(args.html_file, "r" ).read()))
    else:
        print("File not found")
        sys.exit(1)
    
