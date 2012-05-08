#!/bin/python

def main():
   test = spen()
   test.add(action("Woof"))
   print test.formatTXT()

# Generic line
class line(object):
   def __init__(self, content):
      self.content = content
      
   def _set_margin(str,start,end):
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
   pass

# Action line      
class action(line):
   pass

# Dialog line      
class dialog(line):
   pass

# Main class      
class spen(object):
   def __init__(self):
      self.lines = []
      
   def add(self, new_line):
      self.lines.append(new_line)
      
   def formatTXT(self):
      sum_str = ""
      for l in self.lines:
         sum_str += l.content
      return sum_str


if __name__=="__main__":
   main()
   