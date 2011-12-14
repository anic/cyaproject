/**
 * 1 屏蔽中间弹窗;先使用折中的办法转向空白页
 */
(function init() {

	var target = "http://pac.gmcc.net/smc/template/lib/dishi2/JsonObjects/news/middleWindow.jsp";
	var src = window.location.href;

	if(src.indexOf(target) == -1)
		return;

	var bodyContent = document.body.innerHTML;
	var headContent = document.head.innerHTML;
	var linkMatch = headContent.match(/<link [^<]*href="([^"]*)"[^<]*>/);
	var scriptMatch = headContent.match(/<script[^>]*>([\w\W.\n]*)<\/script>/m);

	//这句话会覆盖body和head的所有内容
	document.writeln(bodyContent);

	if(linkMatch)
		window.loadjscssfile(linkMatch[1], "css");

	if(scriptMatch) {
		//根据这页的脚本内容作出修改
		var s = scriptMatch[1];
		//window.onload 的时机已经错过，因此在最后补上函数的执行
		s = s.replace("window.onload", "windowOnload");
		//禁用最恶心的一句alert：alert( navigator.appName+" "+navigator.appVersion );
		s = s.replace("alert( navigator.appName+\" \"+navigator.appVersion );", "//alert( navigator.appName+\" \"+navigator.appVersion );");
		s += "windowOnload();";
		window.loadjscssfile(s);
	}
	//旧的做法是重定向到空白页
	// window.location.href = "about:blank";

	return;
	//无法访问head的children
	// var s = document.head.children[3];

})();

//http://pac.gmcc.net/smc/template/lib/dishi2/JsonObjects/news/middleWindow.jsp?channelId=DISHI2_middle&url=http%3A%2F%2Fgmccnews.gmcc.net%2Fgetnews.aspx

//内容

