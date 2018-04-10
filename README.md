# Evilsays_bot
### Introduction
Evilsays_bot是一个非常简单的Telegram机器人，我用它来查询CVE相关的东西，它的代码逻辑很简单，  
解析csv文件获取CVE相关信息，然后存入mysql数据库中，利用pyTelegramBotAPI进行编写我们的业务逻辑  
我也单独写了一个update_csv的代码用于辨识是否有新的更新，但是还没有完善，应该要加上celery或者  
放到crontab事件里面用于日常更新。
### Functions
1. CVE查询（目前暂时只支持cve编号查询 例如：CVE-1999-1010）
2. CVE模糊查询 （逻辑很简单,也非常容易实现，但是目前没写） todo
3. 乌云知识库查询 (这个我想了我应该要加上这个，乌云对于白帽子来说实在是太重要了) todo
4. 通用CMS漏洞检查 （这个也是我感兴趣的，我应该很快就能更新好） todo
5. 端口服务扫描 （这个之前在QQ机器人上已经写完了 还加了其他几个无聊的功能 可以移植过来）todo
6. 等等... 有好的建议麻烦联系我tg @toorKios

### Requirements
```
lxml  
MySQL-python
DBUtils
pyTelegramBotAPI
requests
```
### Renderings
![main](https://raw.githubusercontent.com/3lackrush/Evilsays_bot/master/assets/main.jpg)
