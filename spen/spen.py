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
    data = formatTXT(lineData)

    file = open(outfile,"w")
    file.write(data)
    
def formatTXT(s):
    data =""
    length = len(s)
    i=0
    while i < length:
        if s[i] == "":
            data += "-"*85+"\n"
        elif s[i][0] == '%':
            s[i] = s[i][1:]
            data += setMargin(s[i],41,74)+"\n"
            i+=1
            if s[i][0] == '(':
                s[i] += ")"
                data += setMargin(s[i],34,54)+"\n"
                i+=1
            if s[i][0] == '"':
                s[i] = s[i][1:] 
                data += setMargin(s[i],21,61)+"\n\n"
        elif s[i][0] == '$':
            s[i] = s[i][1:]
            data += setMargin(s[i],17,74)+"\n\n"
        elif s[i][0] == '^':
            s[i] = s[i][1:]
            data += setMargin(s[i],17,74)+"\n\n"
        elif s[i][0] == '@':
            s[i] = s[i][1:]
            data += setMargin(s[i],17,74)+"\n\n"
        else:
            print "Error on line",i,"Unknown Format Character\n"
        i += 1
    return data

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
