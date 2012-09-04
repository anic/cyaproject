通信录的返回格式

通信录查询格式：


POST http://contacts.services.gmcc.net/UserInfoSimple.aspx?nid=61ca46b7-0b76-41ae-9e1a-cd9adba8c86c&sid=11&f=app HTTP/1.1
__CALLBACKID	__Page
__CALLBACKPARAM	chengyaoan#0#
__EVENTVALIDATION	/wEWAwLMrLGHCgLEhISFCwLytKiXDBvNvvikkUDhcvNY7VWyxeI3WvrS
__EVENTTARGET	
__EVENTARGUMENT	
__VIEWSTATE	/wEPDwULLTExMTE4NjQ2NzcPFgIeEVJpZ2h0Q29udGFjdHNOb2RlMrYBAAEAAAD/////AQAAAAAAAAAMAgAAAEZHQ1AuRGF0YS5Db21tb24sIFZlcnNpb249MS4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBQEAAAAmR0NQLkRhdGEuQ29tbW9uLkNvcmUuUmlnaHRDb250YWN0c05vZGUDAAAAB19tYW5hZ2ULX2dyb3VwVmlzaXQGX3Zpc2l0AAAAAQEBAgAAAAABAQtkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQhpYlNlYXJjaP13wAgoQ8PxOIwxG7hR7aPTALig
txtName	



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<title>系统登录</title>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<meta http-equiv="Expires" CONTENT="-1">

<meta http-equiv="Cache-Control" CONTENT="no-store">

<meta http-equiv="Pragma" CONTENT="no-cache">



<link href="/sso/themes/default/style.css" rel="stylesheet" type="text/css" />

<script src="/sso/scripts/jquery.js" type="text/javascript"></script>

<script src="/sso/scripts/jquery.utils.js"

	type="text/javascript"></script>

<script type="text/javascript">

	(function() {

		window.history.go(1);

		return false;

	})();

</script>


	<link href="/sso/views/default/style.css" media="screen" rel="stylesheet" type="text/css">
	<script src="/sso/views/default/login.js" type="text/javascript"></script>
 

	<link href="/sso/views/default/images/login.css" media="screen" rel="stylesheet" type="text/css">
 

		<script type="text/javascript">
    	$(document).ready(function(){
			$('#username').focus().enterkeydown(function(){
				doSubmit();
			});
			$('#password').enterkeydown(function(){
				doSubmit();
			});
        });
	</script>
</head>
<body scroll="no">

  
  
  
  <!--<div id="customlogo">
      <img src="/sso/views/default/images/bg_logo.gif">
  </div>
