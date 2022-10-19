#!/bin/bash

FOLDER=/tmp
REGEX_PATERN=".Data_.*"

for f in $(find $FOLDER -name "*.txt")
do 
  newname=$(echo "$f" | sed -r "s/$REGEX/.Data_.$(date '+%Y_%m_%d').txt/g")
  mv "$f" "$newname"
done
