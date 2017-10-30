---
title: redmine 0.8.4 on ubuntu jaunty
author: gjergj.sheldija
layout: post
permalink: /redmine-0-8-4-on-ubuntu-jaunty/
categories:
  - random
tags:
  - jauntu
  - rails
  - redmine
  - ubuntu
comments: true
---
this is a quick guide based on [this][1], it only differs on some small apache configs and rails stuff, so i&#8217;m gonna write only the different steps

before running rake&#8230;you should do a

```bash
$ sudo gem install rubygems-update
$ sudo gem update --system
```

due to some problems with apache confing i moved the whole redmine directory from /var/www to /opt/redmine

```bash
$ sudo ln -s /opt/redmine/public /var/www/redmine
```

and did a quick mod in /etc/apache2/sites-enabled/000-default adding this before the VirtualHost

```bash
...
RailsBaseUri   /redmine
</VirtualHost>
```

restart apache and that&#8217;s it.

 [1]: http://wiki.ousli.org/index.php/RedmineUbuntu
