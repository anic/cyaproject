/**
 优化：
 1 搜索。如果搜索工单号，直接重定向到目标；在工单号中回车也可以直接搜索
 2 禁用了收缩的按钮，使得可以使用回车进行搜索
 */

var aSearch;
function init() {

	var src = window.location.href;
	if(src.indexOf("Search.aspx") == -1) {
		return;
	}

	//这是frame 4
	//window.frames[4].document.getElementById("ctl00_cphBody_txtWorkId")
	var txtAVId = document.getElementById("ctl00_cphBody_txtWorkId");
	//1 增加判断，如果输入内容为标准工单号的形式，将开始日期调整至工单发起日期

	//不用addEventListener,防止回车直接提交数据（目前未能生效）
	txtAVId.onkeyup = txtAVId.onblur = function(e) {
		// if(e.keyCode == 13)//ENTER,
		// {
		// aSearch.onclick();
		// e.stopPropagation();
		// e.preventDefault();
		// return false;
		// } else//非回车
		var avid = txtAVId.value;
		console.log(avid);
		if(/[A-z]{2}\d{9}/.test(avid))//满足工单的格式
		{
			var y = avid.substr(2, 2);
			var m = avid.substr(4, 2);
			var d = avid.substr(6, 2);
			var date = "20" + y + "-" + m + "-" + d;
			document.getElementById("ctl00_cphBody_dtpStart1_txtDate").value = date;
		}
		// }
	};
	aSearch = document.createElement("a");
	aSearch.innerHTML = "详细";
	aSearch.href = "#";
	aSearch.onclick = function() {
		var avId = txtAVId.value;
		if(!avId) {
			window.err("Id empty!");
			return false;
		} else {
			searchList(txtAVId.value);
		}
		return false;
	};
	txtAVId.parentNode.appendChild(aSearch);

	var divTitle = document.getElementsByClassName("searchTitle")[0];
	var btn = divTitle.children[1];
	btn.disabled = true;

}

var xmlHttp;
function searchList(id) {
	var et = new Date();
	var st = addDate(5, -6, et);
	var strEt = et.getFullYear() + "-" + (et.getMonth() + 1) + "-" + et.getDate();
	var strSt = st.getFullYear() + "-" + (st.getMonth() + 1) + "-" + st.getDate();

	//标准的查询GET语句
	//http://xqp2.gz.gmcc.net/Workflow/Search.aspx?bt=2011-10-29&et=2011-11-30&wname=&aname=&c=&a=&tk=&ck=&i=AV
	var url = "Search.aspx?" + "bt=" + strSt + "&et=" + strEt + "&wname=&aname=&c=&a=&tk=&ck=&i=" + id;
	if(window.ActiveXObject) {
		xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	} else if(window.XMLHttpRequest) {
		xmlHttp = new XMLHttpRequest();
	}

	window.log("1/3 搜索...");
	xmlHttp.open("GET", url);
	xmlHttp.onreadystatechange = callback;
	xmlHttp.send(null);
}

function callback() {
	if(xmlHttp.readyState == 4) {
		if(xmlHttp.status == 200) {
			//do something interesting here
			var str = xmlHttp.responseText;
			/*
			 <tr style="text-align:center;">
			 <td><img alt="AV" class="groupImage" src="/images/groups/flow_av.gif" /></td>
			 <td style="text-align:left;">
			 <a href="WorkflowView.aspx?wiid=1ee8c0d9-157d-4ac9-ae32-5837c8972acb">金海无纸化试点项目BOSS接口开发需求书</a>
			 </td>
			 <td>AV111129002</td>
			 <td>陈爱琼</td>
			 <td>业务支持中心分发</td>
			 <td>余立</td>
			 <td>2011-11-29 11:39:47</td>
			 </tr>

			 * */
			window.log("2/3 分析...");

			var resultArr = str.match(/(WorkflowView.aspx\?wiid=.*)[\'|\"]/m);
			//alert(str.indexOf("WorkflowView.aspx"));
			//alert(resultArr);
			if(!!resultArr) {
				var url = resultArr[1];
				window.log("3/3 定位...");
				window.location.href = url;

			} else {
				window.log("Result empty!");
			}

		}
	}
}

function addDate(type, NumDay, vdate) {
	var date = new Date(vdate);
	type = parseInt(type)//类型
	var lIntval = parseInt(NumDay)//间隔
	switch(type) {
		case 6 :
			//年
			date.setYear(date.getYear() + lIntval)
			break;
		case 7 :
			//季度
			date.setMonth(date.getMonth() + (lIntval * 3))
			break;
		case 5 :
			//月
			date.setMonth(date.getMonth() + lIntval)
			break;
		case 4 :
			//天
			date.setDate(date.getDate() + lIntval)
			break
		case 3 :
			//时
			date.setHours(date.getHours() + lIntval)
			break
		case 2 :
			//分
			date.setMinutes(date.getMinutes() + lIntval)
			break
		case 1 :
			//秒
			date.setSeconds(date.getSeconds() + lIntval)
			break;
		default:

	}
	return date;
}

//call init
init();
