#!/bin/python

'''
%ANN'S MOM
(Yelling from the other room
"Come get dinner sweety!
%ANN
(Yelling back
"I'm not hungry I ate on my way back from school like I always do. Save me some for later.
%ANN'S MOM
"What sweety? Woof!
'''

def main():
   test = spen()
   test.add(slug(1, "ANN'S HOUSE", "DAY (NOON)"))
   test.add(action("Ann lays in her room reading a book. And woofs around a whole bunch like crazy woofing."))
   test.add(dialog("ANN'S MOM", "Yelling from the other room", "Come get dinner sweety!"))
   print test.formatTXT()

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

# Action line      
class action(line):
   def format(self):
      return line._set_margin(self,self.content,17,74)

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

# Main class      
class spen(object):
   def __init__(self):
      self.lines = []
      
   def add(self, new_line):
      self.lines.append(new_line)
      
   def formatTXT(self):
      sum_str = ""
      for l in self.lines:
         sum_str += l.format() + "\n\n"
      return sum_str


if __name__=="__main__":
   main()
   