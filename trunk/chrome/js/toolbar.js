$(function() {

	$('.dropdown-toggle').dropdown();
	if(chrome) {
		var url = chrome.extension.getURL("popup.html");
		$.get(url, function(page) {
			window.p = page;

			var mat = page.match(/<ul [\w\W.\n]+?>([\w\W.\n]+)<\/ul>/);
			if(mat)
			{
				var adjust = mat[1];
				adjust = adjust.replace(/target="_blank"/g,"");
				adjust = adjust.replace(/onclick="[\w\W\n.]*?"/g,"");
				$("#ulTool").html(adjust);
			}
			else
				$("#ulTool").html("<li>加载失败</li>");
		});
	}

});
