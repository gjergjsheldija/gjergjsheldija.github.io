---
title: utf-8 with php and mysql
author: gjergj.sheldija
layout: post
permalink: /utf-8-with-php-and-mysql/
categories:
  - code
  - php
  - random
tags:
  - csv
  - import
  - php
  - utf-8
  - utf8
comments: true
---
quick guide on how to use utf-8 encoding with php and mysql.
first check that character set is set to utf-8 and that collation is set to utf8\_general\_ci.
then, add the following :

```mysql
mysql_query('SET character_set_results=utf8');
mysql_query('SET names=utf8');  
mysql_query('SET character_set_client=utf8');
mysql_query('SET character_set_connection=utf8');   
mysql_query('SET character_set_results=utf8');   
mysql_query('SET collation_connection=utf8_general_ci');
```
