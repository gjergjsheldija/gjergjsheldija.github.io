---
title: mercurial server on ubuntu jaunty
author: gjergj.sheldija
layout: post
permalink: /mercurial-server-on-ubuntu-jaunty/
categories:
  - code
  - mercurial
tags:
  - hg
  - jaunty
  - mercurial
  - server
  - ubuntu
---
this is a short howto on how to install a mercurial server on a ubuntu jaunty and maybe lynx.

first of all we install mercurial and the wsgi mod for apache

```bash
sudo apt-get install mercurial libapache2-mod-wsgi
```

second we create a directory where we want to store our mercurial source code and copy the defualt config files from the mercurial dir

```bash
sudo mkdir /data/mercurial
cd /data/mercurial
mv /usr/share/doc/mercurial/examples/hgwebdir.wsgi /data/mercurial/hgwebdir.cgi
```

under /etc/apache/sites-enabled/ edit file 000-default and add the following line

```apache
ScriptAlias /hg "/data/mercurial/hgwebdir.cgi"
```

change the default access to www-data for all the files inside /data/mercurial and that&#8217;s it, you can start creating and accessing mercurial repos

if you receive an error like ssq_required, you should create a file named hgrc inside the .hg directory of your project and add the following lines

```bash
[web]
push_ssl = false
```
