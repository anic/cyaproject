$(function() {
	// var bg = chrome.extension.getBackgroundPage();
	// $("#description").append(bg.gExInfo.description);

	//暂时不开启自动登录
	// window.Login.testLogin(function(result) {
	// if(result) {
	// onLoginSuccess(result);
	// } else {
	// $("#btnLogin").html("<< 请登录  >>");
	// }
	// });

	//屏蔽管理员菜单
	var bg = chrome.extension.getBackgroundPage();
	if(!bg.isExtensionAdmin()) {
		$(".adminMenu").hide();
	}

	function onLoginSuccess(result) {
		if(result) {
			$("#btnLogin").css("color", "green").html("OA已登录")[0].onclick = null;
			$("#btnLogin").append("<img src='image/popup/check.png'>");
		} else {
			$("#btnLogin").css("color", "red").html("登录失败");
		}
	}

	function menuLogin() {
		$("#btnLogin").css("color", "orange").html("登录中...");
		window.Login.testLogin(function(result) {
			if(result) {
				onLoginSuccess(true);
			} else {
				var bg = chrome.extension.getBackgroundPage();
				var name = bg.setting("PortalName");
				var pwd = bg.setting("PortalPwd");
				if(name && pwd) {
					window.Login.login(name, pwd, onLoginSuccess);
				} else
					$("#btnLogin").css("color", "red").html("未设置用户名密码");
			}
		})
	}

	function openTab(url) {
		chrome.tabs.create({
			url : url
		});
	}


	$("#btnLogin").click(menuLogin);
	$("#btnChromeSetting").click(function() {
		openTab('chrome://settings/extensionSettings')
	});
});
