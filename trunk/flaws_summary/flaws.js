console.log("start");

// Count all of the links from the nodejs build page
var jsdom = require("jsdom");

jsdom.env("E:/work/mytask/120521 漏洞扫描/0615/appscan内网九大系统扫描报告/appscan_需求协作_20120615.html", [], function(errors, window) {
	var document = window.document;

	//提取漏洞信息
	var title = document.getElementsByClassName("f34_");
	var degree = document.getElementsByClassName("f45_");
	var url = document.getElementsByClassName("f42_");
	var task = document.getElementsByClassName("f69_");
	var id = document.getElementsByClassName("f35_");

	var detail = document.getElementsByClassName("f37_");
	var d, itemid;
	var str = "序号\tID\t标题\t严重性\tURL\t修复任务";
	console.log(str);
	for(var i = 0, size = title.length; i < size; ++i) {
		itemid = id[i].innerHTML.match(/ID=(\d+)/)[1];
		str = i + "\t" + itemid + "\t" + title[i].innerHTML + "\t" + degree[i].innerHTML + "\t" + url[i].innerHTML + "\t" + task[i].innerHTML;
		str = str.replace(/&nbsp;/g, "");

		console.log(str);
	}

});
