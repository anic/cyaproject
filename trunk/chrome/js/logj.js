//基本类库，提供提示的基本功能，与log.js不同，需要jquery支持

window.Log = {
	/**
	 * log 提示用户信息
	 */
	log : function(m, color) {
		$("#messageBox").show();
		color = color ? color : "#68af02";
		var messageBox = document.getElementById("messageBox"), message = document.getElementById("message");
		messageBox.style.filter = "alpha(opacity=100)";
		messageBox.style.visibility = "visible";
		messageBox.style.zIndex = "1000";
		messageBox.style.left = "10px";

		message.style.visibility = "visible";
		//录入内容
		var strHtml = "<div style='background:" + color + "; padding:3px 10px; height:15px; color:#FFFFFF; font-size:13px;'><b>" + m + "</b></div>";
		message.innerHTML = strHtml;
		
		//调用关闭的时间
		$("#messageBox").fadeOut(2000);		
	},
	/**
	 * err 显示错误提示
	 */
	err : function(m) {
		log(m, "#ef8f00");
	},
	/**
	 * 初始化
	 */
	_init : function() {
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
	}
};

//
// <div id="messageBox" style="width:200px; height:30px;">
// <div id="message" style="dispaly:none;"></div>
// </div>
$(function() {
	window.Log._init();
});
