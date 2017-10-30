---
title: Distributing PHP-GTK Applications on Windows
author: admin
layout: post
permalink: /distributing-php-gtk-applications-on-windows/
categories:
  - code
tags:
  - gtk
  - php
comments: true
---
php-gtk is a php extension that uses the GTK (GIMP Tool Kit) to let developers build cool GUI apps which run on Linux, Windows, MacOS, BeOS and other platforms. I am currently studying the curves of building GUI software with php-gtk. It was going on fine. But the first problem I faced while distributing my php-gtk apps is that I need to port php, gtk and some other dependencies on the clients machine. I was searching on the internet if I can find a good solution to this problem. Luckily, I found one.

The package contains a tool kit for deploying php-gtk apps on windows. Download and unzip the package. Then modify and compile the NSIS script that comes in with the package to build a installation package for your own app.

Download Link:  
<a href="http://www.dreadsoft.org/php-gtk/pgsk.zip" target="_blank">http://www.dreadsoft.org/php-gtk/pgsk.zip</a>

This package requires the NSIS, get it from here :

Download Link:  
<a href="http://nsis.sourceforge.net" target="_blank">http://nsis.sourceforge.net</a>
