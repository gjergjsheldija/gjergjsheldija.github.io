---
title: download from rapidshare using aria
author: gjergj.sheldija
layout: post
permalink: /download-from-rapidshare-using-aria/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/download-from-rapidshare-using-aria/"></g:plusone></li></ul>
st_cached_time:
  - 1355877006
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5679340781";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392308579
st_tiny_url:
  - http://acme-tech.net/blog/download-from-rapidshare-using-aria/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - random
tags:
  - aria
  - download
  - rapidshare
comments: true
---
supposing you&#8217;ve saved all your rapidshare links in a file called links.txt the command line is :

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          aria2c <span style="color: #660033;">--http-user</span>=username <span style="color: #660033;">--http-password</span>=password <span style="color: #660033;">-i</span> links.txt <span style="color: #660033;">-j2</span> <span style="color: #660033;">-s4</span> <span style="color: #660033;">-c</span> <span style="color: #000000; font-weight: bold;">></span> <span style="color: #000000; font-weight: bold;">/</span>tmp<span style="color: #000000; font-weight: bold;">/</span>aria2c.log <span style="color: #000000;">2</span><span style="color: #000000; font-weight: bold;">>&</span><span style="color: #000000;">1</span> <span style="color: #000000; font-weight: bold;">&</span>
        </div>
      </td>
    </tr>
  </table>
</div>
