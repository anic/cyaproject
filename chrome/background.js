//应用程序ID
(function() {

	//获取应用的ID
	var url = chrome.extension.getURL("");
	var match = url.match(/\/(\w+)\//);
	var appId = match ? match[1] : "";
	chrome.management.get(appId, function(info) {
		window.gExInfo = info;
	});

	$.getJSON(chrome.extension.getURL("manifest.json"), function(json) {
		window.gManifest = json;
	});
	var onTabChange = function(tab) {

		/*

		 Tab
		 ( object )
		 id ( integer )
		 The ID of the tab. Tab IDs are unique within a browser session.
		 index ( integer )
		 The zero-based index of the tab within its window.
		 windowId ( integer )
		 The ID of the window the tab is contained within.
		 selected ( boolean )
		 Whether the tab is selected.
		 pinned ( boolean )
		 Whether the tab is pinned.
		 url ( string )
		 The URL the tab is displaying.
		 title ( optional string )
		 The title of the tab. This may not be available if the tab is loading.
		 favIconUrl ( optional string )
		 The URL of the tab's favicon. This may not be available if the tab is loading.
		 status ( optional string )
		 Either loading or complete.
		 incognito ( boolean )
		 Whether the tab is in an incognito window.

		 * */
		var cs = gManifest.content_scripts;
		var url = tab.url;
		console.log(url);

		//减少google重定向被墙的概率
		if(url.match(/https?\:\/\/www\.google\.com\/url/)) {
			var mat = url.match(/url=([^&|$]*)/);
			if(mat) {
				var target = mat[1];
				target = decodeURIComponent(target);
				console.log("redirect to " + target);
				chrome.tabs.update(tab.id, {
					url : target
				});
			}
		}

		//这个url不像location.href（末尾有/），这个是直接显示的,为了形成匹配，添加“/”
		var pathMatch = url.match(/\//g);
		if(pathMatch && pathMatch.length == 2) {
			url = url + "/";
		}

		var reg, m;

		for(var i = 0, size = cs.length; i < size; ++i) {
			var item = cs[i];
			//获取content_scripts的match
			var matches = item.matches;
			if(!matches)
				continue;

			for(var j = 0, len = matches.length; j < len; ++j) {
				m = matches[j];
				if(m.indexOf("*") != -1)
					m = m.replace(/\*/g, '.*')
				reg = new RegExp(m);
				if(reg.test(url)) {

					//路径匹配，则使用彩色图标，标示运行中
					chrome.browserAction.setIcon({
						path : chrome.extension.getURL("image/home32.png")
					});
					return;
				}
			}
		}

		//路径不匹配，使用黑白图标，标示未运行
		chrome.browserAction.setIcon({
			path : chrome.extension.getURL("image/home.png")
		});
	};
	//监听tab的变化
	chrome.tabs.onSelectionChanged.addListener(function(tabId, selectInfo) {
		chrome.tabs.get(tabId, onTabChange);
	});
	chrome.tabs.onUpdated.addListener(function(tabId, selectInfo) {
		chrome.tabs.get(tabId, onTabChange);
	});

	chrome.extension.onRequest.addListener(function(request, sender, sendResponse) {
		var args = request.args;
		var result = [];
		switch(request.cmd) {
			case"setting":
				if(args) {
					for(var i = 0, len = args.length; i < len; ++i) {
						result.push(setting(args[i]));
					}
				}
				sendResponse({
					result : result
				});
				break;
			default:
				sendResponse({});
				break;
		}
	});
})();

var gExInfo;
/*
 ExtensionInfo
 ( object )
 Information about an installed extension or app.
 id ( string )
 The extension's unique identifier.
 name ( string )
 The name of this extension or app.
 description ( string )
 The description of this extension or app.
 version ( string )
 The version of this extension or app.
 mayDisable ( boolean )
 Whether this extension can be disabled or uninstalled by the user.
 enabled ( boolean )
 Whether it is currently enabled or disabled.
 isApp ( boolean )
 True if this is an app.
 appLaunchUrl ( optional string )
 The launch url (only present for apps).
 homepageUrl ( optional string )
 The URL of the homepage of this extension or app
 offlineEnabled ( boolean )
 Whether the extension or app declares that it supports offline.
 optionsUrl ( string )
 The url for the item's options page, if it has one.
 icons ( optional array of IconInfo )
 A list of icon information. Note that this just reflects what was declared in the manifest, and the actual image at that url may be larger or smaller than what was declared, so you might consider using explicit width and height attributes on img tags referencing these images. See the manifest documentation on icons for more details.
 permissions ( array of string )
 Returns a list of API based permissions.
 hostPermissions ( array of string )
 Returns a list of host based permissions.
 * */

var gManifest;
//manifest.json文件

//用户设置或获取设置
window.setting = function(key, value) {
	if( typeof (value) == "undefined") {
		//get value
		return window.localStorage[key];
	} else {
		//set value
		window.localStorage[key] = value;
		return value;
	}
}
//判断是否是应用的管理员

var EXTENSION_IS_ADMIN = "Extension.IsAdmin";
window.isExtensionAdmin = function() {
	return setting(EXTENSION_IS_ADMIN) == "true";
}