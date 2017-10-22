---
title: using bazaar as a subversion client
author: gjergj.sheldija
layout: post
permalink: /using-bazaar-as-a-subversion-client/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/using-bazaar-as-a-subversion-client/"></g:plusone></li></ul>
st_cached_time:
  - 1355986687
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5744101463";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392394880
st_tiny_url:
  - http://acme-tech.net/blog/using-bazaar-as-a-subversion-client/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - bazaar
  - code
  - php
  - svn
tags:
  - bazaar
  - bzr
  - client
  - guide
  - subversion
  - svn
comments: true
---
a quick sample based guide on using bazaar as a svn client..

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          bzr init-repo <span style="color: #c20cb9; font-weight: bold;">gettext</span><br /> bzr checkout https:<span style="color: #000000; font-weight: bold;">//</span>....<br /> bzr branch <span style="color: #c20cb9; font-weight: bold;">gettext</span> development
        </div>
      </td>
    </tr>
  </table>
</div>

after you have some changes to submit..

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #7a0874; font-weight: bold;">cd</span> <span style="color: #c20cb9; font-weight: bold;">gettext</span><br /> bzr merge ..<span style="color: #000000; font-weight: bold;">/</span>development<br /> bzr commit <span style="color: #660033;">-m</span> <span style="color: #ff0000;">'testing bzr-svn'</span>
        </div>
      </td>
    </tr>
  </table>
</div>
