#!/bin/python

from sys import stderr

# I know global variables but I think this is a good time for them.
template='''<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" type="text/css" href="./movie.css" />
</head>
<body>
<div id="script">
%s</div>
</body>
</html>'''
division = '<div class="%s">%s\n</div>'

def main():
   test = spen()
   test.add(slug(1, "ANN'S HOUSE", "DAY (NOON)"))
   test.add(action("Ann lays in her room reading a book. And woofs around a whole bunch like crazy woofing."))
   test.add(dialog("1ANN'S MOM", "Yelling from the other room", "Come get dinner sweety!"))
   test.add(dialog("2ANN'S MOM", "Yelling from the other room", "Come get dinner sweety!"))
   #test.delete(5)
   print test.formatHTML()
   #f = open("./newfile.html", "w")
   #f.write(test.formatHTML())

# Generic line
class line(object):
   def __init__(self, content):
      self.content = content
      
   def _set_margin(self,str,start,end):
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
      
   #def format():
      

# Slug line   
class slug(line):
   def __init__(self, light, location, time):
      line.__init__(self,location)
      self.light = light
      self.time = time
   def format(self):
      str = "INT." if self.light else "EXT."
      str += " "+self.content
      str += " - "+self.time
      return line._set_margin(self,str,17,74)
   def formatHTML(self):
      str = "INT." if self.light else "EXT."
      str += " "+self.content
      str += " - "+self.time
      return division % ("slug", str)

# Action line      
class action(line):
   def format(self):
      return line._set_margin(self,self.content,17,74)
   def formatHTML(self):
      return division % ("action", self.content)

# Dialog line      
class dialog(line):
   def __init__(self, speaker, para, dialog):
      line.__init__(self,dialog)
      self.speaker = speaker
      self.para = para
   def format(self):
      str = line._set_margin(self,self.speaker,41,74)+"\n"
      str += line._set_margin(self,"("+self.para,34,54)+")\n"
      str += line._set_margin(self,self.content,21,61)
      return str
   def formatHTML(self):
      str = division % ("speaker", self.speaker)+"\n"
      str += division % ("para", "("+self.para+")")+"\n"
      str += division % ("dialog", self.content)
      return str

# Main class      
class spen(object):
   def __init__(self):
      self.lines = []
      self.size = 0
      
   def add(self, new_line):
      self.lines.append(new_line)
      self.size+=1
      
   def insert(self, index, new_line):
      if self.size<index:
         print >> stderr, "Error: Insert out of range"
         return
      #if index==0:
         
      
   def delete(self, index):
      '''
      Deletes line at index
      '''
      if self.size<index:
         print >> stderr, "Error: Delete out of range"
         return
      if index==0:
         self.lines = self.lines[1:]
      elif index==self.size-1:
         self.lines = self.lines[:self.size-1]
      else:
         self.lines = self.lines[0:index]+self.lines[index+1:]
      size-=1
      
   def formatTXT(self):
      sum_str = ""
      for l in self.lines:
         sum_str += l.format() + "\n\n"
      return sum_str
      
   def formatHTML(self):
      sum_str = ""
      for l in self.lines:
         sum_str += l.formatHTML() + "\n"
      return template % sum_str


if __name__=="__main__":
   main()
   