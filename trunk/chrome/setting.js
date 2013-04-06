$(function() {
	var bg = chrome.extension.getBackgroundPage();
	$("#txtPortalName").val(bg.setting("PortalName"));

	if(bg.isExtensionAdmin()) {
		$("#pAdminDecription").html("您已经是此应用的管理员，可以访问所有功能。");
		$("#btnDeactivateAdmin").show();
	} else {
		$("#pAdminDecription").html("您不是此应用的管理员，不可访问管理员功能。");
		$("#btnActivateAdmin").show();
	}

	function activateAdmin() {
		var bg = chrome.extension.getBackgroundPage();
		//TODO:加强口令
		if(prompt("请输入管理员口令") == "gmccwebsitesucks") {
			bg.setting(bg.EXTENSION_IS_ADMIN, "true");
			alert("管理员功能开启成功");
			window.location.reload();
		} else {
			alert("管理员口令错误");
		}
	}

	function deactivateAdmin() {
		var bg = chrome.extension.getBackgroundPage();
		if(confirm("确认关闭管理员功能？")) {
			bg.setting(bg.EXTENSION_IS_ADMIN, null);
			alert("管理员功能关闭成功");
			window.location.reload();
		}
	}

	function savePortal() {
		var portalName = $("#txtPortalName").val();
		var portalPwd = $("#txtPortalPwd").val();
		var bg = chrome.extension.getBackgroundPage();
		bg.setting("PortalName", portalName);
		bg.setting("PortalPwd", portalPwd);
		alert("保存成功");
	}

	function settingLogin() {
		var bg = chrome.extension.getBackgroundPage();
		var name = bg.setting("PortalName");
		var pwd = bg.setting("PortalPwd");

		var loginUrl = window.Login.buildUrl(name, pwd);
		window.open(loginUrl);
	}

	function buildUrl() {
		var bg = chrome.extension.getBackgroundPage();
		var name = bg.setting("PortalName");
		var pwd = bg.setting("PortalPwd");

		var loginUrl = window.Login.buildUrl(name, pwd);
		alert(loginUrl);
	}

	$("#btnSave").click(savePortal);
	$("#btnTestLogin").click(settingLogin);
	$("#btnBuilUrl").click(buildUrl);
	$("#btnActivateAdmin").click(activateAdmin);
	$("#btnDeactivateAdmin").click(deactivateAdmin);
	
});