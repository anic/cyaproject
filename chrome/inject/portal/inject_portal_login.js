/**
 1 自动登录portal
 */

$(function() {
	chrome.extension.sendRequest({
		cmd : "setting",
		args : ["PortalName", "PortalPwd"]
	}, function(response) {
		if(response.result) {
			form = $("<form></form>");
			form.attr('action', 'https://pac-am.gmcc.net/amserver/UI/Login');
			form.attr('method', 'post');
			input1 = $("<input type='text' name='Login.Token1' value='" + response[0] + "' />");
			input2 = $("<input type='text' name='Login.Token2' value='" + response[1] + "' />");
			input3 = $("<input type='text' name='module' value='LDAP' />")
			input4 = $("<input type='text' name='goto' value='http://contacts.services.gmcc.net/UserInfoSimple.aspx?nid=61ca46b7-0b76-41ae-9e1a-cd9adba8c86c&sid=11&f=app' />")
			form.append(input1);
			form.append(input2);
			form.append(input3);
			form.append(input4);
			form.appendTo("body");
			form.css('display', 'none');
			form.submit();

			window.log("自动登录Portal...");
			return;
		}

		window.err("无法自动登录");
		return;

		// response.result;
	});
})