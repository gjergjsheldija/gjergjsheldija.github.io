---
title: redmine 1.0.3 on hostmonster
author: gjergj.sheldija
layout: post
permalink: /redmine-on-hostmonster/
categories:
  - hosting
  - redmine
tags:
  - hostmonster
  - redmine
---
i had the need time ago to install redmine on my hostmonster account, after some struggling, trial and error, this is the procedure i followed. ymmv.

#### create a mysql database

login to cpanel and click on mysql database wizard, it will prompt you for database name, then ask you to make a user, make sure you GRANT ALL privileges. remember this database and username we will use it later.

#### create a sub-domain

for the purposes of this tutorial name it redmine, point this sub domain to ~/public_html/redmine.  
do NOT copy any files into this directory, we will be deleting it later

make sure you have the right version of rails installed  
in case it is different from what you need you can install a specific rails version on your machine by running:

```bash
gem install rails -v=2.3.5
```

#### create ror directory

it is not recommended that you put your ror apps within the ~/public_html directory, as users would be able to see the rb files. so we are going to create a rails directory.

```
cd ~
mkdir rails
```

#### create rails app

you create a rails app on hostmonster just like you would on your system, by using the rails command. we are creating the rails project inside of the rails directory

```
cd rails
rails -D redmine
```

we need -D to let rails know that we want custom dispatch.rb, dispatch.cgi and dispatch.fcgi files for later steps.

#### create a sym-link for sub-domain

since the hostmonster interface won’t let you select a directory outside of public\_html, we are going to create a sym link from the ~/public\_html/redmine folder to ~/rails/redmine. to do this we will be deleting the ~/public_html/redmine directory. the sym link will recreate it.

```cd ~/public_html
rm -R redmine
ln -s ~/rails/redmine/public redmine
```

#### prepare redmine

download the latest final release of redmine (the last one is 1.0.3). extract this to your desktop, you should now have a folder name redmine on your desktop. you need to download the following files : dispatch.rb, dispatch.cgi and dispatch.fcgi and put them in your local copy of redmine.

now edit your database.yml file with the database, username and password you created in step one. you only have to change those three values for production  configuration. to do so copy config/database.yml.example into config/database.yml and edit the latter.

#### upload redmine

via ftp upload your redmine files to your redmine directory.

#### finish the installation

ssh into your server, your going to want to chmod 755 your ~/rails/redmine/public folder.

```
cd ~/rails/redmine
chmod 755 public
```

remove any .htaccess file that may already be in the ~/rails/redmine/public directory.

download file from here: http://acme-tech.net/blog/files/redmine_htaccess.txt  into ~/rails/redmine/public directory and save it as .htaccess.

best way to do this is by typing following set of commands:

```
cd ~/rails/redmine/public
wget
```

http://acme-tech.net/blog/files/redmine_htaccess.txt

```
mv htaccess.txt .htaccess
```

#### generate a session store secret

this is required for versions of redmine above release 0.8.7. redmine stores session data in cookies by default, which requires a secret to be generated. this can be done by running:

```
cd ~/rails/redmine
RAILS_ENV=production rake config/initializers/session_store.rb
```

#### setup the db

we have to give redmine it&#8217;s database structure and default values.

```
cd ~/rails/redmine
RAILS_ENV=production rake db:migrate
```

insert default configuration data in database

```
RAILS_ENV=production rake redmine:load_default_data
```

this step is optional but highly recommended, as you can define your own configuration from scratch. it will load default roles, trackers, statuses, workflows and enumerations.  
as a last thing you need to edit config/environment.rb and add the following lines :

```ruby
ENV['GEM_PATH'] ||= '/ruby/gems:/usr/lib64/ruby/gems/1.8'
ENV['RAILS_ENV'] ||= 'production'
```

**Update**  
since the last update from hostmonster i kep receiving a 500 error. the solution was pretty simple

```
gem uninstall i18n
```

then need to change config/boot.rb, and add 
```require 'thread'```

on the file header  
and change config/environment.rb, adding before 
```Rails::Initializer...```

```ruby
if Gem::VERSION >= "1.3.6"
  module Rails
    class GemDependency
      def requirement
        r = super
        (r == Gem::Requirement.default) ? nil : r
      end
    end
  end
end
```
