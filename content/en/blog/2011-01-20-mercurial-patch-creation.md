---
title: mercurial patch creation
author: gjergj.sheldija
layout: post
permalink: /mercurial-patch-creation/
categories:
  - code
  - mercurial
  - ubuntu
tags:
  - mercurial patch diff generation
comments: true
---
some days ago i had the need to generate a patch for a project i had on hosted on mercurial. the problem was that the user that would do the update was not able to apply a diff patch, nor wanted to know about it. the ideal solution for him was to just send him a zipped file for him to extract and copy paste over the existing files. 
after some long searches on google i wasn&#8217;t able to find anything..so, armed with my bash newbie skills i came up with the following code

```bash
#!/bin/bash

if [ $# -lt 3 ] ; then
cat <<HELP
create-changeset -- creates a tar.gz file with the changed files
USAGE: create-changeset 'repository-path' 'revision-from' 'revision-to'
EXAMPLE: create-changeset /var/www/survey 4 5

HELP
  exit 0
fi


mkdir /tmp/project

## changed files
cd $1

for changed_files in `hg log --rev $2:$3 --template '{files}\n'`
do
    cp --parents $changed_files /tmp/project
done


## list of removed files
hg log --rev $2:$3 --template '{files_dels}\n' > removed_files.txt
mv removed_files.txt /tmp/project

## changelog
hg log --rev $2:$3 --style changelog > changelog
mv changelog /tmp/project

cd /tmp/project
tar -czf changes.$2-$3.tar.gz *
mv changes.$2-$3.tar.gz $1
rm -rf /tmp/project
```

the usage is quite simple, just execute it like

```bash
create-changeset full-path-to-repository version-from version-to
```

the result will be a tar.gz compressed file in the repository directory containing a file listing the removed files, a changelog file and your modified files.  
you can download it here : [create-changesets.tar.gzr][1]  
hope it helps

 [1]: http://acme-tech.net/blog/http://acme-tech.net/blog/wp-content/uploads/2011/01/create-changesets.sh.tar.gz
