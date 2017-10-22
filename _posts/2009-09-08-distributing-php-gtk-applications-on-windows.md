---
title: Distributing PHP-GTK Applications on Windows
author: admin
layout: post
permalink: /distributing-php-gtk-applications-on-windows/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/distributing-php-gtk-applications-on-windows/"></g:plusone></li></ul>
st_cached_time:
  - 1355966052
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5685761339";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392351913
st_tiny_url:
  - http://acme-tech.net/blog/distributing-php-gtk-applications-on-windows/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - code
tags:
  - gtk
  - php
comments: true
---
php-gtk is a php extension that uses the GTK (GIMP Tool Kit) to let developers build cool GUI apps which run on Linux, Windows, MacOS, BeOS and other platforms. I am currently studying the curves of building GUI software with php-gtk. It was going on fine. But the first problem I faced while distributing my php-gtk apps is that I need to port php, gtk and some other dependencies on the clients machine. I was searching on the internet if I can find a good solution to this problem. Luckily, I found one.

The package contains a tool kit for deploying php-gtk apps on windows. Download and unzip the package. Then modify and compile the NSIS script that comes in with the package to build a installation package for your own app.

Download Link:  
<a href="http://www.dreadsoft.org/php-gtk/pgsk.zip" target="_blank">http://www.dreadsoft.org/php-gtk/pgsk.zip</a>

This package requires the NSIS, get it from here :

Download Link:  
<a href="http://nsis.sourceforge.net" target="_blank">http://nsis.sourceforge.net</a>
