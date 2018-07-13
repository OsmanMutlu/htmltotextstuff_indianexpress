import sys
import codecs
import re
import lxml.html
from fuzzywuzzy import fuzz
from dask import dataframe as dd
from dask.multiprocessing import get
import pandas as pd
from glob import glob

html_dir = sys.argv[1]

files = glob("http*")

all_df = pd.DataFrame(files, columns=["filename"])

all_df["asd"] = ""

def clean(row):

    try:
        with codecs.open(row.filename, "r", "utf-8") as f:
            lines = f.readlines()
    except IOError:
        sys.exit()

    with open(html_dir + row.filename, "rb") as g:
        html_file = g.read()

    for line in lines:
        line = re.sub(r"\n|\r", r"", line)

    doc = lxml.html.document_fromstring(html_file)
    title = str(doc.xpath("//title/text()"))
    time = str(doc.xpath("//div[@class='story-date']/text()"))

    if time is None:
        time = str(doc.xpath("//div[@class='posted'/strong[last()]/text()"))
        if time is None:
            time = ""
            with codecs.open("NoTime", "a", "utf-8") as g:
                g.write(row.filename + "\n")

# Because place names come up with it. We don't want that for now.
#    lines.insert(0,time)

    if title:
        title = re.sub(r"\n|\r", r"", title)
        lines.insert(0,title)


    with codecs.open(row.filename, "w", "utf-8") as f:
        for line in lines:
            if line:
                line = re.sub(r"\n|\r", r"", line)
                f.write(line + "\n")

    return row

all_df = dd.from_pandas(all_df,npartitions=8).map_partitions(lambda df : df.apply(clean, axis=1),meta=all_df).compute(get=get)
#all_df = all_df.apply(clean, axis=1)
