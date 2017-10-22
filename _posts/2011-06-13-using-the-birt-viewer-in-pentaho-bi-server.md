---
title: using the birt viewer in pentaho bi server
author: gjergj.sheldija
layout: post
permalink: /using-the-birt-viewer-in-pentaho-bi-server/
categories:
  - code
tags:
  - birt
  - birt 2.6
  - java
  - pentaho
  - pentaho 3.6
comments: true
---
the last pentaho bi server v 3.7  has some problems handling birt reports due to old libraries shipped with pentaho. the process of updating is which can be found on the pentaho wiki didn&#8217;t work for me, i was not able to even list the birt reports. after some googling and hacking around i was able to bypass it and use the birt webviewer inside pentaho. since it took me some time to make it work i thought that it might nor be a bad idea to document what i did.  
download birt runtime from [birt runtime]<http://download.eclipse.org/birt/downloads> and extract it somewhere in a temporary directory. copy the WebViewerExample directory in : **/opt/pentaho-3.6/biserver-ce/tomcat/webapps**
edit **/opt/pentaho-3.6/biserver-ce/tomcat/webapps/WebViewerExample/WEB-INF/web.xml** and edit the BIRT\_VIEWER\_WORKING_FOLDER parameter

BIRT_VIEWER_WORKING_FOLDER /opt/pentaho-3.6.0/biserver-ce/pentaho-solutions

restart the pentaho server and test it out on <http://localhost:8080/WebViewerExample>  
if it works, we can continue with step 2.  
download the following archive [birt-plugin.tar][1] into pentaho's system directory  **biserver-ce/pentaho-solutions/system/** and edit **biserver-ce/pentaho-solutions/system/birt-plugin/plugin.xml**

<command>http://localhost:8080/WebViewerExample/frameset?__report={solution}/{path}/{name}</command>

restart the pentaho server.  
and you are ready to go.

if your reports need other jdbc driver expect the supplied jdbc's you can copy them inside **biserver-ce/tomcat/webapps/WebViewerExample/WEB-INF/lib** or **biserver-ce/tomcat/common/lib**

as a last thing, to activate pentaho acl's for birt reports you need to change : **biserver-ce/pentaho-solutions/system/pentaho.xml**

xaction,url,prpt,xdash,xcdf,rptdesign

 [1]: http://acme-tech.net/blog/http://acme-tech.net/blog/wp-content/uploads/2011/06/birt-plugin.tar.gz