-->
    <!--<div id="logins">
 -->

	  
    <form action="http://services.gmcc.net:80/sso/openid?openid.mode=checkid_setup&openid.return_to=http%3a%2f%2fcontacts.services.gmcc.net%2fopenid%2flogin%3freturnUrl%3d%252fUserInfoSimple.aspx%253fnid%253d61ca46b7-0b76-41ae-9e1a-cd9adba8c86c%2526sid%253d11%2526f%253dapp%26openid.ext.pre_openid_mode%3dcheckid_setup%26openid.ext.sessionid%3dyah5j4jgn44wz3v4ksi2l245%26timemillis%3d129889049571968750&openid.assoc_handle=6f4a21b06557488194fd9649eb55e99d&openid.logout_url=http%3a%2f%2fcontacts.services.gmcc.net%2fopenid%2flogout%3fjsessionid%3dyah5j4jgn44wz3v4ksi2l245&openid.ext.sessionid=yah5j4jgn44wz3v4ksi2l245&openid.ext.login_view_type=built-in&openid.signed=return_to%2clogout_url%2cassoc_handle%2cext.login_view_type&openid.sig=KIkPCzCdF1gy%2bRedyJL9Sg%2fFL8Y%3d&secret_key=RChJgQLShezKdnFGfYxGxPk4GBclSKZP&secret_alg=HmacSHA1" method="post">
       <input type="hidden" name="LoginForm" value="yes"/>
 
    
    	 <table width="100%" cellpadding="0" cellspacing="0" height="100%">
			<tr>
				<td height="100%" align="center">
				<div class="lgn_body">
				<div class="lgn_fim_mg2">
				<table cellSpacing="0" cellPadding="0" border="0">
											<tr>
												<td class="lgn_fim_l">帐号类型：</td>
												<td class="lgn_fim_r">
												<select id="loginType" name="loginType" style="width:195px;ime-mode:disabled;">
													<option value="PortalAccount">PORTAL帐户</option><option value="DefaultAccount">本地帐户</option>
													
													
													
												</select>
												</td>
											</tr>
											<tr>
												<td class="lgn_fim_l">用&nbsp;户&nbsp;名(U)：</td>
												<td class="lgn_fim_r">
													<input type="text" id="username" name="username" class="com_textbox" style="width:195px; ">
												</td>
											</tr>
											<tr>
												<td class="lgn_fim_l">密&nbsp;&nbsp;&nbsp;&nbsp;码(P)：</td>
												<td class="lgn_fim_r"><input type="password" id="password" name="password" class="com_textbox" style="width:195px; "></td>
											</tr>
											
 
											

										  <div class="messages"><p class="error"><font color="red">login from sso fail</font></p></div>
										  

											<tr>
												<td colspan="2">
												<table cellSpacing="0" cellPadding="0" width="*" class="lgn_btn_mg">
													<tr>
														<td class="lgn_btn">
															<img src="/sso/views/default/images/lgn_bi_1d.gif" style="cursor:hand" onclick="doSubmit();">&nbsp;
															 <img src="/sso/views/default/images/lgn_bi_2d.gif" style="cursor:hand" onclick="window.close();"></a>
														</td>
													</tr>
												</table>
												</td>
											</tr>
										</table>
				</div>
				</div>
				</td>
			</tr>
		</table> 
		
		
      <!--<div class="group">
        <fieldset>
          <label for="username">登录账号:</label>
          <input id="username" name="username" tabindex="1" type="text" value="">
        </fieldset>
        <fieldset>
          <label for="password">登录密码:</label>
          <input id="password" name="password" tabindex="2" type="password">
        </fieldset>
      </div>
      <p class="buttons">
        <a class="mmbutton" id="sign_in_button_standard" onclick="doSubmit();">
          <span>登录</span>
        </a>
      </p>
-->
    </form>
    <!--</div>
 -->

  <!--<div class="dlg_footer">
    &nbsp;
  </div>
 -->

</body>
</html>
contact.js:406

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head id="Head1"><title>

	人员信息

