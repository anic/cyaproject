//需要jquery-impromptu.4.0.min.js
//修复更多无法显示菜单的问题
//从Head.aspx中复制过来的

var oPopup = window.parent.document.createElement("iframe");
oPopup.width = "156px";
oPopup.height = "600px";
oPopup.id = "oPop";
oPopup.style.position = "absolute";
oPopup.scrolling = "no";
oPopup.frameborder = "0";
oPopup.style.zIndex = 1000;
oPopup.style.display = "none";
oPopup.style.borderStyle = "none";
//竟然没有body，所以只能在html后添加iframe
window.parent.document.getElementsByTagName("html")[0].appendChild(oPopup);

window.showMenu = function(theId, reference) {
	var menu = document.getElementById(theId);
	// alert(menu.innerHTML);

	var t = reference.offsetTop + 58;
	var l = reference.offsetLeft - 60;
	while( reference = reference.offsetParent) {
		t += reference.offsetTop;
		l += reference.offsetLeft;
	}
	// Popup对象和Window对象一样，里面包含了一个完整的HTML文档，在Body中插入HTML
	//oPopup.document.body.innerHTML = menu.innerHTML;
	oPopup.style.left = l + "px";
	oPopup.style.top = t + "px";

	// 设置显示的位置、大小、参照物
	// left, top, width, height: 38 + 25*(n-1)
	//oPopup.show(l, t, 156, 500, document.body);
	oPopup.contentDocument.documentElement.getElementsByTagName("body")[0].innerHTML = menu.innerHTML;

	//toggle menu
	if(oPopup.style.display == "none")
		oPopup.style.display = "block";
	else
		oPopup.style.display = "none";
}

document.getElementById("getmore").onclick = function() {
	showMenu("divMoreMenu", document.getElementById("getmore"));
};
