---
title: download from rapidshare using aria
author: gjergj.sheldija
layout: post
permalink: /download-from-rapidshare-using-aria/
categories:
  - random
tags:
  - aria
  - download
  - rapidshare
---
supposing you&#8217;ve saved all your rapidshare links in a file called links.txt the command line is :

```bash
aria2c --http-user=username --http-password=password -i links.txt -j2 -s4 -c > /tmp/aria2c.log 2>&1 &
```