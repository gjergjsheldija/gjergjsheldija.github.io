---
title: mikrotik 3.x crashed after hotspot login
author: gjergj.sheldija
layout: post
permalink: /mikrotik-3-x-crashed-after-hotspot-login/
categories:
  - random
tags:
  - crash
  - hotspot
  - mikrotik
  - mikrotik 3.20
  - mikrotik 3.22
---
all mikrotik version 3.x have a strange bug, when a user logs in via the hotspot the processor goes 100%.
the solution is to disable the address pool in the user profile, and set it to none.
