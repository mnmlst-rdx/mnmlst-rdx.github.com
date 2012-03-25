from bs4 import BeautifulSoup

import os
import sys


for r,d,f in os.walk("/Users/christopherkinniburgh/mnmlst-redux/mnmlist.com copy"):
  for files in f:
      newfile = os.path.join(r,files)
      reload(sys)
      sys.setdefaultencoding('utf-8')
      f = open(newfile, "r")
      old = f.read()
      soup = BeautifulSoup(old)
      for t in soup.findAll(text=True):
        text = unicode(t)
        for vowel in u'aeiou':
          text = text.replace(vowel, u'') 
        t.replaceWith(text)
      print newfile
      f.close()
      f = open(newfile, "w")
      f.write(soup.prettify())
      f.close()