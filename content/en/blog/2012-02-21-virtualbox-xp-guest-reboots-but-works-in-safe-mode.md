---
title: 'virtualbox XP guest reboots <br />but works in safe mode'
author: gjergj.sheldija
layout: post
permalink: /virtualbox-xp-guest-reboots-but-works-in-safe-mode/
categories:
  - random
tags:
  - guest
  - reboot
  - virtualbox
  - xp
---
just change the 'Start' value of reg HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\intelppm start to 4
