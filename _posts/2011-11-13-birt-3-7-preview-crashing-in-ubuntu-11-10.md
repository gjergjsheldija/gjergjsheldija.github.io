---
title: birt 3.7 preview crashing in ubuntu 11.10
author: gjergj.sheldija
layout: post
permalink: /birt-3-7-preview-crashing-in-ubuntu-11-10/
categories:
  - code
  - java
  - ubuntu
tags:
  - birt
  - java
  - ubuntu
comments: true
---
if you have problems with birt 3.7 preview crashing and recieve this sort of output on ubuntu 11.10 :

{% codeblock lang:bash %}
 No bp log location saved, using default.
 [000:000] Browser XEmbed support present: 1
 [000:000] Browser toolkit is Gtk2.
 [000:000] Using Gtk2 toolkit
 [000:021] Warning(optionsfile.cc:23): Load: Could not open file, err=2
 [000:021] No bp log location saved, using default.
 [000:021] Browser XEmbed support present: 1
 [000:021] Browser toolkit is Gtk2.
 [000:021] Using Gtk2 toolkit
 (Eclipse:13610): GnomeShellBrowserPlugin-DEBUG: plugin loaded
 ** (Eclipse:13610): DEBUG: NP_Initialize
 ** (Eclipse:13610): DEBUG: NP<em>Initialize succeeded
 ** (Eclipse:13610): DEBUG: NP</em>Initialize
 ** (Eclipse:13610): DEBUG: NP_Initialize succeeded
 ** (Eclipse:13610): DEBUG: NP<em>Initialize
 ** (Eclipse:13610): DEBUG: NP</em>Initialize succeeded
 ** (Eclipse:13610): DEBUG: NP_Initialize
 ** (Eclipse:13610): DEBUG: NP_Initialize succeeded
{% endcodeblock %}

there is a two step solution to fix that, first you have to install xulrunner which not available on ubuntu repos anymore. so you have to download
here [xulrunner](http://bit.ly/veR5YO) and install the xulrunner deb.  
second step is to change the birt menu entry and add the the following line :

{% codeblock lang:bash %}
./eclipse -vmargs -Dorg.eclipse.swt.browser.DefaultType=mozilla
{% endcodeblock %}
and that should fix birt preview
