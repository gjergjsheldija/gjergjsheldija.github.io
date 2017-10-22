---
title: samba and ldap
author: gjergj.sheldija
layout: post
permalink: /samba-and-ldap/
categories:
  - hosting
  - ubuntu
tags:
  - ldap
  - network
  - samba
  - ubutu
comments: true
---

_i found this online, and forgot the url where i copied it. so if you are the
author or know the original url, please leave it in the commends and i'll
gladly link it._

Hi all,

Hi everyone, after digging over the net and after spending a lot of time
trying to understand how things work, I'm proud to present a very quick and
super easy tutorial to create a Samba Primary Domain Controller with LDAP
integration inside Ubuntu 10.04, both 32bit and 64bit.

In less than 30 minutes you'll have:
- A fully working PDC for Windows Clients
- Roaming profiles NOT enabled (this is what most of you want)
- Be able to have shared folders automatically mounted when a user logs into the domain
- Tested and fully working with(all flavours): Windows XP, Windows Vista and even Windows 7!

If you do everything exactly like I wrote I guarantee it will work. One single
error can compromise everything and you'll have to restart from the beginning!
You have been warned!

General Information before reading:
- In this guide each step will have a number, so if you ever have to ask me a question be sure you point the exact number, I will ignore any posts without the number being explicited.
- Commands you must type start with a "->".
- The guide presumes you know how to use Nano text editor (or any other text editor from shell like Vim).
- In this guide my default password is always "pwd123″.

Let's Start.

1)

Install Ubuntu Server 10.04 32Bit or 64Bit
Once Ubuntu 10.04 is up, log with root user:

sudo su

From now on I assume you are always root user.

2)

Set a static IP, in this example the NIC card is eth0 and the network is part of 192.168.1.x class.

nano /etc/network/interfaces

{% codeblock lang:bash %}
auto lo eth0
iface lo inet loopback
iface eth0 inet static
address 192.168.1.10
broadcast 192.168.1.255
netmask 255.255.255.0
gateway 192.168.1.1
{% endcodeblock %}

3)

{% codeblock lang:bash %}
/etc/init.d/networking restart  
ifconfig
{% endcodeblock %}

The output should show you the static IP, try pinging a local IP or an
internet IP to be sure you are on the net, ex:

ping www.google.it

or try pinging your gateway set before:

ping 192.168.1.1

If you are unsure, reboot your machine to see if "ifconfig" command still shows you the same IP and to be sure you're still part of the network by
pinging as said before.

ONCE YOU FINISHED WITH THIS GUIDE, IF YOU EVER CHANGE YOUR IP BE SURE TO READ SECTION: "TIPS AND TRICKS", FOUND AT THE END OF THIS GUIDE OR YOUR PDC WILL
STOP WORKING.

4)

{% codeblock lang:bash %}
apt-get update  
apt-get dist-upgrade  
reboot  
sudo su
{% endcodeblock %}

5)

{% codeblock lang:bash %}
apt-get install slapd ldap-utils  
ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/cosine.ldif  
ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/nis.ldif  
ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/ldap/schema/inetorgperson.ldif
{% endcodeblock %}

6)

backend.example.com.ldif

Your next step will be to modify this file, the only thing you should care of changing is the password, which is set at line "olcRootPW:". By default password is "pwd123″.

nano backend.example.com.ldif

{% codeblock lang:bash %}
dn: cn=module,cn=config
objectClass: olcModuleList
cn: module
olcModulepath: /usr/lib/ldap
olcModuleload: back_hdb
dn: olcDatabase=hdb,cn=config
objectClass: olcDatabaseConfig
objectClass: olcHdbConfig
olcDatabase: {1}hdb
olcSuffix: dc=pdc
olcDbDirectory: /var/lib/ldap
olcRootDN: cn=admin,dc=pdc
olcRootPW: pwd123
olcDbConfig: set_cachesize 0 2097152 0
olcDbConfig: set_lk_max_objects 1500
olcDbConfig: set_lk_max_locks 1500
olcDbConfig: set_lk_max_lockers 1500
olcDbIndex: objectClass eq
olcLastMod: TRUE
olcDbCheckpoint: 512 30
olcAccess: to attrs=userPassword by dn="cn=admin,dc=pdc" write by anonymous
auth by self write by * none
olcAccess: to attrs=shadowLastChange by self write by * read
olcAccess: to dn.base="" by * read
olcAccess: to * by dn="cn=admin,dc=pdc" write by * read
{% endcodeblock %}

