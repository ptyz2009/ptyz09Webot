这个项目希望做一个打通群聊的机器人

目标：转发任一子群的消息

转发格式

(隔壁)群昵称
消息

##支持消息类型
文字
图片  （前缀和图片将不在同一位置）
表情   (有的表情发得出去，有的发不出去，详情研究中）
公众号名片
地图   （会转为位置名称+链接）
视频

##不支持消息类型
个人名片
语音（会转为mp3,语音消息不多暂不考虑）
文章分享（会转为文章+链接，链接一般很长，会刷屏）
小程序

##完成功能
@机器人    展示状态
不转发文章、语音的分享
查看某人在不在群里   按照群备注查找，所以没改备注会查不到

##待测试场景
群里热闹时，转发不能乱

##计划功能：
机器人运行状态发到监控群

##计划外功能
连续发图、视频时只报1次人名
@机器人 获取群二维码 
只转发身份确认成员的消息
自检消息频率
查看隔壁有谁

##不支持功能
@的传递性(框架不支持)
