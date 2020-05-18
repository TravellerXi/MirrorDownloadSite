#!/usr/bin/python3

# coding:utf-8
#import shutil
from flask import Flask,request
import _thread
import os



basedir = os.path.abspath(os.path.dirname(__file__))

downloadSite='https://mirror.fastspeedgo.xyz'



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
<p>Pls paste the download link to 'Download URL'. Once you have clicked 'Request Download to our mirror', our server will download the resource automatically and deliver a mirror URL with fast download speed to you.
<br>
<p>请在下方'Download URL'处填入下载地址，然后点击'Request Download to our mirror',我们服务器将在后台下载,并提供一个速度快到飞起的链接给您。
<p>返回镜像主站点，Back to main mirror <a href='https://mirror.fastspeedgo.xyz/' target='_blank'>请点此 Click Here</a>。

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
<h1> System now is downloading your resource. Download URL has been generated, pls click below link to go to download page to check if you can download now. <br>
<h1>系统正在下载您的资源，镜像链接已生成，点击下方'download'前往下载地址以查看是否可以下载。<br>

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
<p><a href='https://requestmirror.fastspeedgo.xyz/' target='_blank'>再请求一次下载 Download another resource</a>

</body>
</html>

'''

def Mkdir_andDownload(RealPath,url):
    os.system('mkdir -p ' + RealPath)
    os.system("touch "+RealPath+"/README.html")
    os.system('echo "please do not download this file as server is still downloading. Once you have refreshed the page and you can not see this notice, then you can download all the file." > '+RealPath+"/README.html")
    os.system('wget -P ' + RealPath + ' ' + url)
    os.system('rm -rf '+RealPath+"/README.html")



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
            try :
                _thread.start_new_thread(Mkdir_andDownload,(RealPath,url))
                return (downloadUrl_before + download_url+downloadUrl_after)
            except:
                return ('System internal error, please try again<br><a href="https://requestmirror.fastspeedgo.xyz">back to index</a>')
    elif url.find('http://')>-1:
        path = url[7:]
        RealPath = os.getcwd()[:os.getcwd().find('Download_Programm_SourceCode')] + '/thirdparty/http/' + path
        download_url = downloadSite + '/thirdparty/http/' + path
        if os.path.exists(RealPath):
            return (downloadUrl_before_type2 + download_url+downloadUrl_after)
        else:
            try :
                _thread.start_new_thread(Mkdir_andDownload,(RealPath,url))
                return (downloadUrl_before + download_url+downloadUrl_after)
            except:
                return ('System internal error, please try again<br><a href="https://requestmirror.fastspeedgo.xyz">back to index</a>')




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=False,threaded=True)
