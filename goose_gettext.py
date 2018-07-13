import re
import codecs
from goose import Goose
from glob import glob
import pandas as pd
from dask import dataframe as dd
from dask.multiprocessing import get
import sys
import os.path

path = sys.argv[1]

files = glob("http*")

all_df = pd.DataFrame(files,columns=["filename"])

def getText(row):

    with open(row.filename, "rb") as f:
        data = f.read()

    if os.path.isfile(path + row.filename):
        return row

    g = Goose()
    article = g.extract(raw_html=data)

    with codecs.open(path + row.filename, "w", "utf-8") as g:
        g.write(article.cleaned_text)

    #print("Finished : " + row.filename)

    return row

all_df = dd.from_pandas(all_df,npartitions=8).map_partitions(lambda df : df.apply(getText,axis=1),meta=all_df).compute(get=get)
