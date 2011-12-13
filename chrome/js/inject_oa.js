/**
 * 1 屏蔽中间弹窗;先使用折中的办法转向空白页
 */

(function init() {

	var target = "middleWindow.jsp";
	var src = window.location.href;

	if(src.indexOf(target) == -1)
		return;

	//window.location.href = "about:blank";
	//return;
	// var s = document.head.children[3];
	// document.head.removeChild(s);
	// document.writeln("");

})();

//http://pac.gmcc.net/smc/template/lib/dishi2/JsonObjects/news/middleWindow.jsp?channelId=DISHI2_middle&url=http%3A%2F%2Fgmccnews.gmcc.net%2Fgetnews.aspx
