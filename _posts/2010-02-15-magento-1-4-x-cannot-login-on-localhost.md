---
title: magento 1.4.x cannot login on localhost
author: gjergj.sheldija
layout: post
permalink: /magento-1-4-x-cannot-login-on-localhost/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/magento-1-4-x-cannot-login-on-localhost/"></g:plusone></li></ul>
st_cached_time:
  - 1355881500
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5680192245";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 3
st_last_socialized:
  - 1392312513
st_tiny_url:
  - http://acme-tech.net/blog/magento-1-4-x-cannot-login-on-localhost/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
  - magento
  - php
tags:
  - localhost
  - login
  - magento 1.4
comments: true
---
magento 1.4.x stable has a problem on the login procedure on localhost.  
you need to change in app/code/core/Mage/Core/Model/Session/Abstract/Varien.php

<div class="codecolorer-container php geshi" style="overflow:auto;white-space:nowrap;width:100%;height:300px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />20<br />21<br />22<br />
        </div>
      </td>
      
      <td>
        <div class="php codecolorer" style="white-space:nowrap">
          &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #666666; font-style: italic;">// session cookie params</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #000088;">$cookieParams</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/array"><span style="color: #990000;">array</span></a><span style="color: #009900;">&#40;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'lifetime'</span> <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getLifetime</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'path'</span> &nbsp; &nbsp; <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getPath</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'domain'</span> &nbsp; <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getConfigDomain</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'secure'</span> &nbsp; <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">isSecure</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'httponly'</span> <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getHttponly</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #339933;">!</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'httponly'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://www.php.net/unset"><span style="color: #990000;">unset</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'httponly'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #339933;">!</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'secure'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://www.php.net/unset"><span style="color: #990000;">unset</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'secure'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><span style="color: #339933;">!</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'domain'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://www.php.net/unset"><span style="color: #990000;">unset</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'domain'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #009900;">&#125;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #009900;">&#125;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #009900;">&#125;</span><br /> <br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #b1b100;">if</span> <span style="color: #009900;">&#40;</span><a href="http://www.php.net/isset"><span style="color: #990000;">isset</span></a><span style="color: #009900;">&#40;</span><span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'domain'</span><span style="color: #009900;">&#93;</span><span style="color: #009900;">&#41;</span><span style="color: #009900;">&#41;</span> <span style="color: #009900;">&#123;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #000088;">$cookieParams</span><span style="color: #009900;">&#91;</span><span style="color: #0000ff;">'domain'</span><span style="color: #009900;">&#93;</span> <span style="color: #339933;">=</span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getDomain</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #009900;">&#125;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

with

<div class="codecolorer-container php geshi" style="overflow:auto;white-space:nowrap;width:100%;height:300px;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />16<br />17<br />18<br />19<br />20<br />21<br />22<br />23<br />
        </div>
      </td>
      
      <td>
        <div class="php codecolorer" style="white-space:nowrap">
          &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #666666; font-style: italic;">// session cookie params</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #000088;">$cookieParams</span> <span style="color: #339933;">=</span> <a href="http://www.php.net/array"><span style="color: #990000;">array</span></a><span style="color: #009900;">&#40;</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'lifetime'</span> <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getLifetime</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #0000ff;">'path'</span> &nbsp; &nbsp; <span style="color: #339933;">=></span> <span style="color: #000088;">$cookie</span><span style="color: #339933;">-></span><span style="color: #004000;">getPath</span><span style="color: #009900;">&#40;</span><span style="color: #009900;">&#41;</span><span style="color: #339933;">,</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #666666; font-style: italic;">// 'domain' &nbsp; => $cookie->getConfigDomain(),</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #666666; font-style: italic;">// 'secure' &nbsp; => $cookie->isSecure(),</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #666666; font-style: italic;">// 'httponly' => $cookie->getHttponly()</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color: #009900;">&#41;</span><span style="color: #339933;">;</span><br /> <span style="color: #666666; font-style: italic;">/*<br /> &nbsp; &nbsp; &nbsp; &nbsp; if (!$cookieParams['httponly']) {<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unset($cookieParams['httponly']);<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if (!$cookieParams['secure']) {<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unset($cookieParams['secure']);<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if (!$cookieParams['domain']) {<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; unset($cookieParams['domain']);<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; }<br /> &nbsp; &nbsp; &nbsp; &nbsp; }<br /> <br /> &nbsp; &nbsp; &nbsp; &nbsp; if (isset($cookieParams['domain'])) {<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; $cookieParams['domain'] = $cookie->getDomain();<br /> &nbsp; &nbsp; &nbsp; &nbsp; }<br /> */</span>
        </div>
      </td>
    </tr>
  </table>
</div>
