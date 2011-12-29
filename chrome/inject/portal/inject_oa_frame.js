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

			if(tr.children.length > 0 && tr.children[0].style.height == "3px") {
				tr.parentElement.removeChild(tr);
				continue;
			}
		}
	}, 2000);

	window.setTimeout(function() {
		var menu = document.getElementById("lmt_Menu");
		if(menu) {
			//重新定义onmouseover的函数
			function onover(e) {
				e.target.src = e.target.getAttribute("xsrc");
				//使用了getAttribute修正之前的bug
			}

			//重新定义onmouseout的函数
			function onout(e) {
				e.target.src = e.target.getAttribute("dsrc");
			}

			function onclick(e) {
				//点击使用事件绑定而非覆盖，在触发了原有操作后，可以将按钮重置状态，修复原来的图片缺失问题
				var is = menu.getElementsByTagName("img");
				for(var i in is) {
					onout({
						target : is[i]
					});
				}
			}

			var imgs = menu.getElementsByTagName("img");
			for(var i in imgs) {
				imgs[i].onmouseover = onover;
				imgs[i].onmouseout = onout;
				imgs[i].addEventListener("click", onclick);
			}
		}
	}, 3000);
}());
