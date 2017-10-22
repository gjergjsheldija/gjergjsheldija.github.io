---
title: mercurial on hostmonster
author: gjergj.sheldija
layout: post
permalink: /mercurial-on-hostmonster/
categories:
  - code
  - hosting
  - linux
tags:
  - hostmonster
  - mercurial
comments: true
---
this i quick guide on how to install mercurial on hostmonster. it's made of pieces taken from the net plus some trial and error.

#### update the path settings

update your .bashrc file  
Add or edit this line

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
          <span style="color: #007800;">PATH</span>=<span style="color: #007800;">$PATH</span>:<span style="color: #007800;">$HOME</span><span style="color: #000000; font-weight: bold;">/</span>bin:<span style="color: #007800;">$HOME</span><span style="color: #000000; font-weight: bold;">/</span>packages<span style="color: #000000; font-weight: bold;">/</span>mercurial
        </div>
      </td>
    </tr>
  </table>
</div>

source ~/.bashrc

#### install mercurial

get mercurial and install

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />11<br />12<br />13<br />14<br />15<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<br /> <span style="color: #c20cb9; font-weight: bold;">mkdir</span> install_files<br /> <span style="color: #c20cb9; font-weight: bold;">mkdir</span> packages<br /> <span style="color: #c20cb9; font-weight: bold;">mkdir</span> ~<span style="color: #000000; font-weight: bold;">/</span>public_html<span style="color: #000000; font-weight: bold;">/</span>hg<br /> <span style="color: #c20cb9; font-weight: bold;">mkdir</span> ~<span style="color: #000000; font-weight: bold;">/</span>public_html<span style="color: #000000; font-weight: bold;">/</span>hg<span style="color: #000000; font-weight: bold;">/</span>repos<br /> <span style="color: #7a0874; font-weight: bold;">cd</span> ~<span style="color: #000000; font-weight: bold;">/</span>packages<br /> http:<span style="color: #000000; font-weight: bold;">//</span>mercurial.selenic.com<span style="color: #000000; font-weight: bold;">/</span>release<span style="color: #000000; font-weight: bold;">/</span>mercurial-1.6.3.tar.gz<br /> <span style="color: #c20cb9; font-weight: bold;">tar</span> zxf mercurial-1.6.3.tar.gz<br /> <span style="color: #c20cb9; font-weight: bold;">mv</span> mercurial-1.6.3.tar.gz ~<span style="color: #000000; font-weight: bold;">/</span>install_files<span style="color: #000000; font-weight: bold;">/</span><br /> <span style="color: #c20cb9; font-weight: bold;">mv</span> mercurial<span style="color: #000000; font-weight: bold;">*</span> mercurial<br /> <span style="color: #7a0874; font-weight: bold;">cd</span> mercurial<br /> <span style="color: #c20cb9; font-weight: bold;">make</span> <span style="color: #7a0874; font-weight: bold;">local</span><br /> .<span style="color: #000000; font-weight: bold;">/</span>hg debuginstall<br /> <span style="color: #c20cb9; font-weight: bold;">cp</span> ~<span style="color: #000000; font-weight: bold;">/</span>packages<span style="color: #000000; font-weight: bold;">/</span>mercurial<span style="color: #000000; font-weight: bold;">/</span>hgweb.cgi ~<span style="color: #000000; font-weight: bold;">/</span>public_html<span style="color: #000000; font-weight: bold;">/</span>hg<br /> <span style="color: #c20cb9; font-weight: bold;">chmod</span> <span style="color: #000000;">755</span> ~<span style="color: #000000; font-weight: bold;">/</span>public_html<span style="color: #000000; font-weight: bold;">/</span>hg<span style="color: #000000; font-weight: bold;">/</span>hgweb.cgi
        </div>
      </td>
    </tr>
  </table>
</div>

now inside the hg dir create those files :  
*hgweb.cgi*

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
          <span style="color: #666666; font-style: italic;">#!/usr/bin/env python</span><br /> <span style="color: #666666; font-style: italic;">#</span><br /> <span style="color: #666666; font-style: italic;"># An example hgweb CGI script, edit as necessary</span><br /> <span style="color: #666666; font-style: italic;"># See also http://mercurial.selenic.com/wiki/PublishingRepositories</span><br /> <br /> <span style="color: #666666; font-style: italic;"># Path to repo or hgweb config to serve (see 'hg help hgweb')</span><br /> config = <span style="color: #ff0000;">"/full/path/to/your/hgweb.config"</span><br /> <br /> <span style="color: #666666; font-style: italic;"># Uncomment and adjust if Mercurial is not installed system-wide:</span><br /> import sys; sys.path.insert<span style="color: #7a0874; font-weight: bold;">&#40;</span><span style="color: #000000;"></span>, <span style="color: #ff0000;">"/full/path/to/your/mercurial"</span><span style="color: #7a0874; font-weight: bold;">&#41;</span><br /> <br /> <span style="color: #666666; font-style: italic;"># Uncomment to send python tracebacks to the browser if an error occurs:</span><br /> <span style="color: #666666; font-style: italic;">#import cgitb; cgitb.enable()</span><br /> <br /> from mercurial import demandimport; demandimport.enable<span style="color: #7a0874; font-weight: bold;">&#40;</span><span style="color: #7a0874; font-weight: bold;">&#41;</span><br /> from mercurial.hgweb import hgweb, wsgicgi<br /> application = hgweb<span style="color: #7a0874; font-weight: bold;">&#40;</span>config<span style="color: #7a0874; font-weight: bold;">&#41;</span><br /> wsgicgi.launch<span style="color: #7a0874; font-weight: bold;">&#40;</span>application<span style="color: #7a0874; font-weight: bold;">&#41;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

