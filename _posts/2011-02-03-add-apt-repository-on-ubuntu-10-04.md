---
title: add-apt-repository on ubuntu 10.04
author: gjergj.sheldija
layout: post
permalink: /add-apt-repository-on-ubuntu-10-04/
categories:
  - ubuntu
tags:
  - ubuntu add-apt-repository lucid
comments: true
---
in you're playing around with ubuntu 10.04 and you get something like : sudo add-apt-repository .. 
you can quickly fix it by :

{% codeblock lang:bash %}
sudo apt-get install python-software-properties
{% endcodeblock%} 
