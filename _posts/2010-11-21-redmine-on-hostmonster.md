---
title: redmine 1.0.3 on hostmonster
author: gjergj.sheldija
layout: post
permalink: /redmine-on-hostmonster/
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
    </li><li><script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script><g:plusone size="tall" href="http://acme-tech.net/blog/redmine-on-hostmonster/"></g:plusone></li></ul>
st_cached_time:
  - 1355866350
st_tiny_url:
  - http://acme-tech.net/blog/redmine-on-hostmonster/
st_tweetmeme:
  - 's:85:"a:2:{s:7:"tm_link";s:37:"http://tweetmeme.com/story/3140022604";s:9:"url_count";i:1;}";'
st_reddit:
  - 'a:3:{s:9:"permalink";s:0:"";s:5:"score";i:0;s:12:"num_comments";i:0;}'
st_social_score:
  - 0
st_last_socialized:
  - 1392373709
st_twitter:
  - 0
st_facebook:
  - 0
st_googleplusones:
  - 0
categories:
  - hosting
  - redmine
tags:
  - hostmonster
  - redmine
comments: true
---
i had the need time ago to install redmine on my hostmonster account, after some struggling, trial and error, this is the procedure i followed. ymmv.

#### create a mysql database

login to cpanel and click on mysql database wizard, it will prompt you for database name, then ask you to make a user, make sure you GRANT ALL privileges. remember this database and username we will use it later.

#### create a sub-domain

for the purposes of this tutorial name it redmine, point this sub domain to ~/public_html/redmine.  
do NOT copy any files into this directory, we will be deleting it later

make sure you have the right version of rails installed  
in case it is different from what you need you can install a specific rails version on your machine by running:

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
          gem <span style="color: #c20cb9; font-weight: bold;">install</span> rails <span style="color: #660033;">-v</span>=2.3.5
        </div>
      </td>
    </tr>
  </table>
</div>

#### create ror directory

it is not recommended that you put your ror apps within the ~/public_html directory, as users would be able to see the rb files. so we are going to create a rails directory.

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<br /> <span style="color: #c20cb9; font-weight: bold;">mkdir</span> rails
        </div>
      </td>
    </tr>
  </table>
</div>

#### create rails app

you create a rails app on hostmonster just like you would on your system, by using the rails command. we are creating the rails project inside of the rails directory

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> rails<br /> rails <span style="color: #660033;">-D</span> redmine
        </div>
      </td>
    </tr>
  </table>
</div>

we need -D to let rails know that we want custom dispatch.rb, dispatch.cgi and dispatch.fcgi files for later steps.

#### create a sym-link for sub-domain

since the hostmonster interface won’t let you select a directory outside of public\_html, we are going to create a sym link from the ~/public\_html/redmine folder to ~/rails/redmine. to do this we will be deleting the ~/public_html/redmine directory. the sym link will recreate it.

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<span style="color: #000000; font-weight: bold;">/</span>public_html<br /> <span style="color: #c20cb9; font-weight: bold;">rm</span> <span style="color: #660033;">-R</span> redmine<br /> <span style="color: #c20cb9; font-weight: bold;">ln</span> <span style="color: #660033;">-s</span> ~<span style="color: #000000; font-weight: bold;">/</span>rails<span style="color: #000000; font-weight: bold;">/</span>redmine<span style="color: #000000; font-weight: bold;">/</span>public redmine
        </div>
      </td>
    </tr>
  </table>
</div>

#### prepare redmine

download the latest final release of redmine (the last one is 1.0.3). extract this to your desktop, you should now have a folder name redmine on your desktop. you need to download the following files : dispatch.rb, dispatch.cgi and dispatch.fcgi and put them in your local copy of redmine.

now edit your database.yml file with the database, username and password you created in step one. you only have to change those three values for production  configuration. to do so copy config/database.yml.example into config/database.yml and edit the latter.

#### upload redmine

via ftp upload your redmine files to your redmine directory.

#### finish the installation

ssh into your server, your going to want to chmod 755 your ~/rails/redmine/public folder.

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<span style="color: #000000; font-weight: bold;">/</span>rails<span style="color: #000000; font-weight: bold;">/</span>redmine<br /> <span style="color: #c20cb9; font-weight: bold;">chmod</span> <span style="color: #000000;">755</span> public
        </div>
      </td>
    </tr>
  </table>
</div>

remove any .htaccess file that may already be in the ~/rails/redmine/public directory.

download file from here: http://acme-tech.net/blog/files/redmine_htaccess.txt  into ~/rails/redmine/public directory and save it as .htaccess.

best way to do this is by typing following set of commands:

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<span style="color: #000000; font-weight: bold;">/</span>rails<span style="color: #000000; font-weight: bold;">/</span>redmine<span style="color: #000000; font-weight: bold;">/</span>public<br /> <span style="color: #c20cb9; font-weight: bold;">wget</span>
        </div>
      </td>
    </tr>
  </table>
