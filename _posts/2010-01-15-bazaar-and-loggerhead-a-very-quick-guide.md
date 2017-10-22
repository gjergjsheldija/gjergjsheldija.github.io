---
title: bazaar and loggerhead a ( very ) quick guide
author: gjergj.sheldija
layout: post
permalink: /bazaar-and-loggerhead-a-very-quick-guide/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/bazaar-and-loggerhead-a-very-quick-guide/"></g:plusone></li></ul>
st_cached_time:
  - 1355866040
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5680654493";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 2
st_last_socialized:
  - 1392319309
st_tiny_url:
  - http://acme-tech.net/blog/bazaar-and-loggerhead-a-very-quick-guide/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
  - linux
tags:
  - bazaar
  - loggerhead
  - ubuntu
comments: true
---
### bazaar

first add the bazaar PPA to the repository list

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
          <span style="color: #c20cb9; font-weight: bold;">vi</span> <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>apt<span style="color: #000000; font-weight: bold;">/</span>sources.list.d<span style="color: #000000; font-weight: bold;">/</span>bzr.list
        </div>
      </td>
    </tr>
  </table>
</div>

add the following

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #666666; font-style: italic;"># Bazaar PPA</span><br /> deb http:<span style="color: #000000; font-weight: bold;">//</span>ppa.launchpad.net<span style="color: #000000; font-weight: bold;">/</span>bzr<span style="color: #000000; font-weight: bold;">/</span>ubuntu hardy main<br /> deb-src http:<span style="color: #000000; font-weight: bold;">//</span>ppa.launchpad.net<span style="color: #000000; font-weight: bold;">/</span>bzr<span style="color: #000000; font-weight: bold;">/</span>ubuntu hardy main<br /> <span style="color: #c20cb9; font-weight: bold;">aptitude</span> update
        </div>
      </td>
    </tr>
  </table>
</div>

### bazaar server

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
          <span style="color: #c20cb9; font-weight: bold;">aptitude</span> <span style="color: #c20cb9; font-weight: bold;">install</span> bzr bzrtools python-paramiko
        </div>
      </td>
    </tr>
  </table>
</div>

### sftp

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
          <span style="color: #c20cb9; font-weight: bold;">aptitude</span> <span style="color: #c20cb9; font-weight: bold;">install</span> <span style="color: #c20cb9; font-weight: bold;">ssh</span> openssh-server
        </div>
      </td>
    </tr>
  </table>
</div>

create the user account

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
          useradd <span style="color: #660033;">--create-home</span> <span style="color: #660033;">--home-dir</span> <span style="color: #000000; font-weight: bold;">/</span>var<span style="color: #000000; font-weight: bold;">/</span>local<span style="color: #000000; font-weight: bold;">/</span>bzr <span style="color: #660033;">--shell</span> <span style="color: #000000; font-weight: bold;">/</span>usr<span style="color: #000000; font-weight: bold;">/</span>lib<span style="color: #000000; font-weight: bold;">/</span>sftp-server bzr<br /> <span style="color: #c20cb9; font-weight: bold;">passwd</span> bzr<br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">'/usr/lib/sftp-server'</span> <span style="color: #000000; font-weight: bold;">&</span>gt;<span style="color: #000000; font-weight: bold;">&</span>gt; <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>shells
        </div>
      </td>
    </tr>
  </table>
</div>

### Loggerhead

i decided to use Loggerhead instead of an apache or lighttpd integratrion so..

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #c20cb9; font-weight: bold;">aptitude</span> <span style="color: #c20cb9; font-weight: bold;">install</span> python-configobj python-simpletal python-paste python-pastedeploy python-simplejson<br /> bzr branch lp:loggerhead<br /> <span style="color: #c20cb9; font-weight: bold;">wget</span> http:<span style="color: #000000; font-weight: bold;">//</span>launchpad.net<span style="color: #000000; font-weight: bold;">/</span>loggerhead<span style="color: #000000; font-weight: bold;">/</span><span style="color: #000000;">1.17</span><span style="color: #000000; font-weight: bold;">/</span><span style="color: #000000;">1.17</span><span style="color: #000000; font-weight: bold;">/</span>+download<span style="color: #000000; font-weight: bold;">/</span>loggerhead-<span style="color: #000000;">1.17</span>.tar.gz<br /> <span style="color: #c20cb9; font-weight: bold;">tar</span> zxvf loggerhead-<span style="color: #000000;">1.17</span>.tar.gz<br /> python setup.py <span style="color: #c20cb9; font-weight: bold;">install</span><br /> <span style="color: #000000; font-weight: bold;">/</span>usr<span style="color: #000000; font-weight: bold;">/</span>bin<span style="color: #000000; font-weight: bold;">/</span>serve-branches <span style="color: #000000; font-weight: bold;">/</span>var<span style="color: #000000; font-weight: bold;">/</span>local<span style="color: #000000; font-weight: bold;">/</span>bzr<span style="color: #000000; font-weight: bold;">/</span>
        </div>
      </td>
    </tr>
  </table>
</div>

### starting and stopping loggerhead

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #c20cb9; font-weight: bold;">nano</span> <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>loggerhead.conf<br /> <span style="color: #666666; font-style: italic;"># use this if you're mapping loggerhead within apache via proxy</span><br /> <span style="color: #666666; font-style: italic;"># server.webpath = 'http://code.example.org/Loggerhead/'</span><br /> <span style="color: #666666; font-style: italic;"># the access and debug logs can be set up to roll 'daily', 'weekly', or 'never':</span><br /> log.roll = <span style="color: #ff0000;">'daily'</span><br /> <span style="color: #666666; font-style: italic;"># here's an example of an auto-published folder:</span><br /> <br /> <span style="color: #7a0874; font-weight: bold;">&#91;</span>bazaar<span style="color: #7a0874; font-weight: bold;">&#93;</span><br /> name = <span style="color: #ff0000;">'My Bazaar'</span><br /> auto_publish_folder = <span style="color: #ff0000;">'/var/local/bzr/'</span><br /> loggerhead can be started and stopped via<br /> <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>init.d<span style="color: #000000; font-weight: bold;">/</span>loggerhead start<br /> <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>init.d<span style="color: #000000; font-weight: bold;">/</span>loggerhead stop<br /> loggerhead searching<br /> <span style="color: #c20cb9; font-weight: bold;">mkdir</span> <span style="color: #660033;">-p</span> ~<span style="color: #000000; font-weight: bold;">/</span>.bazaar<span style="color: #000000; font-weight: bold;">/</span>plugins<br /> bzr branch lp:bzr-search ~<span style="color: #000000; font-weight: bold;">/</span>.bazaar<span style="color: #000000; font-weight: bold;">/</span>plugins<span style="color: #000000; font-weight: bold;">/</span>search<br /> bzr index <span style="color: #000000; font-weight: bold;">/</span>var<span style="color: #000000; font-weight: bold;">/</span>local<span style="color: #000000; font-weight: bold;">/</span>bzr<span style="color: #000000; font-weight: bold;">/</span>Project1<br /> <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>init.d<span style="color: #000000; font-weight: bold;">/</span>loggerhead restart
        </div>
      </td>
    </tr>
  </table>
</div>
