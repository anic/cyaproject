$(function() {
	var bg = chrome.extension.getBackgroundPage();
	$("#version").append(bg.gExInfo.version);
});
