---
title: get duplicate lines working in ubuntu
author: gjergj.sheldija
layout: post
permalink: /get-duplicate-lines-working-in-ubuntu/
categories:
  - ubuntu
tags:
  - eclipse
  - ubuntu
---
the default keyboard shortcut for duplicating lines (alt + ctrl + up/down) does not work. this is caused by the system using the same shortcuts to move to a virtual workspace above and below. go to system > preferences > keyboard shortcuts and assign a different key combo for the following two actions: switch to workspace up switch to workspace down duplicate lines works again.
