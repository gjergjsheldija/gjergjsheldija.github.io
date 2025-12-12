---
title: bazaar and loggerhead a ( very ) quick guide
author: gjergj.sheldija
layout: post
permalink: /bazaar-and-loggerhead-a-very-quick-guide/
categories:
  - code
  - linux
tags:
  - bazaar
  - loggerhead
  - ubuntu
---

### bazaar

first add the bazaar PPA to the repository list

```bash
vi /etc/apt/sources.list.d/bzr.list
```

add the following

```bash
# Bazaar PPA
deb http://ppa.launchpad.net/bzr/ubuntu hardy main
deb-src http://ppa.launchpad.net/bzr/ubuntu hardy main
aptitude update
```

### bazaar server

```bash
aptitude install bzr bzrtools python-paramiko
```

### sftp

```bash
aptitude install ssh openssh-server
```

create the user account

```bash
useradd --create-home --home-dir /var/local/bzr --shell /usr/lib/sftp-server bzr
passwd bzr
echo '/usr/lib/sftp-server' &gt;&gt; /etc/shells
```

### Loggerhead

i decided to use Loggerhead instead of an apache or lighttpd integratrion so..

```bash
aptitude install python-configobj python-simpletal python-paste python-pastedeploy python-simplejson
bzr branch lp:loggerhead
wget http://launchpad.net/loggerhead/1.17/1.17/+download/loggerhead-1.17.tar.gz
tar zxvf loggerhead-1.17.tar.gz
python setup.py install
/usr/bin/serve-branches /var/local/bzr/
```

### starting and stopping loggerhead

```bash
nano /etc/loggerhead.conf
# use this if you're mapping loggerhead within apache via proxy
# server.webpath = 'http://code.example.org/Loggerhead/'
# the access and debug logs can be set up to roll 'daily', 'weekly', or 'never':
log.roll = 'daily'
# here's an example of an auto-published folder:

[bazaar]
name = 'My Bazaar'
auto_publish_folder = '/var/local/bzr/'
loggerhead can be started and stopped via
/etc/init.d/loggerhead start
/etc/init.d/loggerhead stop
loggerhead searching
mkdir -p ~/.bazaar/plugins
bzr branch lp:bzr-search ~/.bazaar/plugins/search
bzr index /var/local/bzr/Project1
/etc/init.d/loggerhead restart
```
