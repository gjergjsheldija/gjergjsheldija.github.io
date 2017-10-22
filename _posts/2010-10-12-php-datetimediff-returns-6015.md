---
title: php DateTime::diff returns 6015
author: gjergj.sheldija
layout: post
permalink: /php-datetimediff-returns-6015/
st_cached:
  - |
    <ul class="socialize-this"><li><!-- AddThis Button BEGIN -->
    <div class="addthis_toolbox addthis_default_style">
    <a href="http://www.addthis.com/bookmark.php?v=250&amp;username=xa-4ca3f7522e6e7fdb" class="addthis_button_compact">Share</a>
    <span class="addthis_separator">|</span>
    <a class="addthis_button_preferred_1"></a>
    <a class="addthis_button_preferred_2"></a>
    <a class="addthis_button_preferred_3"></a>
    <a class="addthis_button_preferred_4"></a>
    </div>
    <script type="text/javascript" src="http://s7.addthis.com/js/250/addthis_widget.js#username=xa-4ca3f7522e6e7fdb"></script>
    <!-- AddThis Button END -->
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/php-datetimediff-returns-6015/"></g:plusone></li></ul>
st_cached_time:
  - 1355875131
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/2710417996";s:9:"url_count";i:2;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 2
st_last_socialized:
  - 1392370357
st_tiny_url:
  - http://acme-tech.net/blog/php-datetimediff-returns-6015/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
  - php
tags:
  - datetime diff
  - 'php #6015'
  - php 5.3
comments: true
---
the following code :

<div class="codecolorer-container php geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />
        </div>
      </td>
      
      <td>
        <div class="php codecolorer" style="white-space:nowrap">
          <span style="color: #000088;">$start</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'2010-06-06'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$end</span> &nbsp; <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'2011-02-04'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #b1b100;">echo</span> <span style="color: #000088;">$start</span><span style="color: #339933;">-></span><span style="color: #004000;">diff</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$end</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-></span><span style="color: #004000;">days</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$start</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'2005-01-01'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #b1b100;">echo</span> <span style="color: #000088;">$start</span><span style="color: #339933;">-></span><span style="color: #004000;">diff</span><span style="color: #009900;">&#40;</span><span style="color: #000088;">$end</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-></span><span style="color: #004000;">days</span><span style="color: #339933;">;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

will always return 6015 on windows platforms no matter on the date values. it is a bug regarding php 5.3.x on windows platforms <a href="http://bugs.php.net/bug.php?id=51184" target="_blank">#51184 </a>and <a href="http://bugs.php.net/49778" target="_blank">#49778</a>. the solution to this is  
to use the following code :

<div class="codecolorer-container php geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />
        </div>
      </td>
      
      <td>
        <div class="php codecolorer" style="white-space:nowrap">
          <span style="color: #000000; font-weight: bold;">function</span> dateDiff<span style="color: #009900;">&#40;</span><span style="color: #000088;">$dt1</span><span style="color: #339933;">,</span> <span style="color: #000088;">$dt2</span><span style="color: #339933;">,</span> <span style="color: #000088;">$timeZone</span> <span style="color: #339933;">=</span> <span style="color: #0000ff;">'GMT'</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> <span style="color: #000088;">$tZone</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTimeZone<span style="color: #009900;">&#40;</span><span style="color: #000088;">$timeZone</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$dt1</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #000088;">$dt1</span><span style="color: #339933;">,</span> <span style="color: #000088;">$tZone</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$dt2</span> <span style="color: #339933;">=</span> <span style="color: #000000; font-weight: bold;">new</span> DateTime<span style="color: #009900;">&#40;</span><span style="color: #000088;">$dt2</span><span style="color: #339933;">,</span> <span style="color: #000088;">$tZone</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$ts1</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$dt1</span><span style="color: #339933;">-></span><span style="color: #004000;">format</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Y-m-d'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$ts2</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$dt2</span><span style="color: #339933;">-></span><span style="color: #004000;">format</span><span style="color: #009900;">&#40;</span><span style="color: #0000ff;">'Y-m-d'</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$diff</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/abs"><span style="color: #990000;">abs</span></a><span style="color: #009900;">&#40;</span><a href="http://www.php.net/strtotime"><span style="color: #990000;">strtotime</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$ts1</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">-</span><a href="http://www.php.net/strtotime"><span style="color: #990000;">strtotime</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$ts2</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000088;">$diff</span><span style="color: #339933;">/=</span> <span style="color: #cc66cc;">3600</span><span style="color: #339933;">*</span><span style="color: #cc66cc;">24</span><span style="color: #339933;">;</span><br /> <span style="color: #b1b100;">return</span> <span style="color: #000088;">$diff</span><span style="color: #339933;">;</span><br /> <span style="color: #009900;">&#125;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

echo dateDiff(&#8217;2010-10-10&#8242;, &#8217;2010-10-12&#8242;);

hope it helps