7)

From now on, if ldap commands similar to this ask for a password, put password set above in step 6, by default in this guide as said "pwd123″.

{% codeblock lang:bash %}
ldapadd -Y EXTERNAL -H ldapi:/// -f backend.example.com.ldif
{% endcodeblock %}

8)

{% codeblock lang:bash %}
apt-get install samba samba-doc libpam-smbpass smbclient smbldap-tools
{% endcodeblock %}

9)

Now I'll make you download my samba configuration file.

{% codeblock lang:bash %}
wget http://acme-tech.net/blog/http://acme-tech.net/blog/wp-content/uploads/2012/10/smb.conf_.txt
{% endcodeblock %}

After downloading it, you'll have to change ONLY two values: "workgroup = "
and "netbios = ".

Workgroup is the name of the Domain. This is the name that you'll have to
enter in a Windows client to make it join the domain. Netbios is instead the
name used to browse shared folders, for example in Windows you'll put
"\\$netbiosname\$shared_folder".

DO NOT PUT WORKGROUP NAME IDENTICAL TO NETBIOS NAME.

IMPORTANT: carefully decide the NETBIOS name, once you change it YOU CAN'T
CHANGE IT AGAIN OTHERWISE IT WILL BREAK EVERYTHING! YOU'VE BEEN WARNED.

Type the following and change the two values.

{% codeblock lang:bash %}
nano smb.conf
{% endcodeblock %}

Once you changed the two values type:

{% codeblock lang:bash %}
cp -rf smb.conf /etc/samba/smb.conf
{% endcodeblock %}

10)

In the next command it will prompt you to put a password, this must be the
same as set before in step 6, by default in this guide "pwd123″

{% codeblock lang:bash %}
smbpasswd -W
{% endcodeblock %}

11)

{% codeblock lang:bash %}
ervice smbd restart
{% endcodeblock %}

12)

Now you must check that samba is running, it will ask you for a password, just
hit Enter.

{% codeblock lang:bash %}
smbclient -L localhost
{% endcodeblock %}

It should not give you any errors, instead it must show some stuff and you
should see your Workgroup Name set in step 9

13)

{% codeblock lang:bash %}
mkdir -v /var/lib/samba/profiles  
chmod 777 /var/lib/samba/profiles  
mkdir -v -p /var/lib/samba/netlogon  
chmod 777 /var/lib/samba/netlogon  
cp /usr/share/doc/samba-doc/examples/LDAP/samba.schema.gz /etc/ldap-&gt; /schema/  
gzip -d /etc/ldap/schema/samba.schema.gz
{% endcodeblock %}

14)

{% codeblock lang:bash %}
schema_convert.conf  
nano schema_convert.conf
{% endcodeblock %}

{% codeblock lang:bash %}
include /etc/ldap/schema/core.schema
include /etc/ldap/schema/collective.schema
include /etc/ldap/schema/corba.schema
include /etc/ldap/schema/cosine.schema
include /etc/ldap/schema/duaconf.schema
include /etc/ldap/schema/dyngroup.schema
include /etc/ldap/schema/inetorgperson.schema
include /etc/ldap/schema/java.schema
include /etc/ldap/schema/misc.schema
include /etc/ldap/schema/nis.schema
include /etc/ldap/schema/openldap.schema
include /etc/ldap/schema/ppolicy.schema
include /etc/ldap/schema/samba.schema
{% endcodeblock %}

15)

{% codeblock lang:bash %}
mkdir /tmp/ldif_output  
slapcat -f schema_convert.conf -F /tmp/ldif_output -n0 -s "cn={12}samba,cn=schema,cn=config" > /tmp/cn=samba.ldif
{% endcodeblock %}

16)

Now you'll have to edit a file, open the file with the following command and
read below to understand what must be edited.

{% codeblock lang:bash %}
nano /tmp/cn\=samba.ldif
{% endcodeblock %}

At the very top you'll see:

dn: cn{12}=samba,cn=schema,cn=config

Change it to:

dn: cn=samba,cn=schema,cn=config

Always at the top you'll see:

cn: {12}samba

Change it to: 

cn: samba

At the end of the file you'll see:
{% codeblock lang:bash %}
structuralObjectClass: olcSchemaConfig
entryUUID: b53b75ca-083f-102d-9fff-2f64fd123c95
creatorsName: cn=config
createTimestamp: 20080827045234Z
entryCSN: 20080827045234.341425Z#000000#000#000000
modifiersName: cn=config
modifyTimestamp: 20080827045234Z
{% endcodeblock %}

