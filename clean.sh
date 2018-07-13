#!/bin/sh
#Takes a full path of the html_dir without slash / charachter at the end
#Text_dir can be relative to html_dir. It is given without slash / character at the end
HTML_DIR=$1
TEXT_DIR=$2
cd $HTML_DIR
if [ ! -d ../$TEXT_DIR ]; then
 mkdir $TEXT_DIR
 mkdir $TEXT_DIR/empties
fi

#python /scratch/users/omutlu/htmltotextstuff_indianexpress/goose_gettext.py $TEXT_DIR/
#echo "Finished boilerplate removal"
cd $TEXT_DIR
python3 /scratch/users/omutlu/htmltotextstuff_indianexpress/deletecertainstr.py
echo "Finished Deleting"
python3 /scratch/users/omutlu/htmltotextstuff_indianexpress/addnewstime.py $HTML_DIR/
echo "Finished Adding place and title"
python3 /scratch/users/omutlu/htmltotextstuff_indianexpress/addnewslink.py
exit 0
