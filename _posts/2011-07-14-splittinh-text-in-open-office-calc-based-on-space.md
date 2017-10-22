---
title: splitting text in open office calc based on space
author: gjergj.sheldija
layout: post
permalink: /splittinh-text-in-open-office-calc-based-on-space/
categories:
  - code
  - random
tags:
  - calc
  - openoffice
comments: true
---
paste them in different columns

{% codeblock %}
=LEFT(D2,FIND(” ”,D2))
=MID(D2,FIND(” ”,E2),255) 
{% endcodeblock %}