// <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
//
// <html>
// <head>
// <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
// <title>新闻</title>
//
//
// <link href="../../ext/resources/images/default/root/css2.css" rel="stylesheet" type="text/css" />
// <script type="text/javascript">
// //2010 0128 -- 14:46 by zhu tai jiang
//
// var xmlhttprequest ;
//
// var IEenv;
//
// function getIEVersion(){
// if(navigator.appName == "Microsoft Internet Explorer")
// {
// if(navigator.appVersion.match(/7./i)=='7.'){
// IEenv = "ie7";
// }else if(navigator.appVersion.match(/6./i)=='6.'){
// IEenv = "ie6";
// }
// }else{
// alert( navigator.appName+" "+navigator.appVersion );
// }
// }
//
// window.onload=function(){
// getIEVersion();
// //alert(IEenv);
//
// var request = false;
// try {
// 　request = new ActiveXObject("Microsoft.XMLHTTP");
// } catch (trymicrosoft) {
// 　try {
// 　　request = new ActiveXObject("Msxml2.XMLHTTP");
// 　} catch (othermicrosoft) {
// 　　try {
// 　　　request = new XMLHttpRequest();
// 　　} catch (failed) {
// 　　　request = false;
// 　　}
// 　}
// }
// xmlhttprequest = request;
//
// xmlhttprequest.open("GET","../../JsonObjects/news/dataproxy.jsp?url=http://gmccnews.gmcc.net/getnews.aspx",true);
// xmlhttprequest.onreadystatechange=setSelect;
// xmlhttprequest.send(null);
// }
//
// function setSelect(){
//
// if(xmlhttprequest.readyState==4){
// if(xmlhttprequest.status==200){
// var son=xmlhttprequest.responseText;
// try{
// var json=eval(son);
// startHtml(json);	//执行startHtml
// }catch(err){
// errHtml();
// }
//
// }
// }
// }
//
// function errHtml(){
// var html="";
// html=  '<table width="525" border="0"  cellpadding="0" cellspacing="0"> '+
// ' <tr>'+
// '  <td><img src="../../ext/resources/images/default/root/title2.jpg" width="525" height="22" /></td>'+
// '</tr>'+'<tr><td style="height:10px "></td></tr><tr><td><h3>系统出现异常,请检查数据提供格式!</h3></td></tr>'
//
// '</table>';
// document.getElementById('ToDoControl').innerHTML = html;
// }
//
// function startHtml(json)
// {
//
//
// var html="";
// html=  '<table width="525" border="0"  cellpadding="0" cellspacing="0"> '+
// //   ' <tr>'+
// //   '  <td><img src="../../ext/resources/images/default/root/title2.jpg" width="525" height="22" /></td>'+
// //  ' </tr>'+
// ' <tr>'+
// ' <td><table width="525" border="0" cellpadding="0" cellspacing="0" bgcolor="#ced3db">'+
// '     <tr>'+
// '      <td valign="top" class="title_bg">'+
// '     <table  id="tblImportantNews" width="100%" border="0" align="center" cellpadding="2" cellspacing="0" style="margin-top: -3px;background-image:url(../../ext/resources/images/default/root/title_bg.jpg); background-repeat: repeat-x; ">' ;
// html += '  	<tr style="height:10px">	<td></td></tr>';
// var tempLength = 0;	//临时长度变量
// var titleStr = "";
// for(var i = 0 ; i < json.results.length ;i++)  //要闻数据遍历
// {
// var subojb = json.results[i];
// if(subojb.typename=="IMN")
// {
// tempLength=tempLength+1 ;
// if (tempLength<8){
// titleStr = subojb.title;
// if(titleStr.length>32){ titleStr = titleStr.substring(0,32)+"..."; }
// var   strArray = new   Array();
// strArray=subojb.issuedate.split(" ");
// html +=  '<tr>';
// html +=  '<td width="88%" align="left"><a href="'+ subojb.url +'" title="'+subojb.title+'" class="left_link3" target="_blank" >&nbsp;&nbsp;&nbsp;<img  src=\"../../ext/resources/images/default/root/dian.gif\" style=\"height: 3px;width: 3px;margin-top: -3px;TEXT-DECORATION:none;border: 0;vertical-align: middle\">&nbsp;&nbsp;'+ titleStr +'</a></td>'+
// '<td width="12%" align="right" class="zi-5">'+ strArray[0]
// // subojb.issuedate.substring(0,10)
// +'&nbsp;</td>'
// +'</tr>';
// }
// }
// }
// //more  and video
// var videoTempLength = 0 ; //临时长度变量
// for(var i = 0 ; i < json.results.length ;i++){	//视频
// var subojb = json.results[i];
// if(subojb.typename=="VIDEO"){
// if(videoTempLength==0){
// titleStr = subojb.title;
// if(titleStr.length>35){ titleStr = titleStr.substring(0,35)+"..."; }
// html +=  '<tr>';
// html +=  '<td width="88%" align="left" class="zi-5">&nbsp;&nbsp;<img border="0" src="../../ext/resources/images/default/video.gif"><a href="'+ subojb.url +'" title="'+subojb.title+'" target="_blank" style="vertical-align: middle">&nbsp;&nbsp;'+titleStr+'</a> </td>'+
// '<td width="12%" align="left" class="zi-5"><a href="http://gmccnews.gmcc.net/list.aspx?typeid=1" target="_blank">&nbsp;&nbsp;&nbsp;&nbsp;<img border="0" src="../../ext/resources/images/default/more.gif"></td>'
// +'</tr>';
// videoTempLength = videoTempLength + 1 ;
// }
// }
// }
//
// html +=  '</table> ';
// if(IEenv=="ie7"){
// html += '<table><tr><td style="height:4"></td></tr></table>';
// }else{
// html += '<table><tr><td style="height:10"></td></tr></table>';
// }
// html += '  <table width="524" border="0" align="right" cellpadding="0" cellspacing="0" style="background-image: url(../../ext/resources/images/default/root/title_s4_bg.jpg);background-repeat: no-repeat;background-position: right 32px;"> '+
// '     <tr> '+
// '       <td width="260"><div align="left"><img src="../../ext/resources/images/default/root/title_s1.jpg" width="260" height="21" /></div></td>'+
// '        <td width="260"><img src="../../ext/resources/images/default/root/title_s2.jpg" width="260" height="21" /></td>'+
// '     </tr>'+
// '     <tr>'+
// '       <td valign="top"><table width="98%" border="0" cellspacing="0" cellpadding="2">';
// var iMKT=0 ;
//
// if(IEenv=="ie7"){
// html += '<tr><td style="height:3px;"></td></tr>';
// }else{
// html += '';
// }
//
// for(var i = 0 ; i < json.results.length;i++)  //数据遍历
// {
// var subojb = json.results[i];
// if(subojb.typename=="MKT"){
// iMKT = iMKT+1 ;
// if (iMKT<3)
// {
// if(IEenv=="ie7"){
// html += '';
// }else{
// html += '<tr><td style="height:4px;"></td></tr>';
// }
// html +=  '<tr>';
// var stitle=     subojb.title ;
// if (stitle.length>19)
// stitle =stitle.substring(0,18)+"...";
// html +=  '<td width="258px" align="left"><a  href="'+ subojb.url +'" title="'+subojb.title+'" class="left_link3"  target="_blank">&nbsp;&nbsp;&nbsp;<img  src=\"../../ext/resources/images/default/root/dian.gif\" style=\"height: 3px;width: 3px;margin-top: -3px;TEXT-DECORATION:none;border: 0;vertical-align: middle\">&nbsp;&nbsp;'+ stitle +'</a></td>';
// if(IEenv=="ie7"){
// html += '';
// }else{
// html += '</tr> <tr><td style="height:3px;"></td></tr>';
// }
// }
// }
// }
//
// html +=  ' </table></td> '+
// '  <td width="260" height="62" valign="top" ><table width="98%" border="0" align="left" cellpadding="2" cellspacing="0"> ';
// iMKT=0 ;
// html += '<tr><td style="height:4px;"></td></tr>';
// for(var i = 0 ; i < json.results.length;i++)  //数据遍历
// {
// var subojb = json.results[i];
// if(subojb.typename=="NTW"){
// iMKT = iMKT+1 ;
// if (iMKT<3)
// {
// var stitle=     subojb.title ;
// if (stitle.length>19)
// stitle =stitle.substring(0,18)+"...";
// html +=  '<tr>';
// html +=  '<td width="258px" align="left"><a  href="'+ subojb.url +'" title="'+subojb.title+'"  class="left_link3"  target="_blank">&nbsp;&nbsp;&nbsp;<img  src=\"../../ext/resources/images/default/root/dian.gif\" style=\"height: 3px;width: 3px;margin-top: -3px;TEXT-DECORATION:none;border: 0;vertical-align: middle\">&nbsp;&nbsp;'+ stitle +'</a></td>';
// if(IEenv=="ie7"){
// html += '';
// }else{
// html += '</tr> <tr><td style="height:7px;"></td></tr>';
// }
// }
// }
// }
//
// html +=  '   </table></td> '+
// '  </tr> '+
// '    <tr>'+
// '     <td width="260"><div align="left"><img src="../../ext/resources/images/default/root/title_s3.jpg" width="260" height="21" /></div></td>'+
// '    <td><img src="../../ext/resources/images/default/root/title_s4.jpg" width="260" height="21" /></td>'+
// '   </tr>'+
// '   <tr>'+
// '    <td valign="top" ><table width="98%" border="0" cellspacing="0" cellpadding="2">'  ;
// iMKT=0 ;
//
// html += '<tr><td style="height:4px;"></td></tr>';
// for(var i = 0 ; i < json.results.length;i++)  //数据遍历
// {
// var subojb = json.results[i];
// if(subojb.typename=="MNG"){
// iMKT = iMKT+1 ;
// if (iMKT<3)
// {
// html +=  '<tr>';
// var stitle=     subojb.title ;
// if (stitle.length>19)
// stitle =stitle.substring(0,18)+"...";
// html +=  '<td width="258px" align="left"><a  href="'+ subojb.url +'" title="'+subojb.title+'"  class="left_link3"  target="_blank">&nbsp;&nbsp;&nbsp;<img  src=\"../../ext/resources/images/default/root/dian.gif\" style=\"height: 3px;width: 3px;margin-top: -3px;TEXT-DECORATION:none;border: 0;vertical-align: middle\">&nbsp;&nbsp;'+ stitle +'</a></td>';
// if(IEenv=="ie7"){
// html += '';
// }else{
// html += '</tr> <tr><td style="height:5px;"></td></tr>';
// }
//
// }
// }
// }
//
// html +=  '   </table></td> '+
// '   <td width="260" height="60"  valign="top" ><table width="98%" border="0" align="left" cellpadding="2" cellspacing="0">';
// iMKT=0 ;
//
// html += '<tr><td style="height:4px;"></td></tr>';
// for(var i = 0 ; i < json.results.length;i++)  //数据遍历
// {
// var subojb = json.results[i];
// if(subojb.typename=="BLN"){
// iMKT = iMKT+1 ;
// if (iMKT<3)
// {
// html +=  '<tr>';
// var stitle=     subojb.title ;
// if (stitle.length>19)
// stitle =stitle.substring(0,18)+"...";
// html +=  '<td width="258px" align="left"><a  href="'+ subojb.url +'" title="'+subojb.title+'"  class="left_link3"  target="_blank">&nbsp;&nbsp;&nbsp;<img  src=\"../../ext/resources/images/default/root/dian.gif\" style=\"height: 3px;width: 3px;margin-top: -3px;TEXT-DECORATION:none;border: 0;vertical-align: middle\">&nbsp;&nbsp;'+ stitle +'</a></td>';
// if(IEenv=="ie7"){
// html += '';
// }else{
// html += '</tr> <tr><td style="height:5px;"></td></tr>';
// }
//
// }
// }
// }
//
// html +=  '    </table></td>'+
// '   </tr>'+
//
// '    </table></td> '+
// '   </tr>   </table> ';
//
//
// document.getElementById('ToDoControl').innerHTML = html;
// }
// </script>
//
// </head>
// <body >
// <div id="ToDoControl"></div>
// </body>
// </html>