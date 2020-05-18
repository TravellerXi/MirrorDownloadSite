#!/usr/bin/python3
# coding:utf-8
#Author: Github https://github.com/TravellerXi/
#Need to build up a file tree like this:

#├── Download_Programm_SourceCode
#├── README.html
#├── thirdparty
#│   ├── http
#│   ├── https
#│   └── README.html

#this py file need to put at Download_Programm_SourceCode folder.

from flask import Flask,request,session,redirect,Response
import os
import time


basedir = os.path.abspath(os.path.dirname(__file__))

downloadSite='https://mirror.fastspeedgo.xyz' ##enter the apache ftp site that you have built



app =Flask(__name__)

downloadHtml='''



<!--                       .::::.
//                     .::::::::.
//                    :::::::::::
//                 ..:::::::::::'
//              '::::::::::::'
//                .::::::::::
//           '::::::::::::::..
//                ..::::::::::::.
//              ``::::::::::::::::
//               ::::``:::::::::'        .:::.
//              ::::'   ':::::'       .::::::::.
//            .::::'      ::::     .:::::::'::::.
//           .:::'       :::::  .:::::::::' ':::::.
//          .::'        :::::.:::::::::'      ':::::.
//         .::'         ::::::::::::::'         ``::::.
//     ...:::           ::::::::::::'              ``::.
//    ```` ':.          ':::::::::'                  ::::..
//                       '.:::::'                    ':'````..
-->

<script>
console.log("有缘人:");
console.log("本站由Python Flask开发");
console.log("Github https://github.com/TravellerXi/")
</script>

<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset=utf-8"utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="SimpleDrive">
    <meta name="keyword" content="SimpleDrive">
 <title>Request Download</title>
 </head>
<body>
<p>Pls paste the download link to 'Download URL'. Once you click 'Request Download to our mirror', our server will download the resource automatically and deliver a mirror URL with fast download speed to you.
<br>
<p>请在下方'Download URL'处填入下载地址，然后点击'Request Download to our mirror',我们服务器将在后台下载,并提供一个速度快到飞起的链接给您。
<p>返回镜像主站点，<a href='https://mirror.fastspeedgo.xyz/' target='_blank'>请点此</a>。

<form action="/" method="post">
                    <input type="hidden" style="visibility: hidden;" name="formname" value="usernamepasswd" />

                                      <p>Download URL：<input name="url"></p>

                                      <p><button type="submit">Request download to our mirror</button></p>

                                      </form>

</body>
</html>


'''
downloadUrl_before='''


<!--                       .::::.
//                     .::::::::.
//                    :::::::::::
//                 ..:::::::::::'
//              '::::::::::::'
//                .::::::::::
//           '::::::::::::::..
//                ..::::::::::::.
//              ``::::::::::::::::
//               ::::``:::::::::'        .:::.
//              ::::'   ':::::'       .::::::::.
//            .::::'      ::::     .:::::::'::::.
//           .:::'       :::::  .:::::::::' ':::::.
//          .::'        :::::.:::::::::'      ':::::.
//         .::'         ::::::::::::::'         ``::::.
//     ...:::           ::::::::::::'              ``::.
//    ```` ':.          ':::::::::'                  ::::..
//                       '.:::::'                    ':'````..
-->

<script>
console.log("有缘人:");
console.log("本站由Python Flask开发");
console.log("Github https://github.com/TravellerXi/")
</script>

<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset=utf-8"utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="DownloadSource">
    <meta name="keyword" content="DownloadSource">
 <title>Download source</title>
 </head>
<body>
<h1> Download URL has been generated, pls click below link to go to download page. <br>
<h1>镜像链接已生成，点击下方'download'前往下载地址<br>

<td><a href="

'''

downloadUrl_before_type2='''


<!--                       .::::.
//                     .::::::::.
//                    :::::::::::
//                 ..:::::::::::'
//              '::::::::::::'
//                .::::::::::
//           '::::::::::::::..
//                ..::::::::::::.
//              ``::::::::::::::::
//               ::::``:::::::::'        .:::.
//              ::::'   ':::::'       .::::::::.
//            .::::'      ::::     .:::::::'::::.
//           .:::'       :::::  .:::::::::' ':::::.
//          .::'        :::::.:::::::::'      ':::::.
//         .::'         ::::::::::::::'         ``::::.
//     ...:::           ::::::::::::'              ``::.
//    ```` ':.          ':::::::::'                  ::::..
//                       '.:::::'                    ':'````..
-->

<script>
console.log("有缘人:");
console.log("本站由Python Flask开发");
console.log("Github https://github.com/TravellerXi/")
</script>

<!DOCTYPE html>
<html lang="cn">
<head>
    <meta charset=utf-8"utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="DownloadSource">
    <meta name="keyword" content="DownloadSource">
 <title>Download source</title>
 </head>
<body>
<h1>Someone has aleady generated the url, pls click below link to go to download page<br>
<h1>已有人提交该资源，点击下方'download'前往下载地址<br>
<p><td><a href="

'''


downloadUrl_after='''

" target="_blank">download</a></td><br>
<p><a href='https://requestmirror.fastspeedgo.xyz/' target='_blank'>再请求一次下载</a>

</body>
</html>

'''




@app.route('/', methods=['GET'])

def signin_form():
    return (downloadHtml)

@app.route('/', methods=['POST'])
def download_post():
    url = str(request.form['url'])
    if url.find('https://')>-1:
        path=url[8:]
        RealPath=os.getcwd()[:os.getcwd().find('Download_Programm_SourceCode')]+'/thirdparty/https/'+path
        download_url = downloadSite + '/thirdparty/https/' + path
        if os.path.exists(RealPath):
            return (downloadUrl_before_type2+download_url+downloadUrl_after)
        else:
            os.system('mkdir -p '+RealPath)
            os.system('wget -P '+RealPath+' '+ url)
            return (downloadUrl_before + download_url+downloadUrl_after)
    elif url.find('http://')>-1:
        path = url[7:]
        RealPath = os.getcwd()[:os.getcwd().find('Download_Programm_SourceCode')] + '/thirdparty/http/' + path
        download_url = downloadSite + '/thirdparty/http/' + path
        if os.path.exists(RealPath):
            return (downloadUrl_before_type2 + download_url+downloadUrl_after)
        else:
            os.system('mkdir -p ' + RealPath)
            os.system('wget -P '+RealPath+' '+ url)
            return (downloadUrl_before + download_url+downloadUrl_after)






if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=False,threaded=True)
