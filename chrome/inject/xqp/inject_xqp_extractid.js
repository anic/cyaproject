function init() {

	var src = window.location.href;
	if(src.indexOf("DoneTaskByAppl.aspx") == -1) {
		return;
	}

	//初始化
	
	$("#btnSetHasten").after($('<input class="btnPassClass" type="button" value="抽取" id="btnExtract">').click(function() {
		var table = document.getElementById("tblId1");
		var tbody = table.children[0];
		
		
		for(var i = 1, size = tbody.children.length; i < size; ++i) {
			var content = tbody.children[i];
			
			var sty =  (content.children[0].style["display"] == "none")? "":"none";
			
			//remove 0,1,2
			content.children[0].style["display"] = sty;
			content.children[1].style["display"] = sty;
			content.children[2].style["display"] = sty;
			
			content.children[4].style["display"] = sty;
			content.children[5].style["display"] = sty;
			content.children[6].style["display"] = sty;
			content.children[7].style["display"] = sty;
			//content.removeChild(content.children[0]);
			//content.removeChild(content.children[0]);
			//content.removeChild(content.children[0]);
			
			//remove 3,4,5,6
			// content.removeChild(content.children[1]);
			// content.removeChild(content.children[1]);
			// content.removeChild(content.children[1]);
			// content.removeChild(content.children[1]);
		}

		return false;
	}));
}

init();