</title><link href="themes/Default/style.css" rel="stylesheet" type="text/css" /><link href="themes/Custom/Custom.css" rel="stylesheet" type="text/css" />



    <style type="text/css">

        .myImg

        {

         height:13px;

         width:11px;    

        }

        a.labelButton:link, a.labelButton:visited

        {

            color: #1C568A;

            text-decoration: underline;

        }

        a.labelButton:hover

        {

            color: Gold;

            text-decoration: underline;

        }

        #gvData th, #gvData td

        {

            padding-left: 1px;

        }

        th input, .col1 input

        {

            width: 16px;

            text-align: left;

        }

        .col2

        {

            text-overflow: ellipsis;

            white-space: nowrap;

            overflow: hidden;

        }

        .col2 a.user

        {

            width: 50px;

        }

        .col3 span

        {

            text-overflow: ellipsis;

            white-space: nowrap;

            overflow: hidden;

        }

        .col4 span

        {

            width: 68px;

            text-overflow: ellipsis;

            white-space: nowrap;

            overflow: hidden;

        }

    </style> 



    <script src="scripts/jquery-1.3.2.min.js" type="text/javascript"></script>

    <script src="scripts/script.js" type="text/javascript"></script>

    <script src="scripts/waitBox.js" type="text/javascript"></script>



    <script type="text/javascript">



        var isUUMTreeShowing = true;

        window.onresize = resizeTable;

        $(document).ready(function()

        {



            // 隐藏个人名片

            $("#userInfoSpecific").hide();

            // 动态更改iframe的高度

            var goodHeight = $("body").height();

            //window.alert(goodHeight);

            //window.alert($("body").width());

            $("#uumTree").height(goodHeight - 25);

            $("#userInfoSpecific").height(goodHeight);



            // 查询按钮单击事件

            $("#ibSearch").click(function()

            {

                // 这里的查询是查全局的, 因些, 不要"清空"已选择的部门

                if ($.trim($("#txtName").attr("value")) != "")

                {

                    setCurrentSelectedOUGUID("");

                    refreshInfo(null, 0, null, true);

                }

                else

                {

                    window.alert("- 请输入查询条件");



                    // 将查询文本框设为焦点

                    setSearchTextBoxFocus();

                }

                return false;

            });



            // 发送短信按钮单击事件

            $("#sendSMS").click(function()

            {

                var recvString = "";



                $("input[type=checkbox][checked=true]").each(function() { recvString += (this.value + "@"); });



                // 打开企信通页面

                window.open('http://iap.gmcc.net/meip/sso.jsp?receives=' + recvString, "contacts_sendSMS");

                return false;

            });



            // 部门按钮单击事件

            $("#aDepartment").click(function()

            {

                if (isUUMTreeShowing)

                {

                    $("#uumTree").slideUp("slow");

                }

                else

                {

                    $("#uumTree").slideDown("slow");

                }

                isUUMTreeShowing = !isUUMTreeShowing;

                return false;

            });



            // 个人按钮单击事件

            $("#aPerson").click(function () {

                var appCode = '';

                var nid = '61ca46b7-0b76-41ae-9e1a-cd9adba8c86c';

                if (appCode == "") {

                    window.open('MaintainAddressList.aspx?nid='+nid);

                } else {

                    window.open('MaintainAddressList.aspx?appcode='+appCode);

                }

                return false;

            });



            // 高级按钮单击事件

            $("#aAdvance").click(function()

            {

                window.open('http://es.gmcc.net/results.aspx?other=users&k=' + encodeURIComponent($("#txtName").attr("value")));

                return false;

            });

        });



        function hideUUMTreeWhenEsc()

        {

            //ESC

            if (window.event.keyCode == "27")

            {

                hideUUMTree();

            }

        }



        function hideUUMTree()

        {

            if (isUUMTreeShowing)

            {

                $("#uumTree").slideUp("slow");

                isUUMTreeShowing = false;

            }

        }



        function showUUMTree()

        {

            if (!isUUMTreeShowing)

            {

                $("#uumTree").slideDown("slow");

                isUUMTreeShowing = true;

            }

        }



        function showUserInfoPage(employee)

        {

            $("#userInfoSpecific").attr("src", "UserInfoSimple_userinfo.aspx?employee=" + employee);

            $("#userInfoSpecific").fadeIn("slow");

        }



        function hideUserInfoPage()

        {

            $("#userInfoSpecific").attr("src", "");

            $("#userInfoSpecific").fadeOut("slow");



            // 将查询文本框设为焦点

            setSearchTextBoxFocus();

        }



        // 将查询文本框设为焦点

        function setSearchTextBoxFocus()

        {

            $("#txtName").focus();

        }

        //全选

        function allCheckClick(chk)

        {

            if (chk.checked)

            {

                $("input[type=checkbox]").each(

                    function()

                    {

                        this.checked = true;

                    }

                );

            }

            else

            {

                $("input[type=checkbox]").each(

                    function()

                    {

                        this.checked = false;

                    }

                );

            }



        }

        //根据页面的宽度（iframe宽度）自动调节人员信息table的宽度，以便部门栏能够灵活适应宽度

        function resizeTable()

        {

            if ($("#gvData").length == 0)

            {

                return;

            }



            //160为col1,col2,col4的之和，7为每个单元格及其他边距之和，如果不加上7的话，table会看不到又边框。

            var tdOrgW = document.body.clientWidth - 160 - 7;

            if (tdOrgW <= 0)

            {

                return;

            }



            $("#gvData tr").children(".col3").each(

                function(i)

                {

                    this.children[0].style.width = tdOrgW;

                }

            );

        }

       

           

    </script>



    <script type="text/javascript">

        function getInfoFromServer(arg, context) {

            showWaitBox();

            WebForm_DoCallback('__Page',arg,refreshInfoHtml,context,null,false);

        }

        

        function refreshInfoHtml(infoHtml, context) {

            $("#mainInfo").html(infoHtml);

            resizeTable();

            hideWaitBox();       

        }

        

        function setCurrentSelectedOUGUID(newSelectedOUGUID) {

            $("#currentSelectedOUGUID").attr("value", newSelectedOUGUID);

        }

        

        function getParamString(searchCondition, pageIndex, selectedOUGUID) {

            return searchCondition + "#" + pageIndex + "#" + selectedOUGUID;

        }



        function refreshInfo(searchCondition, pageIndex, selectedOUGUID, isHideuumTree) {            

            if (pageIndex >= 0) {

                if (searchCondition == null)

                {

                    searchCondition = $("#txtName").attr("value");

                }

                if (selectedOUGUID == null)

                {

                    selectedOUGUID = $("#currentSelectedOUGUID").attr("value");

                }



                getInfoFromServer(getParamString(searchCondition, pageIndex, selectedOUGUID), "");

                // 默认获取数据后，隐藏组织架构树

                if (isHideuumTree == null || isHideuumTree) {

                    // 隐藏组织架构树

                    hideUUMTree();

                }



                //操作审计

                try {

                    var f = null;

                    var obj = document.getElementById("aDepartment");

                    var eventt= "onclick";

                    if (obj[eventt]) {

                        f = obj[eventt];

                        obj[eventt] = null;

                    }

                    gcpTracker.Load(500, function(trackedArg) {

                        trackedArg.actionID = 'a60c245a-a34f-4cb4-8695-022b223abc0c';

                    }, f);

                } catch(ex) {



                }

            }

        }

    </script>

