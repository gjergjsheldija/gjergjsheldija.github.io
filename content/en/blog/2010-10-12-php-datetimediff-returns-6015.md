---
title: php DateTime::diff returns 6015
author: gjergj.sheldija
layout: post
permalink: /php-datetimediff-returns-6015/
categories:
  - code
  - php
tags:
  - datetime diff
  - 'php #6015'
  - php 5.3
---
the following code :

```php
$start = new DateTime('2010-06-06');
$end   = new DateTime('2011-02-04');
echo $start->diff($end)->days;
$start = new DateTime('2005-01-01');
echo $start->diff($end)->days;
```

will always return 6015 on windows platforms no matter on the date values. it is a bug regarding php 5.3.x on windows platforms <a href="http://bugs.php.net/bug.php?id=51184" target="_blank">#51184 </a>and <a href="http://bugs.php.net/49778" target="_blank">#49778</a>. the solution to this is  
to use the following code :

```php
function dateDiff($dt1, $dt2, $timeZone = 'GMT') {
  $tZone = new DateTimeZone($timeZone);
  $dt1 = new DateTime($dt1, $tZone);
  $dt2 = new DateTime($dt2, $tZone);
  $ts1 = $dt1->format('Y-m-d');
  $ts2 = $dt2->format('Y-m-d');
  $diff = abs(strtotime($ts1)-strtotime($ts2));
  $diff/= 3600*24;
  return $diff;
}
```

echo dateDiff(&#8217;2010-10-10&#8242;, &#8217;2010-10-12&#8242;);

hope it helps
