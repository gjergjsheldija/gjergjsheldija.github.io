---
title: var_dump() for java
author: gjergj.sheldija
layout: post
permalink: /var_dump-for-java/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/var_dump-for-java/"></g:plusone></li></ul>
st_cached_time:
  - 1355866729
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/2007641459";s:9:"url_count";i:1;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 2
st_last_socialized:
  - 1392391886
st_tiny_url:
  - http://acme-tech.net/blog/var_dump-for-java/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
  - java
  - php
tags:
  - java
  - var_dump
comments: true
---
quick tip for java,

<div class="codecolorer-container java geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />
        </div>
      </td>
      
      <td>
        <div class="java codecolorer" style="white-space:nowrap">
          <span style="color: #000000; font-weight: bold;">import</span> <span style="color: #006699;">java.lang.reflect.*</span><span style="color: #339933;">;</span><br /> ....<br /> <span style="color: #666666; font-style: italic;">//o Object..</span><br /> <a href="http://www.google.com/search?hl=en&q=allinurl%3Afield+java.sun.com&btnI=I%27m%20Feeling%20Lucky"><span style="color: #003399;">Field</span></a><span style="color: #009900;">&#91;</span><span style="color: #009900;">&#93;</span> fields <span style="color: #339933;">=</span> o.<span style="color: #006633;">getClass</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span>.<span style="color: #006633;">getDeclaredFields</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #000000; font-weight: bold;">for</span> <span style="color: #009900;">&#40;</span><span style="color: #000066; font-weight: bold;">int</span> i<span style="color: #339933;">=</span><span style="color: #cc66cc;"></span><span style="color: #339933;">;</span> i<span style="color: #339933;"><</span>fields.<span style="color: #006633;">length</span><span style="color: #339933;">;</span> i<span style="color: #339933;">++</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; <span style="color: #000000; font-weight: bold;">try</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://www.google.com/search?hl=en&q=allinurl%3Asystem+java.sun.com&btnI=I%27m%20Feeling%20Lucky"><span style="color: #003399;">System</span></a>.<span style="color: #006633;">out</span>.<span style="color: #006633;">println</span><span style="color: #009900;">&#40;</span>fields<span style="color: #009900;">&#91;</span>i<span style="color: #009900;">&#93;</span>.<span style="color: #006633;">getName</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span> <span style="color: #339933;">+</span> <span style="color: #0000ff;">" - "</span> <span style="color: #339933;">+</span> fields<span style="color: #009900;">&#91;</span>i<span style="color: #009900;">&#93;</span>.<span style="color: #006633;">get</span><span style="color: #009900;">&#40;</span>o<span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> &nbsp; &nbsp; <span style="color: #009900;">&#125;</span> <span style="color: #000000; font-weight: bold;">catch</span> <span style="color: #009900;">&#40;</span>java.<span style="color: #006633;">lang</span>.<a href="http://www.google.com/search?hl=en&q=allinurl%3Aillegalaccessexception+java.sun.com&btnI=I%27m%20Feeling%20Lucky"><span style="color: #003399;">IllegalAccessException</span></a> e<span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://www.google.com/search?hl=en&q=allinurl%3Asystem+java.sun.com&btnI=I%27m%20Feeling%20Lucky"><span style="color: #003399;">System</span></a>.<span style="color: #006633;">out</span>.<span style="color: #006633;">println</span><span style="color: #009900;">&#40;</span>e<span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span> <br /> &nbsp; &nbsp; <span style="color: #009900;">&#125;</span><br /> <span style="color: #009900;">&#125;</span>
        </div>
      </td>
    </tr>
  </table>
</div>