</head>

<body onkeydown="hideUUMTreeWhenEsc();">

    <form name="form1" method="post" action="UserInfoSimple.aspx?nid=61ca46b7-0b76-41ae-9e1a-cd9adba8c86c&amp;sid=11&amp;f=app" onkeypress="javascript:return WebForm_FireDefaultButton(event, 'ibSearch')" id="form1">

<div>

<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />

<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />

<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTExMTE4NjQ2NzcPFgIeEVJpZ2h0Q29udGFjdHNOb2RlMrYBAAEAAAD/////AQAAAAAAAAAMAgAAAEZHQ1AuRGF0YS5Db21tb24sIFZlcnNpb249MS4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBQEAAAAmR0NQLkRhdGEuQ29tbW9uLkNvcmUuUmlnaHRDb250YWN0c05vZGUDAAAAB19tYW5hZ2ULX2dyb3VwVmlzaXQGX3Zpc2l0AAAAAQEBAgAAAAABAQtkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQhpYlNlYXJjaP13wAgoQ8PxOIwxG7hR7aPTALig" />

</div>



<script type="text/javascript">

//<![CDATA[

var theForm = document.forms['form1'];

if (!theForm) {

    theForm = document.form1;

}

function __doPostBack(eventTarget, eventArgument) {

    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {

        theForm.__EVENTTARGET.value = eventTarget;

        theForm.__EVENTARGUMENT.value = eventArgument;

        theForm.submit();

    }

}

//]]>

</script>





<script src="/WebResource.axd?d=---KtIt44X_Vw-yGaqCWtzLo1cG3E9iDgTY_xMLHvwxdi9FZAa3WM0m4yG41&amp;t=634259354644828874" type="text/javascript"></script>





<script src="http://pac-lib.gmcc.net/share/crossdomain/crossdomain-core.js" type="text/javascript"></script>

<script src="/WebResource.axd?d=STnGbmPc6u-FYzsQmFRIJALCrKYNsF2QKhI5v3KltdscLpqCr8xU2eyfat81&amp;t=634259354644828874" type="text/javascript"></script>

<div>



	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWAwLMrLGHCgLEhISFCwLytKiXDBvNvvikkUDhcvNY7VWyxeI3WvrS" />

