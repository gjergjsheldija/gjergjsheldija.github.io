---
title: monitorless karmic koala
author: gjergj.sheldija
layout: post
permalink: /monitorless-karmic-koala/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/monitorless-karmic-koala/"></g:plusone></li></ul>
st_cached_time:
  - 1355868596
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5716466847";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392330683
st_tiny_url:
  - http://acme-tech.net/blog/monitorless-karmic-koala/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - linux
tags:
  - karmic
  - koala
  - ubuntu
comments: true
---
karmic koala and intel i915 chipset don&#8217;t go much well together on monitorless pc&#8217;s, apparently because of this : [431812 ][1]  
besides that, the computer just hangs in an endless loops trying to detect the non present monitor.  
the solution is quite simple &#8211; although i needed 3 hours to figure it out since karmic koala uses the new upstart service management.  
just replace in /etc/init/gdm.conf

<div class="codecolorer-container text geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />
        </div>
      </td>
      
      <td>
        <div class="text codecolorer" style="white-space:nowrap">
          start on (runlevel [3]<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and filesystem<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and started hal<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and tty-device-added KERNEL=tty7<br /> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and (graphics-device-added or stopped udevtrigger))<br /> stop on runlevel [0216]
        </div>
      </td>
    </tr>
  </table>
</div>

 [1]: https://bugs.launchpad.net/ubuntu/karmic/+source/initramfs-tools/+bug/431812
