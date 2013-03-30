//优化AF单无法显示系统的问题
//参考了http://blog.afterthedeadline.com/2010/05/14/how-to-jump-through-hoops-and-make-a-chrome-extension/
(function() {
	var scriptStr1 = '<script type="text/javascript">(function(l) {   var res = document.createElement("SCRIPT");  res.type = "text/javascript";   res.src = l;   document.getElementsByTagName("head")[0].appendChild(res);})("';
	var scriptStr2 = '");</script>';
	var url = chrome.extension.getURL("inject/xqp/inject_xqp_form.js");
	jQuery('head').append(scriptStr1 + url + scriptStr2);

	var url = window.location.href.toLowerCase();
	if(url.indexOf("head.aspx") != -1) {
		url = chrome.extension.getURL("inject/xqp/inject_xqp_head.js");
		jQuery('body').append(scriptStr1 + url + scriptStr2);
	}
})();
