---
title: creating a djvu book from a list of images
author: gjergj.sheldija
layout: post
permalink: /creating-a-djvu-book-from-a-list-of-images/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/creating-a-djvu-book-from-a-list-of-images/"></g:plusone></li></ul>
st_cached_time:
  - 1355875133
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/2710426401";s:9:"url_count";i:1;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 2
st_last_socialized:
  - 1392362712
st_tiny_url:
  - http://acme-tech.net/blog/creating-a-djvu-book-from-a-list-of-images/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - ubuntu
tags:
  - conversion
  - djvu
  - img
  - script
  - ubuntu
comments: true
---
i had the need to convert some images ( 2600 ) separated into folder into books. each one titled as the containing folder.

after installing the djvu libre tools under linux i resolved everything with this small script

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #c20cb9; font-weight: bold;">find</span> <span style="color: #000000; font-weight: bold;">*</span> <span style="color: #660033;">-type</span> d <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #000000; font-weight: bold;">while</span> <span style="color: #c20cb9; font-weight: bold;">read</span> DIRNAME<br /> <span style="color: #000000; font-weight: bold;">do</span><br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">" "</span><br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">"ENTERING &nbsp;: <span style="color: #007800;">$DIRNAME</span>"</span><br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">"=========================================================================="</span><br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">" "</span><br /> <br /> <span style="color: #7a0874; font-weight: bold;">cd</span> &nbsp;<span style="color: #007800;">$DIRNAME</span><br /> <br /> <span style="color: #000000; font-weight: bold;">for</span> <span style="color: #c20cb9; font-weight: bold;">file</span> <span style="color: #000000; font-weight: bold;">in</span> $<span style="color: #7a0874; font-weight: bold;">&#40;</span><span style="color: #c20cb9; font-weight: bold;">ls</span> <span style="color: #000000; font-weight: bold;">*</span>.jpg <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">sort</span> -n<span style="color: #7a0874; font-weight: bold;">&#41;</span>; <span style="color: #000000; font-weight: bold;">do</span><br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">"converting &nbsp;: <span style="color: #007800;">$file</span>"</span>;<br /> c44 <span style="color: #007800;">$file</span>;<br /> <span style="color: #000000; font-weight: bold;">done</span><br /> <br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">"creating book file : <span style="color: #007800;">$DIRNAME</span>.djvu"</span><br /> djvm <span style="color: #660033;">-c</span> <span style="color: #007800;">$DIRNAME</span>.djvu $<span style="color: #7a0874; font-weight: bold;">&#40;</span><span style="color: #c20cb9; font-weight: bold;">ls</span> <span style="color: #000000; font-weight: bold;">*</span>.djvu <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">sort</span> -n<span style="color: #7a0874; font-weight: bold;">&#41;</span><br /> <span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #ff0000;">"done."</span><br /> <span style="color: #7a0874; font-weight: bold;">cd</span> ..<br /> <span style="color: #000000; font-weight: bold;">done</span>
        </div>
      </td>
    </tr>
  </table>
</div>

as a short notice the ls * | sort -n is for sorting images correctly.

you need also to replace spaces in directory and path names, to do so you can use this script :

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
          <span style="color: #666666; font-style: italic;">#!/bin/bash</span><br /> <br /> <span style="color: #c20cb9; font-weight: bold;">ls</span> <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #000000; font-weight: bold;">while</span> <span style="color: #c20cb9; font-weight: bold;">read</span> <span style="color: #660033;">-r</span> FILE<br /> <span style="color: #000000; font-weight: bold;">do</span><br /> &nbsp; &nbsp; <span style="color: #c20cb9; font-weight: bold;">mv</span> <span style="color: #660033;">-v</span> <span style="color: #ff0000;">"<span style="color: #007800;">$FILE</span>"</span> <span style="color: #000000; font-weight: bold;">`</span><span style="color: #7a0874; font-weight: bold;">echo</span> <span style="color: #007800;">$FILE</span> <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">tr</span> <span style="color: #ff0000;">' '</span> <span style="color: #ff0000;">'_'</span> <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">tr</span> <span style="color: #660033;">-d</span> <span style="color: #ff0000;">'[{}(),\!]'</span> <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">tr</span> <span style="color: #660033;">-d</span> <span style="color: #ff0000;">"\'"</span> <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">tr</span> <span style="color: #ff0000;">'[A-Z]'</span> <span style="color: #ff0000;">'[a-z]'</span> <span style="color: #000000; font-weight: bold;">|</span> <span style="color: #c20cb9; font-weight: bold;">sed</span> <span style="color: #ff0000;">'s/_-_/_/g'</span><span style="color: #000000; font-weight: bold;">`</span><br /> <span style="color: #000000; font-weight: bold;">done</span>
        </div>
      </td>
    </tr>
  </table>
</div>