</div>

    <div class="search">

        <table id="searchBar" cellpadding="0" cellspacing="0" style="width: 99%">

	<tr>

		<td>

                    <table cellpadding="0" cellspacing="0" style="width: 100%">

                        <tr>

                            <td style="padding-left: 1px; width: 90px;">

                                <input name="txtName" type="text" maxlength="20" id="txtName" class="TextBox" style="width:100%;" />

                            </td>

                            <td style="width: 25px; padding-right: 2px;">

                                <input type="image" name="ibSearch" id="ibSearch" title="查询" src="Images/ico_search.gif" align="right" style="border-width:0px;" />

                            </td>

                            <td style="width: 15px; padding-left: 2px;">

                             <a href="#" class="labelButton" id="aPerson" title="我的通讯录">

                                    <img border="0" src="Images/user2.gif"  alt="我的通讯录" /></a>

                            </td>

                            <td style="width: 15px; padding-left: 2px;">

                                <a href="#" title="发送短信" id="sendSMS">

                                    <img border="0" src="Images/icon_mobile.gif" alt="发送短信" /></a>

                            </td>

                            <td>

                                <a href="#" class="labelButton" id="aDepartment" title="显示/隐藏组织架构树">

                                    <img border="0" src="Images/dept.gif"  title="显示/隐藏组织架构树"/></a>

                                <a href="#" class="labelButton" id="aAdvance" title="查看详细企业通讯录">

                                    <span id="lbAdvance">

                                    <img class="myImg" border="0" src="Images/title_list_bg.gif" alt="查看详细企业通讯录"/>

                                    </span></a>

                            </td>

                        </tr>

                    </table>

                </td>

	</tr>

</table>



    </div>

    <div class="mainarea" id="mainInfo">

        <table class="dg_borderstyle" cellspacing="1" cellpadding="0" rules="all" border="1"

            id="gvData" style="background-color: White; border-color: #A8CFEB; border-width: 1px;

            border-style: Solid;">

            <tr>

                <td colspan="3">

                    <center>

                        <br />

                        <br />

                        <br />

                        加载数据…

                        <br />

                        <br />

                        <br />

                    </center>

                </td>

            </tr>

        </table>

    </div>

    

    <iframe id="uumTree" name="uumTree" style="width: 100%; position: absolute; left: 0px;

        top: 25px; z-index: 20;" frameborder="0" scrolling="auto" src="UserInfoSimple_left.aspx?nid=61ca46b7-0b76-41ae-9e1a-cd9adba8c86c&sid=11&f=app">

    </iframe>

    

    <iframe id="userInfoSpecific" name="userInfoSpecific" style="width: 100%; position: absolute;

        left: 0px; top: 0px; z-index: 30;" frameborder="0" scrolling="auto" src=""></iframe>

    <input type="hidden" id="currentSelectedOUGUID" value="" />

    



<script type="text/javascript">

//<![CDATA[



WebForm_InitCallback();WebForm_AutoFocus('txtName');//]]>

</script>

</form>

    <script type='text/javascript'>

        try {

            var gcpTracker = new Object();

            gcpTracker.tracked = {

                nodeID: '53f4fc1b-599a-48bb-ae41-3d67f08ebf39',

                userID: 'chengyaoan',

                moduleID: '8d7c947c-d1c1-4f8d-8a59-4099fdbe88aa',

                actionID: '',

                subNodeID: '',

                browser: window.navigator.userAgent

            };

            gcpTracker.Load = function (delay, preSend, postSend) {

                var onLoad = function (cxt) {

                    if (preSend && typeof (preSend) == 'function') {

                        preSend.call(cxt, this.tracked);

                    }



                    this.postSends = postSend;



                    var tUrl = 'http://traffic.services.gmcc.net/gcpTracker.js?timestamp' + new Date().valueOf();

                    var ts = document.createElement('script');

                    ts.setAttribute('src', tUrl);

                    document.getElementsByTagName('head')[0].appendChild(ts);

                };

                var g = this;

                return function() {

                    return setTimeout(function() {

                        onLoad.call(g, this);

                    }, delay);

                };

            };

            gcpTracker.postSends = new Object();

            gcpTracker.onPostSend = function () {

                if (this.postSends)

                    setTimeout(this.postSends, 100);

            };

            gcpTracker.Event = function(obj, eventt, delay, onPreSend) {

                var f = null;

                if (obj[eventt]) {

                    f = obj[eventt];

                    obj[eventt] = null;

                }

                obj.attachEvent(eventt, gcpTracker.Load(delay, onPreSend, f));

            };



            // obj: event source on which you want to attach method;

            // event: name of event you are going to listen, base on a browser or element;

            // delay: the gap between event occurs and method executes, 

            // onPreSend: the custom defined PreSend event handler, which's argment is only gcpTracker.tracked.        

            // eg. delay 500 milliseconds after page 'onload' base on IE6: 

            //      gcpTracker.Event(window,'onload',500)

            // eg. delay 0 milliseconds after button(it's id: btnOK) 'onclick' base on IE6: 

            //      gcpTracker.Event(document.getElementById('btnOK'),'onclick',0) // make sure button btnOK has loaded before this line being invoked.



            //注册页面进入

            gcpTracker.Event(window, 'onload', 500);

            //注册搜索事件

            gcpTracker.Event(

                document.getElementById("ibSearch"), 'click', 500,

                function (trackedArg) {

                    trackedArg.actionID = '0d60e36b-2810-4d11-b67a-dc584704f114';

                }

           );

           //注册按部门

           gcpTracker.Event(

                document.getElementById("aDepartment"), 'click', 500,

                function (trackedArg) {

                    trackedArg.actionID = 'a60c245a-a34f-4cb4-8695-022b223abc0c';

                }

           );

        }

        catch (e) {

        }

