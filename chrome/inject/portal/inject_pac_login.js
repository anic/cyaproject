(function init() {

	var arr = document.getElementsByClassName("login_area");
	if(arr.length == 0)
		return;

	//修改登录框的位置
	arr[0].style["vertical-align"] = "bottom";

	//修改登录框的宽度，使得按钮全部可以显示
	var f = document.getElementById("login-form");
	f.style.width = "260px";

	chrome.extension.sendRequest({
		cmd : "setting",
		args : ["PortalName", "PortalPwd"]
	}, function(response) {
		if(response.result) {
			var txtName = document.getElementById("ext-comp-1002");
			if (txtName.value != response.result[0])
				return;
			
			var txtPwd = document.getElementById("ext-comp-1003");
			txtPwd.value = response.result[1];
		}
		// response.result;
	});
})();
