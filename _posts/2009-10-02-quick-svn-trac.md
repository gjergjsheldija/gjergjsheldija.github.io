---
title: quick svn + trac
author: gjergj.sheldija
layout: post
permalink: /quick-svn-trac/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/quick-svn-trac/"></g:plusone></li></ul>
st_cached_time:
  - 1355985459
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5685532990";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392338378
st_tiny_url:
  - http://acme-tech.net/blog/quick-svn-trac/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
tags:
  - install
  - linux
  - svn
  - trac
  - ubuntu
comments: true
---
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
          <span style="color: #c20cb9; font-weight: bold;">svn import</span> <span style="color: #660033;">-m</span> <span style="color: #ff0000;">"First import to SVN"</span> <span style="color: #000000; font-weight: bold;">/</span>import<span style="color: #000000; font-weight: bold;">/</span>from<span style="color: #000000; font-weight: bold;">/</span>here<span style="color: #000000; font-weight: bold;">/</span>project file:<span style="color: #000000; font-weight: bold;">///</span>var<span style="color: #000000; font-weight: bold;">/</span>svn<span style="color: #000000; font-weight: bold;">/</span>repos<span style="color: #000000; font-weight: bold;">/</span>project<span style="color: #000000; font-weight: bold;">/</span>trunk
        </div>
      </td>
    </tr>
  </table>
</div>

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
          <span style="color: #c20cb9; font-weight: bold;">sudo</span> trac-admin <span style="color: #000000; font-weight: bold;">/</span>var<span style="color: #000000; font-weight: bold;">/</span>trac<span style="color: #000000; font-weight: bold;">/</span>sites<span style="color: #000000; font-weight: bold;">/</span>testProject initenv<br /> <span style="color: #c20cb9; font-weight: bold;">sudo</span> <span style="color: #c20cb9; font-weight: bold;">chown</span> <span style="color: #660033;">-R</span> www-data <span style="color: #000000; font-weight: bold;">/</span>var<span style="color: #000000; font-weight: bold;">/</span>trac<span style="color: #000000; font-weight: bold;">/</span>sites<span style="color: #000000; font-weight: bold;">/</span>testProject
        </div>
      </td>
    </tr>
  </table>
</div>
