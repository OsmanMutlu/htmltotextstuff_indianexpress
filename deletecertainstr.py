import sys
import codecs
import re
import shutil

filename = sys.argv[1]
#These are the starting lines of the comment section
stoplist = ["Tags:","ALSO READ","Please read our before posting comments","TERMS OF USE: The views expressed in comments published on indianexpress.com are those of the comment writer's alone. They do not represent the views or opinions of The Indian Express Group or its staff. Comments are automatically posted live; however, indianexpress.com reserves the right to take it down at any time. We also reserve the right not to publish comments that are abusive, obscene, inflammatory, derogatory or defamatory."]

with codecs.open(filename, "r", "utf-8") as f:
    lines = f.readlines()

for i in range(0,len(lines)):
    if not lines[i]:
        continue
    firstline = lines[i]
    firstline = re.sub(r"\n|\r", r"", firstline)
    if any(firstline == word for word in stoplist):
#We delete the same line because when we delete the item, item index shifts 1 number
        for j in range(i, len(lines)):
            del lines[i]
        break

if not lines or all(len(line)==0 for line in lines):
    print(filename + " is empty!!!!!")
    with open("empty_files","a") as g:
        g.write(filename + "\n")
    shutil.move(filename, "empties/" + filename)

else:
    with codecs.open(filename, "w", "utf-8") as f:
        for line in lines:
            if line:
                line = re.sub(r"\n|\r", r"", line)
                f.write(line + "\n")
