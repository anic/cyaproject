(function init() {
	var date = new Date();
	var strdate = date.getFullYear() + "-" + (1 + date.getMonth()) + "-" + date.getDate() + " 08:00";
	//设置当前时间的天
	$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_tbDate").val(strdate);
	//设置进入原因
	$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_ddlOrigin").val(1);

	//设置进入楼层，因为异步加载，所以只能用延时改变这种方式
	window.setTimeout(function() {
		$("#tbFloorSelect_D")[0].innerHTML += '<option value="56">7层</option>';
		console.log("test");
	}, 2000);
	var _lastname = "";

	//快速查找用户
	function quickSearch() {
		//查询姓名
		var name = $("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_tbName").val();

		//POST http://isite.gz.gmcc.net/Controls/Visit/VisitUserQueryHandler.ashx
		//pageIndex:0
		// UserName:张波
		// Department:
		// Mobile:
		// Hylink:javascript:getVisitorSearch({0})
		// BindVisitor:true
		var reg = /[^\u4e00-\u9fa5]/;
		if(reg.test(name)) {
			//非中文
			return;
		}

		//中文时，判断是否已经出现过
		if(name !== '' && name != _lastname) {
			_lastname = name;
			console.log(name);
			$.post('http://isite.gz.gmcc.net/Controls/Visit/VisitUserQueryHandler.ashx', {
				'pageIndex' : 0,
				'UserName' : name,
				'Department' : '',
				'Mobile' : '',
				'Hylink' : 'javascript:getVisitorSearch({0})',
				'BindVisitor' : true
			}, function(result) {
				console.log(result);
				var arr = result.match(/<a .*?<\/a>/);
				if(arr.length > 0) {
					//找到匹配
					var company = arr[0].match(/Company="(.*?)"/)[1]; //匹配公司名称
					var phone = arr[0].match(/Phone="(.*?)"/)[1]; 
					var idcard = arr[0].match(/IDCardNo='(.*?)'/)[1];
					var userid = arr[0].match(/UserID='(.*?)'/)[1];
					
					//填写用户ID、公司、手机和身份证号
					$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_hfID1").val(userid);
					$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_tbCompany").val(company);
					$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_tbPhone").val(phone);
					$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_tbPersonCard").val(idcard);
				}

			});
		}

	}


	$("#ctl00_ctl00_ctl00_MainContentPlaceHolder_BodyPlaceHolder_FormContentPlaceHolder_tbName").bind('keyup', quickSearch);

})();