</script>

</body>

</html>


-------------------------
请求的返回,猜测数字为数据条数

56|/wEWAwLMrLGHCgLEhISFCwLytKiXDBvNvvikkUDhcvNY7VWyxeI3WvrS
<table class="dg_borderstyle" cellspacing="1" cellpadding="0" rules="all" border="1" id="gvData" style="background-color:White;border-color:#A8CFEB;border-width:1px;border-style:Solid;">

    <tr>
        <th scope="col">
          <input type='checkbox' onclick='allCheckClick(this)' />
        </th>
        <th scope="col">
            名称
        </th>
        <th scope="col">
            部门
        </th>
        <th scope="col">
            手机号码
        </th>
    </tr>

    <tr class="dg_itemstyle">
        <td class="col1"><input type="checkbox" value="zhangyuling" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=zhangyuling&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=zhangyuling" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0221020110');return false;"
                href="#" title="张玉玲">张玉玲</a>
        </td>
        <td class="col3"><span title="广州分公司-西区分公司">广州-西区分公司</span>
        </td>
        <td class="col4">
            <span title="13922200628">13922200628</span>
        </td>
    </tr>

    <tr class="dg_alternatingitemstyle">
        <td class="col1"><input type="checkbox" value="chenyuliang" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=chenyuliang&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=chenyuliang" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0221023046');return false;"
                href="#" title="陈煜亮">陈煜亮</a>
        </td>
        <td class="col3"><span title="广州分公司-白云分公司">广州-白云分公司</span>
        </td>
        <td class="col4">
            <span title="13922303612">13922303612</span>
        </td>
    </tr>

    <tr class="dg_itemstyle">
        <td class="col1"><input type="checkbox" value="chenyuling2" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=chenyuling2&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=chenyuling2" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0221021947');return false;"
                href="#" title="陈玉玲">陈玉玲</a>
        </td>
        <td class="col3"><span title="广州分公司-番禺分公司-番禺分公司综合部">广州-番禺分公司综合部</span>
        </td>
        <td class="col4">
            <span title=""></span>
        </td>
    </tr>

    <tr class="dg_alternatingitemstyle">
        <td class="col1"><input type="checkbox" value="chenyulin" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=chenyulin&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=chenyulin" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0221350253');return false;"
                href="#" title="陈玉麟">陈玉麟</a>
        </td>
        <td class="col3"><span title="广州分公司-番禺分公司-中区服务销售中心">广州-中区服务销售中心</span>
        </td>
        <td class="col4">
            <span title="13922330333">13922330333</span>
        </td>
    </tr>

    <tr class="dg_itemstyle">
        <td class="col1"><input type="checkbox" value="wengyulin" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=wengyulin&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=wengyulin" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0521480312');return false;"
                href="#" title="翁裕霖">翁裕霖</a>
        </td>
        <td class="col3"><span title="汕头分公司-澄海分公司-澄城区域">汕头-澄城区域</span>
        </td>
        <td class="col4">
            <span title="13825866565">13825866565</span>
        </td>
    </tr>

    <tr class="dg_alternatingitemstyle">
        <td class="col1"><input type="checkbox" value="queyuling" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=queyuling&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=queyuling" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0421040106');return false;"
                href="#" title="阙誉翎">阙誉翎</a>
        </td>
        <td class="col3"><span title="珠海分公司-数据业务中心">珠海-数据业务中心</span>
        </td>
        <td class="col4">
            <span title="13702323239">13702323239</span>
        </td>
    </tr>

    <tr class="dg_itemstyle">
        <td class="col1"><input type="checkbox" value="qiuyuli" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=qiuyuli&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=qiuyuli" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0921660550');return false;"
                href="#" title="邱玉丽">邱玉丽</a>
        </td>
        <td class="col3"><span title="惠州分公司-惠阳分公司-惠阳分公司市场部">惠州-惠阳分公司市场部</span>
        </td>
        <td class="col4">
            <span title="13923636490">13923636490</span>
        </td>
    </tr>

    <tr class="dg_alternatingitemstyle">
        <td class="col1"><input type="checkbox" value="laiyulin" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=laiyulin&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=laiyulin" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0921661368');return false;"
                href="#" title="赖昱霖">赖昱霖</a>
        </td>
        <td class="col3"><span title="惠州分公司-博罗分公司-博罗分公司市场部">惠州-博罗分公司市场部</span>
        </td>
        <td class="col4">
            <span title="15807525191">15807525191</span>
        </td>
    </tr>

    <tr class="dg_itemstyle">
        <td class="col1"><input type="checkbox" value="mayulin" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=mayulin&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=mayulin" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('1221140017');return false;"
                href="#" title="马玉林">马玉林</a>
        </td>
        <td class="col3"><span title="中山分公司-南部分公司">中山-南部分公司</span>
        </td>
        <td class="col4">
            <span title="18826011008">18826011008</span>
        </td>
    </tr>

    <tr class="dg_alternatingitemstyle">
        <td class="col1"><input type="checkbox" value="liuyulian2" /></td>
        <td class="col2">
            <a target="_blank" href="http://ims.gmcc.net/api/msgrd.ashx?uid=liuyulian2&action=chat"><img name="imsStatus" onload="getOnlineStatus(this)" style="border: none; vertical-align: text-bottom;" imsImgUrl="http://ims.gmcc.net/api/UserStatusImage.ashx?uid=liuyulian2" src="http://contacts.services.gmcc.net/Images/nodisturb.ico" alt="发起IMS会话" /></a> <a class="user" onclick="showUserInfoPage('0821800094');return false;"
                href="#" title="刘育连">刘育连</a>
        </td>
        <td class="col3"><span title="梅州分公司-城区分公司-市场部">梅州-市场部</span>
        </td>
        <td class="col4">
            <span title="13823857296">13823857296</span>
        </td>
    </tr>

</table>

<div style="margin-top: 5px;">
    <span style="margin-left: 1px; float: left; color: #1C568A; font-size: 8pt;">第<span style="color: Blue;">1</span>页|共<span style="color: Blue;">11</span>页/<span style="color: Blue;">103</span>条</span>
    <span style="margin-right: 1px; float: right;">
        <a id="pager_first" href="#" onclick="refreshInfo(null, -1, null, true);return false;"><img title="首页" src="Images/dg_btn_first.gif" align="absbottom" style="border-width:0px;" /></a><a id="pager_prev" href="#" onclick="refreshInfo(null, -1, null, true);return false;"><img title="上一页" src="Images/dg_btn_prev.gif" align="absbottom" style="border-width:0px;" /></a><a id="pager_next" href="#" onclick="refreshInfo(null, 1, null, true);return false;"><img title="下一页" src="Images/dg_btn_next.gif" align="absbottom" style="border-width:0px;" /></a><a id="pager_last" href="#" onclick="refreshInfo(null, 10, null, true);return false;"><img title="尾页" src="Images/dg_btn_last.gif" align="absbottom" style="border-width:0px;" /></a>
    </span>
</div>
