/**
 * 加载外部文件或者脚本

 如果filetype为空，则创建脚本内容
 如果为js或css，则引入外部文件
 */
window.loadjscssfile = loadjscssfile = function(filename, filetype) {
	if( typeof filetype == "undefined") {
		var fileref = document.createElement('script');
		fileref.setAttribute("type", "text/javascript");
		fileref.innerHTML = filename;
	} else if(filetype == "js") {//if filename is a external JavaScript file
		var fileref = document.createElement('script');
		fileref.setAttribute("type", "text/javascript");
		fileref.setAttribute("src", filename);
	} else if(filetype == "css") {//if filename is an external CSS file
		var fileref = document.createElement("link");
		fileref.setAttribute("rel", "stylesheet");
		fileref.setAttribute("type", "text/css");
		fileref.setAttribute("href", filename);
	}
	if( typeof fileref != "undefined")
		document.getElementsByTagName("head")[0].appendChild(fileref)
};
