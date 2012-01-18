/**
 * 邮件内容
 */
//http://gzmail.gmcc.net/shareRes.nsf/Portal_Mail_web_sgs
//http://gzmail.gmcc.net/shareRes.nsf/GetMailList_sgs?OpenAgent&MailDbPath=mail\chengyaoan.nsf&MailBox=($Inbox)&CurPage=1
/**
 *
 */
(function() {
	var url=window.location.href;
	var target="http://gzmail.gmcc.net/shareRes.nsf/";
	if(url.indexOf(target)==-1)
		return;
		
	var pageList = document.getElementById("pageList");
	if (pageList)
	{
		pageList.onmouseover = function(){};
		pageList.onclick = function(){};
		pageList.onout = function(){};
	}

})();
