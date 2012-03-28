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

	
}());
