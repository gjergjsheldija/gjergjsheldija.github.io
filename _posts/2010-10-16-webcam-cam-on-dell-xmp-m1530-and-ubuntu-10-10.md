---
title: 'webcam cam on dell xmp m1530<br/> and ubuntu 10.10'
author: gjergj.sheldija
layout: post
permalink: /webcam-cam-on-dell-xmp-m1530-and-ubuntu-10-10/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/webcam-cam-on-dell-xmp-m1530-and-ubuntu-10-10/"></g:plusone></li></ul>
st_cached_time:
  - 1355870314
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5688220542";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392348134
st_tiny_url:
  - http://acme-tech.net/blog/webcam-cam-on-dell-xmp-m1530-and-ubuntu-10-10/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - linux
  - ubuntu
tags:
  - cam
  - dell m1530
  - ubuntu 10.10
  - webcam
comments: true
---
quick fix how to enable the integrated webcam on a dell xps m1530 on ubuntu 10.10 to work with skype and ekiga. first do a

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
          <span style="color: #c20cb9; font-weight: bold;">sudo</span> modprobe uvcvideo
        </div>
      </td>
    </tr>
  </table>
</div>

if it works ok, then add it as a line in /etc/modules with

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
          <span style="color: #c20cb9; font-weight: bold;">sudo</span> gedit <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>modules
        </div>
      </td>
    </tr>
  </table>
</div>

restart and it&#8217;s done.
