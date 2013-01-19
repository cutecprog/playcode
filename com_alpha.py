import pygtk
import gtk
import re

def main():
        pygtk.require('2.0')
        cb = gtk.clipboard_get()
        cb_text = cb.wait_for_text()
        if cb_text == None:
                print "Error: Nothing copied"
                return
        try:
                cb.set_text(com_alpha(cb_text))
                cb.store()
        except:
                print "Error: Please contact Andrea at andi.grooms@gmail.com"

def com_alpha(text):
        """Read in commitee text field and order it appropriately.
        
        """
        lines = text.strip('\n').split('\n')
        present = [] # list of current commitees
        former = []  # list of former commitees
        no_date = [] # list of commitees where the date served is unknown
        for line in lines:
                tmp = re.split('[-| ]', line)
                if tmp[len(tmp)-1] == 'present':
                        present.append(line.split(', '))
                elif line[len(line)-1].isdigit():
                        former.append(line.split(', '))
                else:
                        no_date.append(line.split(', '))
        present.sort(key = lambda x: x[len(x)-2])
        former.sort(key = lambda x: x[len(x)-2])
        no_date.sort(key = lambda x: x[len(x)-1])
        new_text = ""
        for line in present:
                new_text += line[0]
                for item in line[1:]:
                        new_text += ', ' + item
                new_text += '\n'
        for line in former:
                new_text += line[0]
                for item in line[1:]:
                        new_text += ', ' + item
                new_text += '\n'
        for line in no_date:
                new_text += line[0]
                for item in line[1:]:
                        new_text += ', ' + item
                new_text += '\n'
        return new_text

if __name__ == "__main__":
        main()
