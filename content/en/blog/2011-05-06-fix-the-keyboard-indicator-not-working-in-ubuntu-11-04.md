---
title: fix the keyboard indicator not working in ubuntu 11.04
author: gjergj.sheldija
layout: post
permalink: /fix-the-keyboard-indicator-not-working-in-ubuntu-11-04/
categories:
  - ubuntu
tags:
  - ubuntu keyboard gnome Natty Narwhal
---
in gconf-editor, check **/desktop/gnome/peripherals/keyboard/indicator/showFlags**

install set of flags using 
```bash
sudo apt-get install famfamfam-flag-png
```

make a softlink: 
```bash
ln -s /usr/share/flags/countries/16&#215;11 ~/.icons/flags
```
