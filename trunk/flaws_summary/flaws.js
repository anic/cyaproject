console.log("start");

// var sqlite = require("sqlite");
// var db = sqlite.openDatabaseSync("flaws.sqlite");
//
// return;

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('flaws.sqlite');

// function saveReport0(path, filename, content) {
// // console.log("SAVE REPORT:" + path);
// db.serialize(function() {
// var stmt = db.prepare("INSERT INTO cover_report(filename,path) VALUES (?,?);");
// stmt.run([filename, path]);
// stmt.finalize();
//
// console.log("COVER REPORT:" + path);
// db.each("SELECT id FROM cover_report where path = ?", [path], function(err, row) {
// var id = row.id;
// console.log("GET ID:" + id);
// var stmt2 = db.prepare("INSERT INTO raw_data(flawno,flawid,title,degree,url,fix,param,filename,reportid) VALUES (?,?,?,?,?,?,?,?,?)");
// for(var i = 0, len = content.length; i < len; ++i) {
// content[i].push(filename);
// content[i].push(id);
// stmt2.run(content[i]);
// }
// stmt2.finalize();
// });
// });
// }

function saveReport(path, filename, content) {

	var BufferedWriter = require("buffered-writer");

	var fs = require('fs');
	var row;
	console.log("SAVE:" + path + " " + content.length);
	for(var i = 0, len = content.length; i < len; ++i) {
		row = content[i];
		row.push(path);
		//console.log(row.join("\t"));
		// fs.appendFile('raw_data.txt', row.join("\t") + "\r\n", "utf-8", function(err) {
		// if(err)
		// throw err;
		// });
		new BufferedWriter(sub + ".txt", {
			encoding : "utf8",
			append : true
		}).on("error", function(error) {
			console.log(error);
		}).write(row.join("\t") + "\r\n")//Writes 0x00, 0x01, 0x02
		.close();
	}
}

// function checkReport(path, file, callback) {
// db.all("SELECT id FROM cover_report where path = ?", path, function(err, rows) {
// console.log(rows.length);
// if(rows.length == 0) {
// callback(path, file);
// }
// });
// }

function listTarget(root) {
	var fileUtils = require("file-utils");
	var File = fileUtils.File;

	var names = [], paths = [];
	new File(root).list(function(name, path) {

		//console.log(name);
		if(name.match(/\.html/)) {
			names.push(name);
			paths.push(path);

			extractContent(path, name);
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
			console.error("ERROR:" + path + "\r\n" + err);
		}

		//保存到数据库
		saveReport(path, filename, content);
	});
}

// function init() {
// var fs = require('fs');
// var file = fs.readFileSync("cover_report.txt", "utf8");
// console.log(file);
// var row_reports = file.split("\n");
// var content, id;
// for(var i = 0, len = row_reports.length; i < len; ++i) {
// content = row_reports[i].split("\t");
// id = parseInt(content[0]);
//
// _dic[content[1]] = {
// id : id,
// path : content[1],
// filename : content[2]
// };
//
// if(id > _maxId) {
// _maxId = id;
// }
// }
//
// listTarget(_root);
// }

// var _dic = {};
// var _maxId = 0;
var sub = process.argv.length > 2 ? process.argv[2] : "";
var root = "E:/work/mytask/120521 漏洞扫描/flaws_target/" + sub;
var path = "E:\\work\\mytask\\120521 漏洞扫描\\flaws_target\\0521\\内网系统\\AppScan_需求协作_20120522.html";
var file = "AppScan_需求协作_20120522.html";
//console.log(root);
//extractContent(path, file);
listTarget(root);
//init();