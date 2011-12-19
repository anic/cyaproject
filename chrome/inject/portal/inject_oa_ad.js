/**
 * 广告内容
 */

//http://ad.services.gmcc.net//Modules/ADUrlPage/RollAdPage.aspx?nid=a24224cf-b278-4361-995e-f33019106ab2&sysid=&sid=16&adId=26a5680d-b8fd-48a5-bd2d-d24883509fd4

/**
 * 1 屏蔽中间弹窗;先使用折中的办法转向空白页
 */
(function init() {

	//TODO: 临时停用
	return;

	var target = "http://ad.services.gmcc.net//Modules/ADUrlPage/RollAdPage.aspx";
	var src = window.location.href;

	if(src.indexOf(target) == -1)
		return;

	// window.location.href= "about:blank";
	// return;
	// alert(document.body.innerHTML);
	var bodyContent = document.body.innerHTML;
	var headContent = document.head.innerHTML;

	var headElement = document.getElementsByTagName("head")[0];

	var links = headElement.getElementsByTagName("link");
	var scripts = headElement.getElementsByTagName("script");

	var linkHrefs = [], scriptSrc = [], scriptContent = [];
	for(var i in links) {
		if(links[i].href)
			linkHrefs.push(links[i].href);
	}

	for(var i in scripts) {
		if(scripts[i].src)
			scriptSrc.push(scripts[i].src);
		else
			scriptContent.push(scripts[i].innerHTML);
	}

	//这句话会覆盖body和head的所有内容
	document.writeln(bodyContent);
	headElement = document.getElementsByTagName("head")[0];

	for(var i in linkHrefs) {
		window.loadjscssfile(linkHrefs[i], "css");
	}

	for(var i in scriptSrc) {
		window.loadjscssfile(scriptSrc[i], "js");
	}

	for(var i in scriptContent) {
		window.loadjscssfile(scriptContent[i]);
	}

	return;

})();
