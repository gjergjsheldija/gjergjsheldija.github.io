---
title: quick svn + trac
author: gjergj.sheldija
layout: post
permalink: /quick-svn-trac/
categories:
  - code
tags:
  - install
  - linux
  - svn
  - trac
  - ubuntu
comments: true
---
```bash
svn import -m "First import to SVN" /import/from/here/project file:///var/svn/repos/project/trunk
sudo trac-admin /var/trac/sites/testProject initenv
sudo chown -R www-data /var/trac/sites/testProject
```
