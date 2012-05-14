#!/bin/python

from sys import stderr
from sys import stdout

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
   screen_play = spen()
   screen_play.add(slug(1,"Dog House","Day"))
   screen_play.add(action("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent velit nisl, faucibus vel pellentesque ac, fringilla in ipsum. Sed ac ante in purus rutrum aliquet a eu velit. Nullam sit amet est purus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas."))
   screen_play.add(dialog("NYMERIA", "", "Woof, woof!"))
   #screen_play.add("NYMERIA")
   screen_play.add(dialog("BRONX (O.S)", "Yelling from inside a dog house", "Ruff ruff ruff ruff!"))
   screen_play.insert(1, action("The dogs sit in a rainy backyard")) # Inserts line after the second
   screen_play.delete(2) # Deletes line with vulgar Latin in it
   #print screen_play.formatHTML()
   f = open("./newfile.html", "w")
   f.write(screen_play.formatHTML())

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
      if self.para!="":
         str += division % ("para", "("+self.para+")")+"\n"
      str += division % ("dialog", self.content)
      return str

# Main class      
class spen(object):
   def __init__(self):
      self.lines = []
      self.size = 0
      
   def add(self, new_line):
      '''
      Appends item to the back lines
      >>> a = spen()
      >>> a.add(line("Test!"))
      >>> print a.lines[0].content
      Test!
      >>> print a.size
      1
      '''
      self.lines.append(new_line)
      self.size+=1
      
   def insert(self, index, new_line):
      '''
      Inserts item at index
      >>> a = spen()
      >>> a.insert(0,line("Test!"))
      >>> print a.lines[0].content
      Test!
      >>> print a.size
      1
      '''
      if self.size<index:
         print >> stderr, "Error: Insert out of range"
         return
      self.lines.insert(index, new_line)
      self.size+=1
      
   def delete(self, index):
      '''
      Deletes line at index
      >>> a = spen()
      >>> a.add(line(""))
      >>> a.delete(0)
      >>> print a.lines
      []
      >>> print a.size
      0
      '''
      if self.size<=index:
         print >> stderr, "Error: Delete out of range"
         return
      if self.size==1:
         self.lines = []
      if index==0:
         self.lines = self.lines[1:]
      elif index==self.size-1:
         self.lines = self.lines[:self.size-1]
      else:
         self.lines = self.lines[0:index]+self.lines[index+1:]
      self.size-=1
      
   def formatTXT(self):
      sum_str = ""
      for l in self.lines:
         sum_str += l.format() + "\n\n"
      return sum_str
      
   def formatHTML(self):
      sum_str = ""
      for i, l in enumerate(self.lines):
         try:
            sum_str += l.formatHTML() + "\n"
         except AttributeError:
            print >> stderr, "Error of spen line %i: Object is not valid" % i
            return l # This is so they can look at the bad object.
      return template % sum_str


if __name__=="__main__":
   main()
   