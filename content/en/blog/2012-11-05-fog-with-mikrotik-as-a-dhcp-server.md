---
title: fog with mikrotik as a dhcp server
author: gjergj.sheldija
layout: post
permalink: /fog-with-mikrotik-as-a-dhcp-server/
categories:
  - linux
  - ubuntu
tags:
  - dhcp
  - fog
  - mikrotik
  - mikrotik 3.22
  - tftp
---
having mikrotik 3.x give the correct tftp ip to the client can be a bit of a pain.
after some hacking, googling and good luck, finally was able to do it.
and it was not what the manual or helps int he forums say.
you need to go to the terminal and issue the following commands :

```bash
/ip dhcp-server network set 0 boot-file-name=undionly.kkpxe next-server=10.10.0.2
```

and, they are not going to show in the network properties and neither the console..
