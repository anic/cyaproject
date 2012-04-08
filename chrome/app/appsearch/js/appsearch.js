//http://portal-app3.gmcc.net/ApplicationWebModule2/appaccess/appaccess-publish.html?hideServiceTab=true
var apps = document.getElementsByClassName("x-tree-node-anchor");
for(var i = 0, size = apps.length; i < size; ++i) {
	var app = apps[i];
	var url = app.href;
	var name = app.children[0].innerHTML;
	console.log(name + "\t" + url);
}

