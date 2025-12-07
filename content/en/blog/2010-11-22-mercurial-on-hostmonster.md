---
title: mercurial on hostmonster
author: gjergj.sheldija
layout: post
permalink: /mercurial-on-hostmonster/
categories:
  - code
  - hosting
  - linux
tags:
  - hostmonster
  - mercurial
comments: true
---
this i quick guide on how to install mercurial on hostmonster. it's made of pieces taken from the net plus some trial and error.

#### update the path settings

update your .bashrc file  
Add or edit this line

```
PATH=$PATH:$HOME/bin:$HOME/packages/mercurial
source ~/.bashrc
```

#### install mercurial

get mercurial and install

```
cd ~
mkdir install_files
mkdir packages
mkdir ~/public_html/hg
mkdir ~/public_html/hg/repos
cd ~/packages
http://mercurial.selenic.com/release/mercurial-1.6.3.tar.gz
tar zxf mercurial-1.6.3.tar.gz
mv mercurial-1.6.3.tar.gz ~/install_files/
mv mercurial* mercurial
cd mercurial
make local
./hg debuginstall
cp ~/packages/mercurial/hgweb.cgi ~/public_html/hg
chmod 755 ~/public_html/hg/hgweb.cgi
```

now inside the hg dir create those files :  
*hgweb.cgi*

```cgi
#!/usr/bin/env python
#
# An example hgweb CGI script, edit as necessary
# See also http://mercurial.selenic.com/wiki/PublishingRepositories

# Path to repo or hgweb config to serve (see 'hg help hgweb')
config = "/full/path/to/your/hgweb.config"

# Uncomment and adjust if Mercurial is not installed system-wide:
import sys; sys.path.insert(, "/full/path/to/your/mercurial")

# Uncomment to send python tracebacks to the browser if an error occurs:
#import cgitb; cgitb.enable()

from mercurial import demandimport; demandimport.enable()
from mercurial.hgweb import hgweb, wsgicgi
application = hgweb(config)
wsgicgi.launch(application)
```

*hgweb.config*

```config
[web]
allowpull=true
style=gitweb
baseurl = /hg

[collections]
/full/path/to/your/repos/directory = /full/path/to/your/repos/directory
```

*.htaccess*

```apache
Options +ExecCGI
RewriteEngine On
# / for root directory; specify a complete path from / for others
RewriteBase /hg
RewriteRule ^$ hgweb.cgi [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule (.*) hgweb.cgi/$1 [QSA,L]
```

#### initialize the mercurial repository

you need to change REPOSITORY to your repository name  
if you want more than one repository, run the command for each of them

```
~/packages/mercurial/hg init REPOSITORY
```

#### create hgrc files for each project


```config
[web]
contact = Gjergj Sheldija
description =Project Description
style = gitweb
allow_push = MYUSERNAME
push_ssl = false
allow_archive = gz zip bz2
```

there are a couple of things that are non standard here :  
first, i used mercurial 1.6.3 and not the last stable version as the client version that comes default with ubuntu is 1.6.3  
second i made all the repositories visible by default, to change this, you need to add those lines to the .htaccess file

```apache
AuthUserFile /etc/hg-basic-auth
AuthName "Please Log In"
AuthType Basic
```

and create a password file for the users  
you need to change the values of HGUSERNAME and PASSWORD to your wanted user name and password

```
cd ~
htpasswd -b -c -d ~/etc/hg-basic-auth HGUSERNAME PASSWORD
```