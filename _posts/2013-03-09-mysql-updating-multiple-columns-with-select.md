---
title: 'mysql: updating multiple columns with select'
author: gjergj.sheldija
layout: post
permalink: /mysql-updating-multiple-columns-with-select/
categories:
  - code
  - sql
tags:
  - mysql
  - sql
comments: true
---
sometimes even the simples of the things becomes..hard.  
one of those things is updating multimple columns in mysql.  
the standard should be something as easy as :

{% codeblock lang:mysql %}
UPDATE
    table1
SET
    table1.col1 = table2.x,
    table1.col2 = table2.y
FROM
    table1
INNER JOIN
    table2
ON
    table1.CommonColumn = table2.CommonColumn 
{% endcodeblock %}

instead mysql has a quirk that can be used, [USING()](http://dev.mysql.com/doc/refman/5.0/en/join.html)</a>. 
so the whole thing becomes something like

{% codeblock lang:mysql %}
UPDATE
    table1 INNER JOIN table2 USING (CommonColumn)
SET
    table1.col1 = table2.x,
    table1.col2 = table2.y 
{% endcodeblock %}
