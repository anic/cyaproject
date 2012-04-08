/**
 * portal中首页有不少添加的空白位置，用于占位，在chrome中显示错位
 <tr style="height:8px;"><td></td></tr>

 */
( function init() {
	window.setTimeout(function() {
		var trs = document.getElementsByTagName("tr"), tr;
		for(var i in trs) {
			tr = trs[i];
			if(tr.style && (tr.style.height == "8px")) {
				tr.parentElement.removeChild(tr);
				continue;
			}

			if(tr.children && tr.children.length > 0 && tr.children[0].style.height == "3px") {
				tr.parentElement.removeChild(tr);
				continue;
			}
		}
	}, 2000);
	//修正侧栏工具栏
	window.setTimeout(function() {
		var sideTool = document.getElementById("lmt_DivFrames");

		if(sideTool) {
			var tools = sideTool.children;
			for(var i = 0, size = tools.length; i < size; ++i) {
				//<iframe id="lmt_M0_C" height="305px" width="268px" "="" style=" position:relative;display:none;" scrolling="no" frameborder="0"
				//srcurl="http://bizmap.gmcc.net/netportal/menu/Search.aspx" loadstatus="1" src=""></iframe>
				var child = tools[i];
				if(child.hasAttribute("srcurl")) {
					child.setAttribute("src", child.getAttribute("srcurl"));
					child.removeAttribute("srcurl");
				}
			}
		}
	}, 3000);
}());
