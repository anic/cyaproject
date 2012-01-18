function init() {

	var src = window.location.href;
	
	//http://dynamic.12306.cn/otsweb/loginAction.do?method=init
	if(src.indexOf("loginAction.do") == -1) {
		return;
	}
	
	var txtUsr = document.getElementById("UserName");
	txtUsr.value = "zsn04liulang";
	
	var txtPwd = document.getElementById("password");
	txtPwd.value = "maryzhao";
	
	var txtCode = document.getElementById("randCode");
	txtCode.onkeyup = function(e)
	{
		if(e.keyCode == 32)//space
		{
			var form = document.getElementById("loginForm");
			form.submit();
			return false;
		}
		
	};
	
	$("#randCode").focus();
	
}

init();
