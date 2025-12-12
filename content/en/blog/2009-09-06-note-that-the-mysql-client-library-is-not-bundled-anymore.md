---
title: Note that the MySQL client library is not bundled anymore!
author: admin
layout: post
permalink: /note-that-the-mysql-client-library-is-not-bundled-anymore/
categories:
  - code
tags:
  - client
  - library
  - mysql
---
Unable to get PHP configured to my specifications using the Ubuntu repositories, I decided to install it from source. However, I kept getting the error:

> Note that the MySQL client library is not bundled anymore!

Not wanting to install MySQL from source, I found a package in the Ubuntu repositories that installed the necessary library files.

> sudo apt-get install libmysqlclient15-dev

After I installed that package, <span>PHP</span> was able to install successfully.
