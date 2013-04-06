//登录OA的库，需要用到Jquery

window.Login = {
	buildUrl : function(name, pwd) {
		var loginUrl = "https://pac-am.gmcc.net/amserver/UI/Login?goto=http://pac.gmcc.net/portal/dt?provider=DISHI_Portal";
		loginUrl += "&Login.Token1=" + name;
		loginUrl += "&Login.Token2=" + encodeURIComponent(pwd);
		loginUrl += "&module=LDAP";

		return loginUrl;
	},
	testLogin : function(callback) {
		$.ajax({
			type : "GET",
			url : "http://pac.gmcc.net/portal/dt",
			success : function(msg) {
				callback = callback ? callback : function(result) {alert(result)
				};
				if(msg.match(/redirectToDesktop/g)) {
					callback(false);
				} else {
					callback(true)
				}
			},
			error : function() {
				callback(false);
			}
		});

	},
	login : function(name, pwd, callback) {
		var loginUrl = Login.buildUrl(name, pwd);
		// alert(loginUrl);
		var divBackApp = document.getElementById("divBackApp");
		if(!divBackApp) {
			$("body").append('<div id="divBackApp" style="position: absolute;left:-10px;"></div>');
		}
		callback = callback ? callback : function() {alert("已登录！");
		};
		var frLogin = $("<iframe id='frLogin' src='" + loginUrl + "' style='width:1px;height;1px;position:absolute;'/>").load(function() {
			Login.testLogin(function(result) {
				if(result) {
					$("#divBackApp").empty();
					callback(true);
				} else
					callback(false);
			});
		});

		$("#divBackApp").append(frLogin);
	}
};