Delete all those lines, save and close.

17)

Be sure the following command does not give errors:

{% codeblock lang:bash %}
ldapadd -Y EXTERNAL -H ldapi:/// -D cn=admin,cn=config -W -f /tmp/cn\=samba.ldif
{% endcodeblock %}

18)

{% codeblock lang:bash %}
samba_indexes.ldif  
nano samba_indexes.ldif

dn: olcDatabase={1}hdb,cn=config
changetype: modify
add: olcDbIndex
olcDbIndex: uidNumber eq
olcDbIndex: gidNumber eq
olcDbIndex: loginShell eq
olcDbIndex: uid eq,pres,sub
olcDbIndex: memberUid eq,pres,sub
olcDbIndex: uniqueMember eq,pres
olcDbIndex: sambaSID eq
olcDbIndex: sambaPrimaryGroupSID eq
olcDbIndex: sambaGroupType eq
olcDbIndex: sambaSIDList eq
olcDbIndex: sambaDomainName eq
olcDbIndex: default sub
{% endcodeblock %}

19)

Be sure the following does not give any errors.

{% codeblock lang:bash %}
ldapmodify -Y EXTERNAL -H ldapi:/// -D cn=admin,cn=config -W -f samba_indexes.ldif
{% endcodeblock %}

20)

Now thanks to the following command, you'll finally understand if everything
till now went fine. If everything goes fine, it will output a lot of stuff,
including at the end strings similar to the ones found in step 18

{% codeblock lang:bash %}
ldapsearch -Y EXTERNAL -H ldapi:/// -D cn=admin,cn=config -b cn=config -W olcDatabase={1}hdb
{% endcodeblock %}

21)

Now that ldap is working perfectly, we must also be sure Samba is working too.
The following command MUST not give errors, and it must output something similar to this:

{% codeblock lang:bash %}
SID for domain DOMAIN is: S-1-5-21-908678672-1104131578-2020688504
{% endcodeblock %}

So this is the command to type:

{% codeblock lang:bash %}
net getlocalsid
{% endcodeblock %}

22)

{% codeblock lang:bash %}
gzip -d /usr/share/doc/smbldap-tools/configure.pl.gz
{% endcodeblock %}

23)

Next command is crucial to make Samba and Ldap work together. When prompted,
press always Enter without inserting anything. There are only two cases where
you must type something.
When it asks for "Logon Home" and "Logon Path", put a "." character.
At a certain point, it will ask you for a password two times, once for ldap
bind master and then for ldap bind slave. In both cases, you must put the
exact same password you put in step 6, by default in this guide "pwd123″.
So now you know what to do, this is the command:

{% codeblock lang:bash %}
perl /usr/share/doc/smbldap-tools/configure.pl
{% endcodeblock %}

24)

Following command should create some groups, at the end it will ask for a
password. As always put password provided in step 6, default of this guide is
"pwd123″.

{% codeblock lang:bash %}
smbldap-populate
{% endcodeblock %}

