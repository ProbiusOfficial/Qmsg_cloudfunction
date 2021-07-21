使用 [Qmsg酱](https://qmsg.zendee.cn/) 基于py完成QQ推送。  

PS：可以部署在云函数上，利用定时执行来完成一定的推送  

这里提供一个可用的模板，供参考~  

Use [Qmsg酱](https://qmsg.zendee.cn/) to complete QQ message push based on python,   
which can be deployed on cloud functions, 
and use timing execution to complete certain push  
Here is a usable template for reference~ 

- - -
MsgSend.py为发信模块，即Qmsg的发送模块，调用方法为：  

` MsgSend.postData("QQNumb",content) `  

index.py为主程序以及入口，诶都是一些API，确实没什么技术含量Qwq......

MsgSend.py is the sending module, that is, the sending module of Qmsg.   
The calling method is:  
`MsgSend.postData("QQNumb",content)`
index.py is the main program and entry point,   
eh......there are some APIs,  
yeah~there is really no technical content ah...... 
