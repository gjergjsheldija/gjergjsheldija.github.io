---
title: fixing the java console on ubuntu with firefox
author: gjergj.sheldija
layout: post
permalink: /fixing-the-java-console-on-ubuntu-with-firefox/
st_tiny_url:
  - http://acme-tech.net/blog/fixing-the-java-console-on-ubuntu-with-firefox/
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/3075993131";s:9:"url_count";i:1;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392362713
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/fixing-the-java-console-on-ubuntu-with-firefox/"></g:plusone></li></ul>
st_cached_time:
  - 1355881838
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - java
  - ubuntu
tags:
  - applet
  - console
  - firefox
  - java
  - ubuntu
comments: true
---
ubuntu comes with icedtea / openjdk as the default java vm. this crewates some errors loading certain applets. the simple solution to fix that is to remove the icedtea plugin package and install the sun plugin package :

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #c20cb9; font-weight: bold;">sudo</span> <span style="color: #c20cb9; font-weight: bold;">apt-get remove</span> icedtea6-plugin<br /> <span style="color: #c20cb9; font-weight: bold;">sudo</span> <span style="color: #c20cb9; font-weight: bold;">apt-get install</span> sun-java6-plugin
        </div>
      </td>
    </tr>
  </table>
</div>

now open firefox and open about:plugins to check that everything is ok.  
in certain cases you may also need to do :

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
          <span style="color: #c20cb9; font-weight: bold;">sudo</span> update-alternatives <span style="color: #660033;">--config</span> java
        </div>
      </td>
    </tr>
  </table>
</div>
