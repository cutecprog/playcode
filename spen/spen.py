#!bin/usr/python

def main():
    formatFile("example.spen", "example.txt")

def formatFile(infile, outfile):
    file = open(infile,"r")
    data = file.read()
    file.close()
    lineData = data.split('\n')
    data = "" # Reusing variable because why not?
   
    lineData = lineData[1:] # Right now I'm just ignoring doctype format
    for s in lineData:
        data += formatLine(s)
    file = open(outfile,"w")
    file.write(data)

def formatLine(s):
    if s == "":
        return "-"*85+"\n"
    elif s[0] == '@':
        s = s[1:]
        return setMargin(s,17,74)+"\n\n"
    elif s[0] == '^':
        s = s[1:]
        return setMargin(s,17,74)+"\n\n"
    elif s[0] == '$':
        s = s[1:]
        return setMargin(s,17,74)+"\n\n"
    elif s[0] == '%':
        s = s[1:]
        return setMargin(s,41,74)+"\n"
    elif s[0] == '(':
        s += ")"
        return setMargin(s,34,54)+"\n"
    elif s[0] == '"':
        s = s[1:]
        return setMargin(s,21,61)+"\n\n"
    else:
        return "Error: INVALID line start"+"\n"

def setMargin(str,start,end):
    rowSize = end-start
    result = ""

    while(str!=""):
        if len(str)<rowSize:
            result += (" "*start)+str
            str=""
        elif str[rowSize]==" ":
            result += (" "*start)+str[:rowSize]+"\n"
            str = str[rowSize+1:]
        else:
            lastWord=str[:rowSize].rfind(" ")
            result += (" "*start)+str[:lastWord]+"\n"
            str = str[lastWord+1:]
    return result

def center(str):
    return (" "*((80-len(str))/2)) + str

if __name__ == '__main__':
    main()
