from sys import argv
from re import sub

import pygtk
import gtk
pygtk.require('2.0')

cb = gtk.clipboard_get()

if argv[1] == 's':
        with open("./c" + argv[2], "w") as f:
                f.write(cb.wait_for_text())
else:
        with open("./c" + argv[1], "r") as f:
                cb.set_text(f.read())
                cb.store()
