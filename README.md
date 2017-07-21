# Gumballs-And-Dungeons-RandomCode-Helper
因为每天都要蛋疼的访问网站 看一眼密令 <br>
有时候老忘 就定了个闹钟 提醒自己。。。 <br>
后来还是嫌麻烦。。。索性写个脚本自己获取密令 然后给我发邮件吧。。。。 <br>


# 可能需要的安装的库
<pre><code>pip install request</pre></code>
<pre><code>pip install email</pre></code>
<pre><code>pip install configparser</pre></code>


# 使用方法
1. config.ini 配置发信邮箱和收信邮箱<br>
2. 执行mian.py(基于python3)<br>
3. 设置定时任务。。每天12点跑一次<br>

# 关于定时任务
我是用的linux
输入
<pre><code>crontab -e</pre></code>
进入编辑状态

添加行（每日中午12点 执行 并把输出存在 log.log文件上）
<pre><code>0 12 * * * /usr/local/bin/python3 /home/gdhelper/main.py >> /home/gdhelper/log.log 2>&1
</pre></code>

自己把路径改一下 就可以了

使用定时任务时 需要把 mail.py 中 ini文件的路径也改成绝对路径
<pre><code>config.readfp(open('/home/gdhelper/config.ini'))</pre></code>

