---
title: fixing the java console on ubuntu with firefox
author: gjergj.sheldija
layout: post
permalink: /fixing-the-java-console-on-ubuntu-with-firefox/
categories:
  - java
  - ubuntu
tags:
  - applet
  - console
  - firefox
  - java
  - ubuntu
comments: true
---
ubuntu comes with icedtea / openjdk as the default java vm. this crewates some errors loading certain applets. the simple solution to fix that is to remove the icedtea plugin package and install the sun plugin package :

```bash
sudo apt-get remove icedtea6-plugin
sudo apt-get install sun-java6-plugin
```

now open firefox and open about:plugins to check that everything is ok.  
in certain cases you may also need to do :

```bash
sudo update-alternatives --config java
```