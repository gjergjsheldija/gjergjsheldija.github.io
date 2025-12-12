---
title: 'webcam cam on dell xmp m1530<br/> and ubuntu 10.10'
author: gjergj.sheldija
layout: post
permalink: /webcam-cam-on-dell-xmp-m1530-and-ubuntu-10-10/
categories:
  - linux
  - ubuntu
tags:
  - cam
  - dell m1530
  - ubuntu 10.10
  - webcam
---
quick fix how to enable the integrated webcam on a dell xps m1530 on ubuntu 10.10 to work with skype and ekiga. first do a

```bash
sudo modprobe uvcvideo
```


if it works ok, then add it as a line in /etc/modules with

```bash
sudo gedit /etc/modules
```

restart and it&#8217;s done.
