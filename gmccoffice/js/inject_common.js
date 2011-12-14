//基本类库，提供提示的基本功能

/**
 * log 提示用户信息
 */
window.log = log = function(m, color) {
	color = color ? color : "#68af02";
	var messageBox = document.getElementById("messageBox"), message = document.getElementById("message");
	messageBox.style.filter = "alpha(opacity=100)";
	messageBox.style.visibility = "visible";
	messageBox.style.zIndex = "1000";

	message.style.visibility = "visible";
	//录入内容
	var strHtml = "<div style='background:" + color + "; padding:3px 10px; height:15px; color:#FFFFFF; font-size:13px;'><b>" + m + "</b></div>";
	message.innerHTML = strHtml;
	setTimeout("close()", 2000);
	//调用关闭的时间
}
/**
 * err 显示错误提示
 */
window.err = err = function(m) {
	log(m, "#ef8f00");
}
var _i = 100;
function close() {
	if(_i <= 0) {
		message.style.visibility = "hidden";
		message.style.zIndex = "-1000";

		//还原属性和参数
		_i = 100;
		messageBox.style.filter = "alpha(opacity=100)";
		messageBox.style.visibility = "visible";
		clearTimeout();
		return;
	} else {
		_i--;
		messageBox.style.filter = "alpha(opacity=" + _i + ")";
		//刷新可见度，可见度越来越低
		setTimeout("close()", 10);
		//递归
	}
	return;
}

//
// <div id="messageBox" style="width:200px; height:30px;">
// <div id="message" style="dispaly:none;"></div>
// </div>
(function() {
	var messageBox = document.createElement("div");
	messageBox.id = "messageBox";
	//messageBox.className = "fixed";
	messageBox.style.position = "absolute";
	messageBox.style.top = "10px";
	messageBox.style.left = "10px";
	messageBox.style.zIndex = "-1000";
	messageBox.style.width = "200px";
	messageBox.style.height = "30px";
	messageBox.style.borderRadius = "2px";
	messageBox.style.display = "block";

	var message = document.createElement("div");
	messageBox.appendChild(message);
	message.id = "message";

	document.body.appendChild(messageBox);
})();

