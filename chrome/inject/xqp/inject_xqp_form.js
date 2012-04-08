//AF单的脚本里，写了一句“null != document.frames.ifAttachment”，只有IE和Opera可以读取，因此此处为调整
document.frames = {
	ifAttachment : null
};
