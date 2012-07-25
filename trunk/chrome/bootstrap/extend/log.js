//bootstrap 的提示框扩展，使用js弹出提示在顶部
window.Log = (function() {
	return {
		_alert : function(m, element, className) {
			// <div class="alert">
			// <a class="close" data-dismiss="alert">×</a>
			// <strong>警告！</strong> 不要拿法律当挡箭牌。
			// </div>
			if (!element)
				element = document.body;
			$(element).after(' <div class="alert ' + className + '">' + m + '</div>');
		},
		/**
		 * log 提示用户信息
		 */
		success : function(m, element) {
			this._alert(m, element, "alert-success");
		},
		/**
		 * err 显示错误提示
		 */
		error : function(m, element) {
			this._alert(m, element, "alert-error");
		},
		info : function(m, element) {
			this._alert(m, element, "alert-info");
		}
	};
})();
