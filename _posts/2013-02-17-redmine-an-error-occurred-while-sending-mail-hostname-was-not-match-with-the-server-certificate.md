---
title: 'redmine : An error occurred while sending mail (hostname was not match with the server certificate)'
author: gjergj.sheldija
layout: post
permalink: /redmine-an-error-occurred-while-sending-mail-hostname-was-not-match-with-the-server-certificate/
categories:
  - code
  - hosting
  - redmine
  - ubuntu
comments: true
---
quick fix for a silly error i was having today with redmine not sending email anymore. 
open config/environment.rb and add the following lines
{% codeblock lang:ruby %}
ActionMailer::Base::raise_delivery_errors = true
ActionMailer::Base::smtp_settings[:enable_starttls_auto] = false 
{% endcodeblock %}
it should solve the problem
