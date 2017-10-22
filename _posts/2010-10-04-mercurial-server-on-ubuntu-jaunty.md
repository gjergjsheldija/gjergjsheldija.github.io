---
title: mercurial server on ubuntu jaunty
author: gjergj.sheldija
layout: post
permalink: /mercurial-server-on-ubuntu-jaunty/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/mercurial-server-on-ubuntu-jaunty/"></g:plusone></li></ul>
st_cached_time:
  - 1355891612
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5690567337";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392380520
st_tiny_url:
  - http://acme-tech.net/blog/mercurial-server-on-ubuntu-jaunty/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
  - mercurial
tags:
  - hg
  - jaunty
  - mercurial
  - server
  - ubuntu
comments: true
---
this is a short howto on how to install a mercurial server on a ubuntu jaunty and maybe lynx.

first of all we install mercurial and the wsgi mod for apache

<div class="codecolorer-container text geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer" style="white-space:nowrap">
          sudo apt-get install mercurial libapache2-mod-wsgi
        </div>
      </td>
    </tr>
  </table>
</div>

second we create a directory where we want to store our mercurial source code and copy the defualt config files from the mercurial dir

<div class="codecolorer-container text geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer" style="white-space:nowrap">
          sudo mkdir /data/mercurial<br /> cd /data/mercurial<br /> mv /usr/share/doc/mercurial/examples/hgwebdir.wsgi /data/mercurial/hgwebdir.cgi
        </div>
      </td>
    </tr>
  </table>
</div>

under /etc/apache/sites-enabled/ edit file 000-default and add the following line

<div class="codecolorer-container text geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer" style="white-space:nowrap">
          ScriptAlias /hg "/data/mercurial/hgwebdir.cgi"
        </div>
      </td>
    </tr>
  </table>
</div>

change the default access to www-data for all the files inside /data/mercurial and that&#8217;s it, you can start creating and accessing mercurial repos

if you receive an error like ssq_required, you should create a file named hgrc inside the .hg directory of your project and add the following lines

<div class="codecolorer-container text geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer" style="white-space:nowrap">
          [web]<br /> push_ssl = false
        </div>
      </td>
    </tr>
  </table>
</div></p>
