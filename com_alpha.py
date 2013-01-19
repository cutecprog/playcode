
def main():
        S = a = raw_input()
        while a != "":
                a = raw_input()
                S += '\n' + a
        S = S.strip('\n')
        print com_alpha(S)

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
        key = lambda x: x[len(x)-1]
        key2 = lambda x: x[len(x)-2]
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
