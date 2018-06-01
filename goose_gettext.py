#from bs4 import BeautifulSoup
import re
import sys
import codecs
from goose import Goose

filename=sys.argv[1]

# This is the path that will contain texts
path = "../random_goose_newstext/"

with open(filename, "rb") as g:
    html = g.read()

g = Goose()
article = g.extract(raw_html=html)

with codecs.open(path + filename, "a", "utf-8") as f:
    f.write(article.cleaned_text)

print("Finished " + filename)
