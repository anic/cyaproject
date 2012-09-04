window.AccessDb = {
	dbpath : "",
	plugin : null,
	init : function(pluginId) {
		this.dbpath = window.localStorage["DbPath"];
		if(!this.dbpath) {
			this.dbpath = "E:/work/mytask/xqp/xqp.accdb";
		}
		this.plugin = document.getElementById("dbplugin");
	},
	saveDBPath : function(path) {
		window.localStorage["DbPath"] = path;
		alert("请刷新页面以生效");
	},
	exec : function(sql) {
		console.log("this.plugin.msaccess_exec('" + this.dbpath + "','" + sql + "')");
		window._result = this.plugin.msaccess_exec(this.dbpath, sql);
		//console.log(sql);
		return window.eval("(" + _result + ")");
	}
};
