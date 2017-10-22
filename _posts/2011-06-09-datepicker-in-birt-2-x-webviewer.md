---
title: datepicker in birt 2.x webviewer
author: gjergj.sheldija
layout: post
permalink: /datepicker-in-birt-2-x-webviewer/
categories:
  - java
  - birt
tags:
  - birt
  - datepicker
comments: true
---
birt is a really nice tool and the webviewer is great. it lacks a a very simple feature thou, the datepicker when entering parameters.. 
implementing it was a very straightforward process. 
first download [dynarch's calendar]<www.dynarch.com/projects/calendar> and extract it somewhere, you will just need the contents of the src folder 
now locate and open **FramesetFragment.jsp** in **WebViewerExample/webcontent/birt/pages/layout** 
and **TextBoxParameterFragment.jsp** in **WebViewerExample/webcontent/birt/pages/parameter**
now in the **FramesetFragment.jsp** insert those lines before the closing head tag

{% codeblock lang:html %}
    <link href="birt/calendar/css/jscal2.css" rel="stylesheet" type="text/css"></link >
    <link href="birt/calendar/css/border-radius.css" rel="stylesheet" type="text/css"></link>
    <link href="birt/calendar/css/win2k/win2k.css" rel="stylesheet" type="text/css"></link>
    <script src="birt/calendar/js/jscal2.js" type="text/javascript"></script>
    <script src="birt/calendar/js/lang/en.js" type="text/javascript"></script>
{% endcodeblock %}

and in TextBoxParameterFragment.jsp just after

{% codeblock lang:html %}
<INPUT TYPE="HIDDEN" ID="isRequired" VALUE = "<%= parameterBean.isRequired( )? "true": "false" %>">
{% endcodeblock %}

replace

{% codeblock lang:html %}
 <INPUT TYPE="HIDDEN" ID="isRequired" VALUE = "<%= parameterBean.isRequired( )? "true": "false" %>">
{% endcodeblock %}

with

{% codeblock lang:html %}
<INPUT TYPE="HIDDEN" ID="isRequired"
            VALUE = "<%= parameterBean.isRequired( )? "true": "false" %>">

        <%
    if (parameterBean.getParameter().getDataType()==7 || parameterBean.getParameter().getDataType()==4) {
    %>
      <button id="<%=parameterBean.getName()%>_button">...</button>
      <script type="text/javascript">
        Calendar.setup({
          trigger     : '<%=parameterBean.getName()%>_button',
          inputField  : '<%=parameterBean.getName()%>',
          showTime    : 12,
          onSelect    :function () { this.hide() }
        });
      </script>
     <%
     }
     %>


    </TD>
</TR>
{% endcodeblock %}

you may have noticed that i have extracted the contents of the src folder into **WebViewerExample/webcontent/birt/calendar**

well..that's it, hope you appreciate it