</div>

http://acme-tech.net/blog/files/redmine_htaccess.txt

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
          &nbsp;<span style="color: #c20cb9; font-weight: bold;">mv</span> htaccess.txt .htaccess
        </div>
      </td>
    </tr>
  </table>
</div>

#### generate a session store secret

this is required for versions of redmine above release 0.8.7. redmine stores session data in cookies by default, which requires a secret to be generated. this can be done by running:

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<span style="color: #000000; font-weight: bold;">/</span>rails<span style="color: #000000; font-weight: bold;">/</span>redmine<br /> <span style="color: #007800;">RAILS_ENV</span>=production rake config<span style="color: #000000; font-weight: bold;">/</span>initializers<span style="color: #000000; font-weight: bold;">/</span>session_store.rb
        </div>
      </td>
    </tr>
  </table>
</div>

#### setup the db

we have to give redmine it&#8217;s database structure and default values.

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
          <span style="color: #7a0874; font-weight: bold;">cd</span> ~<span style="color: #000000; font-weight: bold;">/</span>rails<span style="color: #000000; font-weight: bold;">/</span>redmine<br /> <span style="color: #007800;">RAILS_ENV</span>=production rake db:migrate
        </div>
      </td>
    </tr>
  </table>
</div>

insert default configuration data in database

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
          <span style="color: #007800;">RAILS_ENV</span>=production rake redmine:load_default_data
        </div>
      </td>
    </tr>
  </table>
</div>

this step is optional but highly recommended, as you can define your own configuration from scratch. it will load default roles, trackers, statuses, workflows and enumerations.  
as a last thing you need to edit config/environment.rb and add the following lines :

<div class="codecolorer-container ruby geshi" style="width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />
        </div>
      </td>
      
      <td>
        <div class="ruby codecolorer">
          ENV<span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#996600;">'GEM_PATH'</span><span style="color:#006600; font-weight:bold;">&#93;</span> <span style="color:#006600; font-weight:bold;">||</span>= <span style="color:#996600;">'/ruby/gems:/usr/lib64/ruby/gems/1.8'</span><br /> ENV<span style="color:#006600; font-weight:bold;">&#91;</span><span style="color:#996600;">'RAILS_ENV'</span><span style="color:#006600; font-weight:bold;">&#93;</span> <span style="color:#006600; font-weight:bold;">||</span>= <span style="color:#996600;">'production'</span>
        </div>
      </td>
    </tr>
  </table>
</div>

**Update**  
since the last update from hostmonster i kep receiving a 500 error. the solution was pretty simple

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
          gem uninstall i18n
        </div>
      </td>
    </tr>
  </table>
</div>

then need to change config/boot.rb, and add 
<pre>require 'thread'</pre>

on the file header  
and change config/environment.rb, adding before 
<pre>Rails::Initializer...</pre>

<div class="codecolorer-container ruby geshi" style="overflow:auto;white-space:nowrap;width:100%;">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td class="line-numbers">
        <div>
          1<br />2<br />3<br />4<br />5<br />6<br />7<br />8<br />9<br />10<br />
        </div>
      </td>
      
      <td>
        <div class="ruby codecolorer" style="white-space:nowrap">
          <span style="color:#9966CC; font-weight:bold;">if</span> <span style="color:#6666ff; font-weight:bold;">Gem::VERSION</span> <span style="color:#006600; font-weight:bold;">></span>= <span style="color:#996600;">"1.3.6"</span><br /> &nbsp; <span style="color:#9966CC; font-weight:bold;">module</span> Rails<br /> &nbsp; &nbsp; <span style="color:#9966CC; font-weight:bold;">class</span> GemDependency<br /> &nbsp; &nbsp; &nbsp; <span style="color:#9966CC; font-weight:bold;">def</span> requirement<br /> &nbsp; &nbsp; &nbsp; &nbsp; r = <span style="color:#9966CC; font-weight:bold;">super</span><br /> &nbsp; &nbsp; &nbsp; &nbsp; <span style="color:#006600; font-weight:bold;">&#40;</span>r == <span style="color:#6666ff; font-weight:bold;">Gem::Requirement</span>.<span style="color:#9900CC;">default</span><span style="color:#006600; font-weight:bold;">&#41;</span> ? <span style="color:#0000FF; font-weight:bold;">nil</span> : r<br /> &nbsp; &nbsp; &nbsp; <span style="color:#9966CC; font-weight:bold;">end</span><br /> &nbsp; &nbsp; <span style="color:#9966CC; font-weight:bold;">end</span><br /> &nbsp; <span style="color:#9966CC; font-weight:bold;">end</span><br /> <span style="color:#9966CC; font-weight:bold;">end</span>
        </div>
      </td>
    </tr>
  </table>
</div>
