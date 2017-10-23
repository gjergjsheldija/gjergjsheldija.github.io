---
title: user friendly selects in birt
author: gjergj.sheldija
layout: post
permalink: /user-friendly-selects-in-birt/
categories:
  - code
  - sql
  - birt
  - javascript
  - jquery
  - chosen
tags:
  - code
  - sql
  - birt
  - javascript
  - jquery
  - chosen
comments: true
---    
a very straightforward post on how to add the chosen plugin to select boxes in birt.
first download the chosen plugin from https://harvesthq.github.io/chosen/ and extract the files in webcontent/birt/js.
then edit webcontent/birt/pages/layout/FramesetFramgment.jsp and add
```html
<link rel="stylesheet" href="birt/js/chosen.min.css">
<script src="birt/js/jquery-1.9.1.min.js" type="text/javascript"></script>
<script src="birt/js/chosen.jquery.min.js" type="text/javascript"></script>
<script>
var $jQuery = jQuery.noConflict();
</script>
```

and webcontent/birt/pages/parameter/ComboBoxParameterFragment.jsp and add the following code at the end of  the file
```javascript
<script>
var setInt;
$jQuery("#<%= encodedParameterName + "_selection"%>")
	.chosen({
		disable_search_threshold: 10, 
		width: "400px"
	})
	.change(function() {
		birtParameterDialog.__refresh_cascade_select($("<%= encodedParameterName + "_selection"%>"));
		window.setTimeout(function() {
			$jQuery('.birtviewer_parameter_dialog_Select').trigger('chosen:updated');
		}, 100);
});
</script>
```

