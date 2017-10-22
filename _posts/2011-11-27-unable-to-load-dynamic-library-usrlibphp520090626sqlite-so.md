---
title: 'Unable to load dynamic library &#8216;/usr/lib/php5/20090626/sqlite.so&#8217;'
author: gjergj.sheldija
layout: post
permalink: /unable-to-load-dynamic-library-usrlibphp520090626sqlite-so/
categories:
  - code
  - linux
  - php
  - ubuntu
tags:
  - php sqlite error 20090626 sqlite.so
comments: true
---
if you happen to have this error with php 5 on ubuntu 11.10

PHP Warning: PHP Startup: Unable to load dynamic library /usr/lib/php5/20090626/sqlite.so - /usr/lib/php5/20090626/sqlite.so: cannot open shared object file: No such file or directory in Unknown on line 0.
This has occurred because sqlite support was removed, in favour of pure sqlite3. It seems that a config file was left in place. 
to fix it, just :

{% codeblock lang:bash %}
sudo rm /etc/php5/conf.d/sqlite.ini
{% endcodeblock %}
