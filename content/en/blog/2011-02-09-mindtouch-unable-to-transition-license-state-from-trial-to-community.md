---
title: 'mindtouch :  Unable to transition license state <br/> from TRIAL to COMMUNITY'
author: gjergj.sheldija
layout: post
permalink: /mindtouch-unable-to-transition-license-state-from-trial-to-community/
categories:
  - random
tags:
  - community
  - mindtouch
  - trial
---

the new version of mindtouch ( 10.x ) does not permit to change the license from Trial to Core, the community version.  
luckily the solution is very simple, you need to move the old license to somewhere else.  
to do so, locate the old license file, usually under **/var/www/dekiwiki/bin/\_deki/license.xml** and **/var/www/dekiwiki/bin/\_deki/default/license.xml** to your home directory, and then restart the Mindtouch API. here it, now you can use your community license
