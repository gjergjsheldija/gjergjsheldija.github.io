---
title: redmine 0.8.4 on ubuntu jaunty
author: gjergj.sheldija
layout: post
permalink: /redmine-0-8-4-on-ubuntu-jaunty/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/redmine-0-8-4-on-ubuntu-jaunty/"></g:plusone></li></ul>
st_cached_time:
  - 1355949086
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5682232461";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 3
st_last_socialized:
  - 1392323013
st_tiny_url:
  - http://acme-tech.net/blog/redmine-0-8-4-on-ubuntu-jaunty/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - random
tags:
  - jauntu
  - rails
  - redmine
  - ubuntu
comments: true
---
this is a quick guide based on [this][1], it only differs on some small apache configs and rails stuff, so i&#8217;m gonna write only the different steps

before running rake&#8230;you should do a

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
          $ <span style="color: #c20cb9; font-weight: bold;">sudo</span> gem <span style="color: #c20cb9; font-weight: bold;">install</span> rubygems-update<br /> $ <span style="color: #c20cb9; font-weight: bold;">sudo</span> gem update <span style="color: #660033;">--system</span>
        </div>
      </td>
    </tr>
  </table>
</div>

due to some problems with apache confing i moved the whole redmine directory from /var/www to /opt/redmine

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
          <span style="color: #666666;">$ </span><span style="color: #c20cb9; font-weight: bold;">sudo</span> <span style="color: #c20cb9; font-weight: bold;">ln</span> <span style="color: #660033;">-s</span> <span style="color: #000000; font-weight: bold;">/</span>opt<span style="color: #000000; font-weight: bold;">/</span>redmine<span style="color: #000000; font-weight: bold;">/</span>public <span style="color: #000000; font-weight: bold;">/</span>var<span style="color: #000000; font-weight: bold;">/</span>www<span style="color: #000000; font-weight: bold;">/</span>redmine
        </div>
      </td>
    </tr>
  </table>
</div>

and did a quick mod in /etc/apache2/sites-enabled/000-default adding this before the VirtualHost

<div class="codecolorer-container apache geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />
        </div>
      </td>
      
      <td>
        <div class="apache codecolorer" style="white-space:nowrap">
          ...<br /> RailsBaseUri &nbsp; /redmine<br /> </<span style="color: #000000; font-weight:bold;">VirtualHost</span>>
        </div>
      </td>
    </tr>
  </table>
</div>

restart apache and that&#8217;s it.

 [1]: http://wiki.ousli.org/index.php/RedmineUbuntu
