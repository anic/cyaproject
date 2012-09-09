console.log("start");

function saveReport(path, filename, content) {
	console.log("SAVE REPORT:" + path);

	var sqlite3 = require('sqlite3').verbose();
	var db = new sqlite3.Database('flaws.sqlite');

	db.serialize(function() {
		var stmt = db.prepare("INSERT INTO cover_report(filename,path) VALUES (?,?)");
		stmt.run([filename, path]);
		stmt.finalize();
	});

	// db.serialize(function() {
		// db.each("SELECT id FROM cover_report where path = ?", [path], function(err, row) {
			// var id = row.id;
			// var stmt2 = db.prepare("INSERT INTO raw_data(flawno,flawid,title,degree,url,fix,param,filename,reportid) VALUES (?,?,?,?,?,?,?,?,?)");
			// for(var i = 0, len = content.length; i < len; ++i) {
				// content[i].push(filename);
				// content[i].push(id);
				// stmt2.run(content[i]);
			// }
			// stmt2.finalize();
			// db.close();
		// });
	// });
}

function checkReport(path, file, callback) {
	var sqlite3 = require('sqlite3').verbose();
	var db = new sqlite3.Database('flaws.sqlite');
	
	db.all("SELECT id FROM cover_report where path = ?", [path], function(err, rows) {
		if(rows.length == 0)
			callback(path, file);

	});
	
	db.close();
}

function listTarget(root) {
	var fileUtils = require("file-utils");
	var File = fileUtils.File;

	var names = [], paths = [];
	new File(root).list(function(name, path) {

		//console.log(name);
		var index = name.indexOf(".html");
		if(index >= 0) {
			names.push(name);
			paths.push(path);

			//异步抽取
			checkReport(path, name, saveReport);
		}
		return true;
	}, 10, function() {
	});
}

function extractContent(path, filename) {
	console.log("EXTRACT:" + path);
	var jsdom = require("jsdom");
	var content = [];

	jsdom.env(path, [], function(errors, window) {
		var document = window.document;

		//提取漏洞信息
		var title = document.getElementsByClassName("f34_");
		var degree = document.getElementsByClassName("f45_");
		var url = document.getElementsByClassName("f42_");
		var task = document.getElementsByClassName("f69_");
		var id = document.getElementsByClassName("f35_");

		var detail = document.getElementsByClassName("f37_");
		var d, itemid, itemurl, itemparam, itemtitle, match, itemcontent;
		//var str = "序号\tID\t标题\t严重性\tURL\t修复任务";
		//console.log(str);

		try {
			for(var i = 0, size = title.length; i < size; ++i) {
				itemid = id[i].innerHTML.match(/ID=(\d+)/)[1];
				itemurl = url[i].innerHTML;
				itemtitle = title[i].innerHTML.replace(/\[.*\]/, "").replace(/&nbsp;/g, "").trim();
				match = itemurl.match(/\((.*)\)/);
				itemparam = match ? match[1] : "";
				itemurl = itemurl.replace(/\(.*\)/, "").replace(/&nbsp;/g, "").trim();
				itemcontent = [i, itemid, itemtitle, degree[i].innerHTML, itemurl, task[i].innerHTML, itemparam];
				content.push(itemcontent);

				// console.log(itemcontent);
			}
		} catch(err) {
			console.error("ERROR:" + path + "\n" + err);
		}

		//保存到数据库
		saveReport(path, filename, content);
	});
}

var root = "E:/work/mytask/120521 漏洞扫描/flaws_target";
// var path = "E:/work/mytask/120521 漏洞扫描/flaws_target/0521/内网系统/AppScan_需求协作_20120522.html";
// var file = "AppScan_需求协作_20120522.html";
// extractContent(path, file);
listTarget(root);
