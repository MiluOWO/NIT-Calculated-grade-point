# NIT-Calculated-grade-point
没啥好说的，网址是一个学校选课的网址，偶然发现可以查询成绩。遂利用了一些库文件计算了一下。

有一些点需要注意：

1.该项目的python版本为：3.6.4

2.需要pip一些库文件，缺一不可

3.在自己的主机端运行需要	app.run(host='0.0.0.0',port=80,debug=False) 这里改成127.0.0.1 端口随便。（但是改了一定要127.0.0.1:端口号）

4.关闭之后，服务器也是关闭的状态。

## 需要pip3 install 的一些库：

flask

flask-wtf

requests

beautifulsoup4

### 为什么存在网页上的说的BUG？

1. 计算绩点本来就是为了方便奖学金，挂科==没有奖学金。

2. 抓取的数据有点杂，没有区分补考。要计算的话1.没什么必要，2.处理有点麻烦

3.没有了。

### 最后一点

这个东西一开始就写着玩的，整个工作时间加起来应该就2天，虽然是断断续续但是还是学到了一些有趣的东西。

代码很乱，但我崇尚“能用就行”，所以不要吐槽我的代码结构。:)

如果有意见可以QQ找我。

http://132.232.22.57:5000/  这个是实践产物（说不定过几天就没有惹）

