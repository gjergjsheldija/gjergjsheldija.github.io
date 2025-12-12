---
title: deploying code and db migration via phing
author: gjergj.sheldija
layout: post
permalink: /deploying-code-and-db-migration-via-phing/
categories:
  - code
  - hosting
  - php
tags:
  - database
  - deploy
  - migrate
  - phing
---
working on a project hosted on a shared hosting, with limited resources, i had to find a way to update my working copy with the testing and the production server..and after some tinkering this is the result. hope it's usefull

```xml
<?xml version="1.0"?>
<project name="project_sync" basedir="." default="-init">
  <property name="version" value="4.0"/>
  <!-- Public targets -->
  <!-- ============================================ -->
  <!-- Target: sync:list -->
  <!-- ============================================ -->
  <target name="sync:list" description="Public: List files to be synchronized facade">
    <phingcall target="-sync-execute-task">
      <property name="listonly" value="true"/>
    </phingcall>
  </target>
  <!-- ============================================ -->
  <!-- Target: sync -->
  <!-- ============================================ -->
  <target name="sync" description="Public: Synchronize task fasade">
    <phingcall target="-sync-execute-task">
      <property name="listonly" value="false"/>
    </phingcall>
  </target>
  <!-- ============================================ -->
  <!-- Target: db-update -->
  <!-- ============================================ -->
  <target name="db-update" depends="-list-applied-updates" description="Public: The db update facade ">
    <php expression="eval('$list=glob("${sync.source.projectdir}/sql/*.sql"); natsort ($list); return implode(",", $list);');" returnProperty="db.patchfiles"/>
    <phingcall target="-list-applied-updates"/>
    <echo msg="Searching for updates on : ${sync.source.projectdir}/sql"/>
    <foreach param="filename" target="-apply-changelog">
      <fileset dir="${sync.source.projectdir}/sql">
        <include name="${db.patchfiles}"/>
        <excludesfile name="${sync.source.projectdir}/build/results.txt"/>
      </fileset>
    </foreach>
    <delete file="${sync.source.projectdir}/build/results.txt"/>
  </target>
  <!-- Private targets -->
  <!-- ============================================ -->
  <!-- Target: -init -->
  <!-- ============================================ -->
  <target name="-init" description="Private: Load main settings and display main menu">
    <!-- Main Menu -->
    <echo>Welcome to the site Update System</echo>
    <echo>----------------------------------------</echo>
    <echo>1) Development to Test</echo>
    <echo>2) Test to Production</echo>
    <echo>3) Apply db updates</echo>
    <echo>x) Exit</echo>
    <echo>----------------------------------------</echo>
    <input propertyName="choice" validargs="1,2,3,x">Give the corresponding arg</input>
    <if>
      <equals arg1="${choice}" arg2="1"/>
      <then>
        <property file="test.properties"/>
        <phingcall target="sync"/>
      </then>
      <elseif>
        <equals arg1="${choice}" arg2="2"/>
        <then>
          <property file="production.properties"/>
          <phingcall target="sync"/>
        </then>
      </elseif>
      <elseif>
        <equals arg1="${choice}" arg2="3"/>
        <then>
          <property file="database.properties"/>
          <phingcall target="db-update"/>
        </then>
      </elseif>
      <elseif>
        <equals arg1="${choice}" arg2="x"/>
        <then>
          <echo>bye bye!</echo>
          <php expression="exit();"/>
        </then>
      </elseif>
    </if>
    <tstamp/>
  </target>
  <!-- ============================================ -->
  <!-- Target: -update-changelog -->
  <!-- ============================================ -->
  <target name="-update-changelog" description="Private: Updates the changelog table with the applied updates">
    <echo msg="Applying update : ${filename}"/>
    <pdo url="${sync.database.type}:host=${sync.database.host};dbname=${sync.database.name}" userid="${sync.database.user}" password="${sync.database.password}" onerror="continue">INSERT INTO care_changelog( delta ) VALUES ( '${filename}'.sql );</pdo>
    <echo msg="INSERT INTO care_changelog( delta ) VALUES ( '${filename}' );"/>
  </target>
  <!-- ============================================ -->
  <!-- Target: -apply-changelog -->
  <!-- ============================================ -->
  <target name="-apply-changelog" description="Private: Applies the sql changeset">
    <pdo url="${sync.database.type}:host=${sync.database.host};dbname=${sync.database.name}" userid="${sync.database.user}" password="${sync.database.password}" onerror="abort">
      <transaction src="${sync.source.projectdir}/sql/${filename}"/>
    </pdo>
    <phingcall target="-update-changelog"/>
  </target>
  <!-- ============================================ -->
  <!-- Target: -list-applied-updates -->
  <!-- ============================================ -->
  <target name="-list-applied-updates" description="Private: Creates a list of available updates">
    <pdo url="${sync.database.type}:host=${sync.database.host};dbname=${sync.database.name}" userid="${sync.database.user}" password="${sync.database.password}" onerror="stop">
      <formatter type="plain" usefile="true" showheaders="false" coldelim="" outfile="${sync.source.projectdir}/build/results.txt"/>
         SELECT delta FROM `care_changelog` ORDER BY CAST(replace( substring(delta,7,3) , '.' , '' ) AS UNSIGNED);
      </pdo>
    </target>
    <!-- ============================================ -->
    <!-- Target: -sync-execute-task -->
    <!-- ============================================ -->
    <target name="-sync-execute-task" description="Private: Executes the synchronize task">
      <echo msg="Syncing files"/>
      <!-- <if>
        <not>
          <isset property="sync.verbose" />
        </not>
        <then>
          <property name="sync.verbose" value="true" override="true" />
          <echo message="The value of sync.verbose has been set to true" />
        </then>
      </if> -->
    <property name="sync.remote.auth" value="${sync.remote.user}@${sync.remote.host}"/>
    <taskdef name="sync" classname="phing.tasks.ext.FileSyncTask"/>
    <sync sourcedir="${sync.source.projectdir}" destinationdir="${sync.remote.auth}:${sync.destination.projectdir}" excludefile="${sync.exclude.file}" listonly="${listonly}" verbose="${sync.verbose}"/>
  </target>
</project>

```
  
the configuration files are as follows 

```ini [database.properties]
# database connection properties
# to be updated on a server basis
sync.source.projectdir=/home/xxxx/www/website/
sync.database.type=mysql
sync.database.name=database_name
sync.database.host=localhost
sync.database.user=db_user
sync.database.password=db_password
production.properties
```

```ini [production.properties] 
# production server properties
sync.source.projectdir=/var/www/website/
sync.destination.projectdir=/home/client/www/
sync.remote.host=hostname.com
sync.remote.user=remote_user
sync.destination.backupdir=hostname.com/website/backup
sync.exclude.file=/var/www/website/build/sync.exclude
sync.verbose=false 
```

test.properties is identical to production.properties except for the values.


```bash [sync.exclude]
.*/
.buildpath
.project
.hgignore
cache
build
uploads
```

changesets.sql is the table containing the changesets

```sql [changesets.sql]
CREATE TABLE IF NOT EXISTS `changelog` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `delta` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
```
