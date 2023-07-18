' 先定义一个Shell对象
Set WshShell = WScript.CreateObject("WScript.Shell")
 
'设置成正需要接续的时间
do
'设置成比屏保时间短点就可以
	WScript.Sleep 60000 '1min 60000ms
	wshShell.SendKeys "{NUMLOCK}"
	WScript.Sleep 500
	wshShell.SendKeys "{NUMLOCK}"
loop
