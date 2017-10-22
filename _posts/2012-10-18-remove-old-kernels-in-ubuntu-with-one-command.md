---
title: remove old kernels in ubuntu with one command
author: gjergj.sheldija
layout: post
permalink: /remove-old-kernels-in-ubuntu-with-one-command/
categories:
  - linux
  - ubuntu
tags:
  - kernel
  - old
  - remove
comments: true
---
{% codeblock lang:bash %}
dpkg -l linux-* | awk '/^ii/{ print $2}' | grep -v -e `uname -r | cut -f1,2 -d"-"` | grep -e [0-9] | xargs sudo apt-get -y purge
{% endcodeblock %}

