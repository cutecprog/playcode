import pygtk
import gtk

def main():
        pygtk.require('2.0')
        cb = gtk.clipboard_get()
        try:
                cb.set_text(com_alpha(cb.wait_for_text()))
                cb.store()
        except:
                print "Error: Nothing copied"

def com_alpha(text):
        lines = text.split('\n')
        present = []
        former = []
        no_date = []
        for line in lines:
                if line[len(line)-1] == 't':
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
