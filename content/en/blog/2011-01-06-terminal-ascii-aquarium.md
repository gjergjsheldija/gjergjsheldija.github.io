---
title: terminal ASCII aquarium
author: gjergj.sheldija
layout: post
permalink: /terminal-ascii-aquarium/
categories:
  - code
  - linux
  - random
  - ubuntu
tags:
  - linux fun
---
ASCIIQuarium is an aquarium/sea animation in ASCII art created using perl. to install it just follow those steps :

#### Term::Animation

```bash
$ sudo apt-get install libcurses-perl
$ cd /tmp
$ wget http://search.cpan.org/CPAN/authors/id/K/KB/KBAUCOM/Term-Animation-2.4.tar.gz
$ tar -zxvf Term-Animation-2.4.tar.gz
$ cd Term-Animation-2.4/
$ perl Makefile.PL && make && make test
$ sudo make install
```

#### ASCIIQuarium

```bash
$ cd /tmp
$ wget http://www.robobunny.com/projects/asciiquarium/asciiquarium.tar.gz
$ tar -zxvf asciiquarium.tar.gz
$ cd asciiquarium_1.0/
$ sudo cp asciiquarium /usr/local/bin
$ chmod 0755 /usr/local/bin/asciiquarium
```

run it

```bash
$ /usr/local/bin/asciiquarium
```

or

```bash
perl /usr/local/bin/
```

[<img class="alignnone size-medium wp-image-195" title="asciiquarium" src="http://acme-tech.net/blog/wp-content/uploads/2011/01/asciiquarium-580x442.png" alt="asciiquarium" data-recalc-dims="1" />][1]

 [1]: http://i1.wp.com/acme-tech.net/blog/http://acme-tech.net/blog/wp-content/uploads/2011/01/asciiquarium.png
