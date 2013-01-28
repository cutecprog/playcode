from re import split

def main():
        cb = gtk.clipboard_get()
        cb_text = cb.wait_for_text()
        if cb_text == None:
                print "Error: Nothing copied"
                return
        cb.set_text(com_alpha(cb_text))
        cb.store()

def com_alpha(text):
        """Read in commitee text field and order it appropriately.
        
        """
        def list_to_string(data):
                """Convert 2d list to multi-line text.
                
                """
                text = ""
                for line in data:
                        text += line[0]
                        for item in line[1:]:
                                text += ', ' + item
                        text += '\n'
                return text
        lines = text.strip('\n').split('\n')
        current = [] # list of current commitees
        former = []  # list of former commitees
        current_no_date = [] # list of current commitees where the date served is unknown
        former_no_date = []  # list of former commitees where the date served is unknown
        for line in lines:
                words = split('[-| ]', line)
                last_word = words[len(words)-1]
                if last_word == 'present':
                        current.append(line.split(', '))
                elif words[len(words)-1].isdigit():
                        former.append(line.split(', '))
                else:
                        if words[0].lower() == "former" or words[0].lower() == "retired":
                                former_no_date.append(line.split(', '))
                        else:
                                current_no_date.append(line.split(', '))
        current.sort(key = lambda x: x[len(x)-2]) # Sort by commitee name
        former.sort(key = lambda x: x[len(x)-2])
        former.sort(key = lambda x: int(x[len(x)-1].split('-')[1]))
        current_no_date.sort(key = lambda x: x[len(x)-1])
        former_no_date.sort(key = lambda x: x[len(x)-1])
        return list_to_string(current) + list_to_string(former) \
                + list_to_string(current_no_date) + list_to_string(former_no_date)

if __name__ == "__main__":
        import pygtk
        import gtk
        pygtk.require('2.0')
        main()
