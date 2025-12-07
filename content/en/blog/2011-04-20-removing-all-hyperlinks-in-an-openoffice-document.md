---
title: 'removing all hyperlinks in an <br /> openoffice document'
author: gjergj.sheldija
layout: post
permalink: /removing-all-hyperlinks-in-an-openoffice-document/
categories:
  - code
  - random
tags:
  - hyperlinks
  - openoffice
  - write
comments: true
---
i was having this really huge oo write doc full of hyperlinks..after some hacking and googling i came out with the follwing code..
hope it helps

```bash
Sub Main

    Dim oDoc,FandR,oFound
    oDoc = ThisComponent
    FandR = oDoc.createSearchDescriptor
    FandR.ValueSearch = False
    
    Dim args(0) as new com.sun.star.beans.PropertyValue
    args(0).Name = “HyperLinkEvents”
    args(0).Value = ””
    FandR.SetSearchAttributes(args())
    oFound = oDoc.FindFirst(FandR)
    
    While Not isNull(oFound)
     oFound.HyperLinkURL = ””
     oFound.HyperLinkName = ””
     oFound.HyperLinkTarget = ””
     oFound = oDoc.FindNext(oFound.End,FandR)
    Wend 

End Sub
```
