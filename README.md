# MirrorDownloadSite
This is a website used for Mirror the resource out site of your country.（为提升下载速度，简历镜像站点，可用来下载Github以及其国外下载文件）
<br><br>
Want to see a sample? Please refer <a href='https://mirror.fastspeedgo.xyz' target='_blank'> to my site </a>.
<br><br>
<a href='https://mirror.fastspeedgo.xyz' target='_blank'>镜像示例网站</a>

<br><br>
可以使用ssh打洞，从本地服务器穿透到云端服务器，本地服务器专门用来下载,本地服务器开启apache文件遍历，云端服务器使用Nginx做反向代理。相应技术参考<a href='https://blog.mytlu.cn/?p=6' target='_blank'>我的博客</a><br>
Apache ftp站点根目录为 /var/www/html/ftp，文件结构为：<br>
├── Download_Programm_SourceCode<br>
├── README.html<br>
├── thirdparty<br>
│   ├── http<br>
│   ├── https<br>
│   └── README.html<br>

<br>
将本项目中的main.py放入ownload_Programm_SourceCode文件夹并使用'nohup python3 -u main.py > main.log 2>&1 &'来启动该项目。（请事先pip install flask）然后为该Python网页打洞穿透到远程服务器。

<br><br>
如遇到ssh打洞不定时TCP连接断开（表现为端口不通），请使用daemon文件夹里的守护进程来定期更换端口并重启Nginx。请创建/daemon文件夹并将本项目daemon文件夹里的守护进程放入其中，设置crontab的定时任务请仿照如下：<br>
*/1 * * * * root /usr/bin/python3 /daemon/daemon-requestmirror.py
*/1 * * * * root /usr/bin/python3 /daemon/daemon-ftp.py

两个守护进程，其中第一个为手动请求镜像的守护进程，第二个是apache ftp站点守护进程。（守护进程主要靠更换ssh打洞的端口来持续连接）


