---
title: enabling background on gnome 3
author: gjergj.sheldija
layout: post
permalink: /enabling-background-on-gnome-3/
categories:
  - gnome 3
  - linux
tags:
  - background
  - gnome 3
  - linux
  - ubuntu 11.10
comments: true
---
having some problems with changing the background on gnome 3 after playing a bit with themes.
luckily the solution was quite simple 

{% codeblock lang:bash %}
$ gsettings set org.gnome.desktop.background draw-background true
{% endcodeblock %}
and that should fix birt preview

