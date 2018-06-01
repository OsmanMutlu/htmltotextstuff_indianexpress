#!/bin/sh
#Takes a full path of the html_dir without slash / charachter at the end
HTML_DIR=$1
cd $HTML_DIR
if [ ! -d ../random_goose_newstext ]; then
 mkdir ../random_goose_newstext
 mkdir ../random_goose_newstext/empties
fi
for file in http*
do
 if [ ! -f ../random_goose_newstext/$file ]; then
#  tmp=$(echo "${file%.cms}.txt")
  python /ai/work/emw/htmltotextstuff_indianexpress/goose_gettext.py $file
  python3 /ai/work/emw/htmltotextstuff_indianexpress/deletecertainstr.py ../random_goose_newstext/$file
  python3 /ai/work/emw/htmltotextstuff_indianexpress/addnewstime.py ../random_goose_newstext/$file
  python3 /ai/work/emw/htmltotextstuff_indianexpress/addnewslink.py ../random_goose_newstext/$file
  echo "Finished $file"
 fi
done
exit 0
