import sys
import codecs
import re
import lxml.html
#from bs4 import BeautifulSoup

filename = sys.argv[1]

try:
    with codecs.open(filename, "r", "utf-8") as f:
        lines = f.readlines()
except IOError:
    sys.exit()

text_path = re.sub(r"(.*\/)[^\/]*$", r"\g<1>", filename)

hfilename = re.sub(r".*\/([^\/]*)$", r"\g<1>", filename)
hfilename = re.sub(r"\.txt$", r".cms", hfilename)

with codecs.open(hfilename, "rb", "utf-8") as g:
    html_file = g.read()

for line in lines:
    line = re.sub(r"\n|\r", r"", line)

doc = lxml.html.document_fromstring(html_file)
title = doc.xpath("//title/text()")
time = doc.xpath("//div[@class='story-date']/text()")

if time is None:
    time = doc.xpath("//div[@class='posted'/strong[last()]/text()")
    if time is None:
        time = ""
        with codecs.open("NoTime", "a", "utf-8") as g:
            g.write(filename + "\n")

title = re.sub(r"\n|\r", r"", title)

lines.insert(0,time)
lines.insert(0,title)


with codecs.open(filename, "w", "utf-8") as f:
    for line in lines:
        if line:
            line = re.sub(r"\n|\r", r"", line)
            f.write(line + "\n")
