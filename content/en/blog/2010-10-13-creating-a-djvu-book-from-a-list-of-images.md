---
title: creating a djvu book from a list of images
author: gjergj.sheldija
layout: post
permalink: /creating-a-djvu-book-from-a-list-of-images/
categories:
  - ubuntu
tags:
  - conversion
  - djvu
  - img
  - script
  - ubuntu
---
i had the need to convert some images ( 2600 ) separated into folder into books. each one titled as the containing folder.

after installing the djvu libre tools under linux i resolved everything with this small script

```bash
find * -type d | while read DIRNAME
do
echo " "
echo "ENTERING  : $DIRNAME"
echo "=========================================================================="
echo " "

cd  $DIRNAME

for file in $(ls *.jpg | sort -n); do
echo "converting  : $file";
c44 $file;
done

echo "creating book file : $DIRNAME.djvu"
djvm -c $DIRNAME.djvu $(ls *.djvu | sort -n)
echo "done."
cd ..
done
```

as a short notice the ls * | sort -n is for sorting images correctly.

you need also to replace spaces in directory and path names, to do so you can use this script :

```bash
#!/bin/bash

ls | while read -r FILE
do
    mv -v "$FILE" `echo $FILE | tr ' ' '_' | tr -d '[{}(),\!]' | tr -d "\'" | tr '[A-Z]' '[a-z]' | sed 's/_-_/_/g'`
done
```
