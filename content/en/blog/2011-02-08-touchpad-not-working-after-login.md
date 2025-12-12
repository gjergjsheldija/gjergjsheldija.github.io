---
title: touchpad not working after login
author: gjergj.sheldija
layout: post
permalink: /touchpad-not-working-after-login/
categories:
  - linux
  - ubuntu
tags:
  - login
  - touchpad
  - ubuntu
---
usually happens when you disable your touchpad and then suspend your computer. to fix this just run this command:

```bash
gconftool-2 --set --type boolean /desktop/gnome/peripherals/touchpad/touchpad_enabled true
```
