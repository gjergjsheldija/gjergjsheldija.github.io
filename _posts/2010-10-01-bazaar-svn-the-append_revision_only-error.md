---
title: bazaar svn, the append_revision_only error
author: gjergj.sheldija
layout: post
permalink: /bazaar-svn-the-append_revision_only-error/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/bazaar-svn-the-append_revision_only-error/"></g:plusone></li></ul>
st_cached_time:
  - 1355898526
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/5675989045";s:9:"url_count";i:0;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392387675
st_tiny_url:
  - http://acme-tech.net/blog/bazaar-svn-the-append_revision_only-error/
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - bazaar
  - svn
tags:
  - bazaar
  - bzr
  - svn
comments: true
---
If you try to push changes from your Bazaar feature branch back to a Subversion repository, and the Subversion repository has been changed since you created your Bazaar branch, you may get something like this:

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
          &nbsp;bzr push<br /> &nbsp;Using saved push location: svn+http://svn/repos/Trunk/MyProject<br /> &nbsp;bzr: ERROR: Operation denied because it would change the mainline history. Set the append_revisions_only setting to False on branch "svn+http://svn/repos/Trunk/MyProject" to allow the mainline to change.
        </div>
      </td>
    </tr>
  </table>
</div>

Find subversion.conf. It is located at:

*   Vista/7: C:\Users\your-user-name\AppData\Roaming\bazaar\2.0\
*   XP/2003: C:\Documents and Settings\your-user-name\ApplicationData\bazaar\2.0\

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
          &nbsp;[4ef181b9-d188-42c4-ae88-5d15bdaece0b]<br /> &nbsp;locations = svn+http://svn/repos/Trunk/MyProject<br /> &nbsp;append_revisions_only = False
        </div>
      </td>
    </tr>
  </table>
</div>
