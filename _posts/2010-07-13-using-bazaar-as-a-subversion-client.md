---
title: using bazaar as a subversion client
author: gjergj.sheldija
layout: post
permalink: /using-bazaar-as-a-subversion-client/
categories:
  - bazaar
  - code
  - php
  - svn
tags:
  - bazaar
  - bzr
  - client
  - guide
  - subversion
  - svn
comments: true
---
a quick sample based guide on using bazaar as a svn client..

```bash
bzr init-repo gettext
bzr checkout https://....
bzr branch gettext development
```

after you have some changes to submit..

```bash
cd gettext
bzr merge ../development
bzr commit -m 'testing bzr-svn'
```
