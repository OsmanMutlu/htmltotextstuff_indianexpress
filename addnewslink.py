import codecs
import re
from glob import glob
import pandas as pd
from dask import dataframe as dd
from dask.multiprocessing import get

#Adding the news link to the end of file

files = glob("http*")

all_df = pd.DataFrame(files, columns=["filename"])

all_df["asd"] = ""

def clean(row):

    try:
        with codecs.open(row.filename, "r", "utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        sys.exit()

    link = re.sub(r"___", r"://", row.filename)

    link = re.sub(r"_", r"/", link)
    lines.append("url : " + link)

    with codecs.open(row.filename, "w", "utf-8") as f:
        for line in lines:
            line = re.sub(r"\n|\r", r"", line)
            f.write(line + "\n")

    return row

all_df = dd.from_pandas(all_df,npartitions=8).map_partitions(lambda df : df.apply(clean, axis=1),meta=all_df).compute(get=get)
