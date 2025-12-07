---
title: monitorless karmic koala
author: gjergj.sheldija
layout: post
permalink: /monitorless-karmic-koala/
categories:
  - linux
tags:
  - karmic
  - koala
  - ubuntu
comments: true
---
karmic koala and intel i915 chipset don&#8217;t go much well together on monitorless pc&#8217;s, apparently because of this : [431812 ][1]  
besides that, the computer just hangs in an endless loops trying to detect the non present monitor.  
the solution is quite simple &#8211; although i needed 3 hours to figure it out since karmic koala uses the new upstart service management.  
just replace in /etc/init/gdm.conf

```bash
start on (runlevel [3]
          and filesystem
          and started hal
          and tty-device-added KERNEL=tty7
          and (graphics-device-added or stopped udevtrigger))
stop on runlevel [0216]
```

 [1]: https://bugs.launchpad.net/ubuntu/karmic/+source/initramfs-tools/+bug/431812