*hgweb.config*

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #7a0874; font-weight: bold;">&#91;</span>web<span style="color: #7a0874; font-weight: bold;">&#93;</span><br /> <span style="color: #007800;">allowpull</span>=<span style="color: #c20cb9; font-weight: bold;">true</span><br /> <span style="color: #007800;">style</span>=gitweb<br /> baseurl = <span style="color: #000000; font-weight: bold;">/</span>hg<br /> <br /> <span style="color: #7a0874; font-weight: bold;">&#91;</span>collections<span style="color: #7a0874; font-weight: bold;">&#93;</span><br /> <span style="color: #000000; font-weight: bold;">/</span>full<span style="color: #000000; font-weight: bold;">/</span>path<span style="color: #000000; font-weight: bold;">/</span>to<span style="color: #000000; font-weight: bold;">/</span>your<span style="color: #000000; font-weight: bold;">/</span>repos<span style="color: #000000; font-weight: bold;">/</span>directory = <span style="color: #000000; font-weight: bold;">/</span>full<span style="color: #000000; font-weight: bold;">/</span>path<span style="color: #000000; font-weight: bold;">/</span>to<span style="color: #000000; font-weight: bold;">/</span>your<span style="color: #000000; font-weight: bold;">/</span>repos<span style="color: #000000; font-weight: bold;">/</span>directory
        </div>
      </td>
    </tr>
  </table>
</div>

*.htaccess*

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          Options +ExecCGI<br /> RewriteEngine On<br /> <span style="color: #666666; font-style: italic;"># / for root directory; specify a complete path from / for others</span><br /> RewriteBase <span style="color: #000000; font-weight: bold;">/</span>hg<br /> RewriteRule ^$ hgweb.cgi <span style="color: #7a0874; font-weight: bold;">&#91;</span>L<span style="color: #7a0874; font-weight: bold;">&#93;</span><br /> RewriteCond <span style="color: #000000; font-weight: bold;">%</span><span style="color: #7a0874; font-weight: bold;">&#123;</span>REQUEST_FILENAME<span style="color: #7a0874; font-weight: bold;">&#125;</span> <span style="color: #000000; font-weight: bold;">!</span>-f<br /> RewriteCond <span style="color: #000000; font-weight: bold;">%</span><span style="color: #7a0874; font-weight: bold;">&#123;</span>REQUEST_FILENAME<span style="color: #7a0874; font-weight: bold;">&#125;</span> <span style="color: #000000; font-weight: bold;">!</span>-d<br /> RewriteRule <span style="color: #7a0874; font-weight: bold;">&#40;</span>.<span style="color: #000000; font-weight: bold;">*</span><span style="color: #7a0874; font-weight: bold;">&#41;</span> hgweb.cgi<span style="color: #000000; font-weight: bold;">/</span><span style="color: #007800;">$1</span> <span style="color: #7a0874; font-weight: bold;">&#91;</span>QSA,L<span style="color: #7a0874; font-weight: bold;">&#93;</span>
        </div>
      </td>
    </tr>
  </table>
</div>

#### initialize the mercurial repository

you need to change REPOSITORY to your repository name  
if you want more than one repository, run the command for each of them

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
          ~<span style="color: #000000; font-weight: bold;">/</span>packages<span style="color: #000000; font-weight: bold;">/</span>mercurial<span style="color: #000000; font-weight: bold;">/</span>hg init REPOSITORY
        </div>
      </td>
    </tr>
  </table>
</div>

#### create hgrc files for each project

<div class="codecolorer-container bash geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />
        </div>
      </td>
      
      <td>
        <div class="bash codecolorer" style="white-space:nowrap">
          <span style="color: #7a0874; font-weight: bold;">&#91;</span>web<span style="color: #7a0874; font-weight: bold;">&#93;</span><br /> contact = Gjergj Sheldija<br /> description =Project Description<br /> style = gitweb<br /> allow_push = MYUSERNAME<br /> push_ssl = <span style="color: #c20cb9; font-weight: bold;">false</span><br /> allow_archive = gz <span style="color: #c20cb9; font-weight: bold;">zip</span> bz2
        </div>
      </td>
    </tr>
  </table>
</div>

there are a couple of things that are non standard here :  
first, i used mercurial 1.6.3 and not the last stable version as the client version that comes default with ubuntu is 1.6.3  
second i made all the repositories visible by default, to change this, you need to add those lines to the .htaccess file

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
          AuthUserFile <span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>hg-basic-auth<br /> AuthName <span style="color: #ff0000;">"Please Log In"</span><br /> AuthType Basic
        </div>
      </td>
    </tr>
  </table>
</div>

and create a password file for the users  
you need to change the values of HGUSERNAME and PASSWORD to your wanted user name and password

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<br /> htpasswd <span style="color: #660033;">-b</span> <span style="color: #660033;">-c</span> <span style="color: #660033;">-d</span> ~<span style="color: #000000; font-weight: bold;">/</span>etc<span style="color: #000000; font-weight: bold;">/</span>hg-basic-auth HGUSERNAME PASSWORD
        </div>
      </td>
    </tr>
  </table>
</div>
