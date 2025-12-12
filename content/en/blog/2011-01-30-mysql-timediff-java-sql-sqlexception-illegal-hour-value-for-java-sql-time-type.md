---
title: 'MySQL : TIMEDIFF(  ) : java.sql.SQLException : <br/> Illegal hour value for java.sql.Time type'
author: gjergj.sheldija
layout: post
permalink: /mysql-timediff-java-sql-sqlexception-illegal-hour-value-for-java-sql-time-type/
categories:
  - code
  - java
tags:
  - java mysql
---
MySQL's TIMEDIFF runs well on MySQl Shell but is an sql exception when using with JDBC. 
the problem is that the TIMEDIFF(expr1,expr2) function returns returns expr1 – expr2 expressed as a time value. this value is handled by java.sql.Time. but TIMEDIFF( , ) may return (for example) 12:27:58 or 48:30:58 as the case may be. For first value it works but for the second value it is not a proper time value according to java.sql.Time, hence the exception.

a workaround of this problem is to convert this query to return a string, like :

```mysql
CONCAT('',TIMEDIFF(expr1,expr2))
```

then the returned value will be a string instead of a time value and JDBC will not parse it.
