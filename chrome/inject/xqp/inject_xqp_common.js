//优化AF单无法显示系统的问题
//参考了http://blog.afterthedeadline.com/2010/05/14/how-to-jump-through-hoops-and-make-a-chrome-extension/
(function() {

	// var scriptStr1 = '<script type="text/javascript">(function(l) {   var res = document.createElement("SCRIPT");  res.type = "text/javascript";   res.src = l;   document.getElementsByTagName("head")[0].appendChild(res);})("';
	// var scriptStr2 = '");</script>';
	// var url = chrome.extension.getURL("inject/xqp/inject_xqp_form.js");
	// $('head').append(scriptStr1 + url + scriptStr2);
	var s = document.createElement('script');
	s.setAttribute('type', 'text/javascript');
	var url = chrome.extension.getURL("inject/xqp/inject_xqp_form.js");
	s.setAttribute('src', url);
	document.documentElement.appendChild(s);

	var url = window.location.href.toLowerCase();
	if(url.indexOf("head.aspx") != -1) {
		url = chrome.extension.getURL("inject/xqp/inject_xqp_head.js");
		s = document.createElement('script');
		s.setAttribute('type', 'text/javascript');
		s.setAttribute('src', url);
		document.documentElement.appendChild(s);
	}
})();
