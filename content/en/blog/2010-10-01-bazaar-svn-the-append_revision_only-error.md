---
title: bazaar svn, the append_revision_only error
author: gjergj.sheldija
layout: post
permalink: /bazaar-svn-the-append_revision_only-error/
categories:
  - bazaar
  - svn
tags:
  - bazaar
  - bzr
  - svn
---
If you try to push changes from your Bazaar feature branch back to a Subversion repository, and the Subversion repository has been changed since you created your Bazaar branch, you may get something like this:

```bash
 bzr push
 Using saved push location: svn+http://svn/repos/Trunk/MyProject
 bzr: ERROR: Operation denied because it would change the mainline history. Set the append_revisions_only setting to False on branch "svn+http://svn/repos/Trunk/MyProject" to allow the mainline to change.
```

Find subversion.conf. It is located at:

*   Vista/7: C:\Users\your-user-name\AppData\Roaming\bazaar\2.0\
*   XP/2003: C:\Documents and Settings\your-user-name\ApplicationData\bazaar\2.0\

```bash
[4ef181b9-d188-42c4-ae88-5d15bdaece0b]
 locations = svn+http://svn/repos/Trunk/MyProject
 append_revisions_only = False
```