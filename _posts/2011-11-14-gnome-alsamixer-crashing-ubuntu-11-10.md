---
title: gnome alsamixer crashing in ubuntu 11.10
author: gjergj.sheldija
layout: post
permalink: /gnome-alsamixer-crashing-ubuntu-11-10/
categories:
  - gnome 3
  - ubuntu
tags:
  - crash
  - gnome 3
  - gnome-alsamixer
  - gnome-shell
  - libgtk-x11-2.0.so.0
  - ubuntu 11.10
comments: true
---
there is a strange bug with gnome alsamixer on ubuntu 11.10 using gnome-shell.. 
the solution is quite simple..
```bash
wget http://launchpadlibrarian.net/83939881/gnome-alsamixer_0.9.7%7Ecvs.20060916.ds.1-2.1ubuntu1_amd64.deb
sudo dpkg -i gnome-alsamixer_0.9.7%7Ecvs.20060916.ds.1-2.1ubuntu1_amd64.deb
```
