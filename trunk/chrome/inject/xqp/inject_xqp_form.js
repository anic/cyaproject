//AF单的脚本里，写了一句“null != document.frames.ifAttachment”，只有IE和Opera可以读取，因此此处为调整
(function adjustTemplate() {
	var ifAttachment = document.getElementById("ifAttachment");
	if(ifAttachment) {
		//如果存在表单，则定义之，是if可以进入
		document.frames = {
			ifAttachment : {
				document : {
					all : {
						ucAttachment_trTemplateHeader : {
							parentElement : null
						}
					}
				}
			}
		};

		/*
		 在AF单界面中有这样的代码，如果用document.frame={ifAttachment : null}进行忽略，则无法产生template对象，也会让后面运行出错
		 if (null != document.frames.ifAttachment) {
		 var template = document.frames.ifAttachment.document.all.ucAttachment_trTemplateHeader.parentElement;
		 template.style.display = "none";
		 }*/
		$(ifAttachment).load(function() {
			document.frames.ifAttachment.document.all.ucAttachment_trTemplateHeader.parentElement = ifAttachment.contentWindow.document.getElementById("tbTemplate");
		});
	} else {
		//否则，跳过if判断
		document.frames = {
			ifAttachment : null
		};
	}
})();
