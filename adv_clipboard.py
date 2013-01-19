from sys import argv
from re import sub

import pygtk
import gtk
pygtk.require('2.0')

cb = gtk.clipboard_get()

if argv[1] == 's':
        with open("./clipboard", "w") as f:
                f.write(cb.wait_for_text())
else:
        with open("./clipboard", "r") as f:
                cb.set_text(f.read())
                cb.store()

def file_set(f, index):
        """Sets clipboard file to current copied text at index.
        
        """
        pass

def file_get(f, index):
        """Returns desire data from clipboard file.
        
        """
        pass
