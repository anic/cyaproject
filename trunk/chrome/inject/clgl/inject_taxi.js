(function init(){
	
	//允许手动编辑日期
	var apDate = document.getElementById("ApplyingDate")
	apDate.readOnly = false;
	
	//自动计算里程数
	var pay = document.getElementById("TaxiPayment");
	pay.addEventListener("keyup",function(){
		if (pay.value)
		{
			var v = window.parseFloat(pay.value);
			var kilo = document.getElementById("UsedMileage");
			kilo.value = window.parseInt(v / 2.6 * 100) / 100;
		}
	});
	
		
	//自动设置出发点和结束点
	var u = document.getElementById("IsRefund_radio");
	var l = u.children[1];
	if(l) {
		u.addEventListener("click",function(){
			var st = document.getElementById("StartPointLocationName");
			st.value = "金海大厦";
			
			var ed = document.getElementById("EndPointLocationName");
			ed.value = "全球通大厦";
		});
	}
	
	//设置时间
	var apptime = document.getElementById("ApplyingTime");
	
	var stHour = apptime.children[0].children[0];
	var stMinute = apptime.children[0].children[2];
	
	
	var edHour = apptime.children[2].children[0];
	var edMinute = apptime.children[2].children[2];
	
	
	stHour.selectedIndex = 8;
	stMinute.selectedIndex = 2;
	edHour.selectedIndex = 17;
	edMinute.selectedIndex = 2;
	
	//设置发票张数
	var receiptCount = document.getElementById("ReceiptCount");
	if (receiptCount)
		receiptCount.value = 1;

})();