25)
{% codeblock lang:bash %}
/etc/init.d/slapd stop  
slapindex  
chown openldap:openldap /var/lib/ldap/*  
/etc/init.d/slapd start
{% endcodeblock %}

26)

If everything till now is really working, the next command will make user
"root" be a Domain Administrator.
In section "Tips and Tricks" you'll see how to make other users be a Domain
admin.
THIS COMMAND MUST NOT GIVE ERRORS, otherwise it means LDAP is not working with
Samba.

{% codeblock lang:bash %}
smbldap-groupmod -m 'root' 'Administrators'
{% endcodeblock %}

27)

In the next command, it will ask you for some stuff. Do not make errors here!
When it asks for questions that want a Yes/No reply, just press Enter leaving
default.

When it asks for LDAP server Uniform Resource Identifier, leave it as it is "ldapi:///"
When it asks for Distinguished name of the search base, put "dc=pdc"
When it asks for LDAP account for root, put "cn=admin, dc=pdc"
When it asks for LDAP password, put the same set in step 6, default of this
guide was "pwd123″

The command is:

{% codeblock lang:bash %}
apt-get --yes install ldap-auth-client
{% endcodeblock %}

IMPORTANT: if you do a mistake, you can reconfigure the previous command
typing:


{% codeblock lang:bash %}
dpkg-reconfigure ldap-auth-config
{% endcodeblock %}

28)

{% codeblock lang:bash %}
auth-client-config -t nss -p lac_ldap
{% endcodeblock %}

29)

The following command is used to enable Unix, Ldap and Samba authentication.
Be sure all of them are selected with "*" character and press Enter.
The command is:

{% codeblock lang:bash %}
pam-auth-update ldap
{% endcodeblock %}

30)

The following command should output something similar to this:

{% codeblock lang:bash %}
Domain Admins:*:512:root
Domain Users:*:513:
Domain Guests:*:514:
Domain Computers:*:515:
Administrators:*:544:root
Account Operators:*:548:
Print Operators:*:550:
Backup Operators:*:551:
Replicators:*:552:
{% endcodeblock %}
  
The command is:

{% codeblock lang:bash %}
getent group
{% endcodeblock %}

31)
{% codeblock lang:bash %}
reboot
{% endcodeblock %}

32)

Good, we're done. After reboot, let's check that everything is working by
creating a user.

{% codeblock lang:bash %}
sudo su
{% endcodeblock %}

If the following command does not give errors, it means Samba and Ldap are
both working together, and you should be happy! It will ask for a password,
the password is the password you want for the user, in this case for user
"user1″:

{% codeblock lang:bash %}
smbldap-useradd -a -m -P user1
{% endcodeblock %}

33)

If you reached this step without errors, it means you are ready to make your
Windows Clients join the domain.

However for security reasons it's not a good idea to make your customer know
the password of "root" account. At the moment, to make a Windows Client join
the domain you'll have to put user "root" and its password, let's instead make
another user which will be part of the Domain Administrators. We'll call the
user "adminpdc".

{% codeblock lang:bash %}
smbldap-useradd -a -m -P adminpdc  
smbldap-groupmod -m ' adminpdc' 'Administrators'  
smbldap-groupmod -m ' adminpdc' 'Domain Admins'  
sudo auth-client-config -t nss -p lac_ldap
{% endcodeblock %}

Good, now we have user "adminpdc" that is a Domain Administrator but is in no
way a possible security danger for your Linux machine, since it's not part of
sudoers. In this way you'll never have to use account "root" to make a Windows
client join the domain or to make changes to the Windows client OS.

Finally, make your Windows Client (xp,vista,7) join the domain! :
- In Windows XP, right click on Computer->Properties and click on Change as seen here: http://www.iaji.net/wp-content/uploa…uter_name3.png
- For Windows Vista and 7 instead, right click on Computer, on the left click on Advanced Settings and then click on "Change" under "Computer Name" Tab.

IMPORTANT ABOUT WINDOWS 7:
To make Windows 7 be part of the domain, read below section Tips and Tricks.
- As domain, put the workgroup name you set in step 9
- When it asks for username and password, put "adminpdc" and the password of this user, you set this on step 33. If everything goes well it will say you joined the domain and you must reboot.

That's all!
TIPS AND TRICKS:
Create/Delete/Manage Users:
To Add: smbldap-useradd -a -m -P user
To Delete: smbldap-userdel user
To ChangePassword: smbldap-passwd user
To add a Domain Administrator:

{% codeblock lang:bash %}
smbldap-groupmod -m 'user' 'Administrators'
smbldap-groupmod -m 'user' 'Domain Admins'
auth-client-config -t nss -p lac_ldap
{% endcodeblock %}

If you ever change the static IP of the PDC:

{% codeblock lang:bash %}
service smbd stop
rm /var/cache/samba/browse.dat
rm /var/cache/samba/login_cache.tdb
rm /var/lib/samba/wins.dat
reboot
{% endcodeblock %}

To make Windows 7 join the domain:
- Check : https://bugzilla.samba.org/attachmen…88&action=view

To make your PDC automatically map net drives:

{% codeblock lang:bash %}
apt-get install flip  
/var/lib/samba/netlogon/allusers.bat
{% endcodeblock %}

In this example you'll have a shared folder for all users, of course you can edit /etc/samba/smb.conf to create specific user shares.

{% codeblock lang:bash %}
mkdir -p /var/lib/samba/shared/  
chmod -R 777 /var/lib/samba/shared/  
nano /var/lib/samba/netlogon/allusers.bat
{% endcodeblock %}

NOTE: change "PSAMBA" with the Netbios name set in step 9. Change drive "m:" to any letter you prefer.

{% codeblock lang:bash %}
@echo off
net use m: /delete
net use m: "\\PSAMBA\shared"
> flip -m /var/lib/samba/netlogon/allusers.bat
{% endcodeblock %}
