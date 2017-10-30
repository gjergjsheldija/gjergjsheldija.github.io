---
title: var_dump() for java
author: gjergj.sheldija
layout: post
permalink: /var_dump-for-java/
categories:
  - code
  - java
  - php
tags:
  - java
  - var_dump
comments: true
---
quick tip for java,

```java
import java.lang.reflect.*;
....
//o Object..
Field[] fields = o.getClass().getDeclaredFields();
for (int i=; i<fields.length; i++) {
    try {
        System.out.println(fields[i].getName() + " - " + fields[i].get(o));
    } catch (java.lang.IllegalAccessException e) {
        System.out.println(e); 
    }
}
```