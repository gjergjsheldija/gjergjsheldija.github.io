---
title: pentaho fails to refresh cache
author: gjergj.sheldija
layout: post
permalink: /pentaho-fails-to-refresh-cache/
categories:
  - code
  - java
tags:
  - duplicate entry
  - fullPath
  - pentaho
  - pro_files
comments: true
---
after inserting some new reports in pentaho and trying to refresh it started giving some strange errors like : Cache refresh failed. 
after some digging around the logs in tomcat/bin/pentaho.log. it turned out that it was a duplicate entry in the fullPath field of the PRO_FILES table. the solution, which is pretty simple, is to change the collate of the field from latin1_swedish_ci to latin1_general_cs.
