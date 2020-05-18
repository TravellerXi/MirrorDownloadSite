#!/usr/bin/python3

# coding:utf-8
import os
#import time
import random
import paramiko

BeforeServiceContent='''
[Unit]
Description=Transfer local 80 port to remote 27281
After=network-online.target
[Service]
User=root
Type=simple
ExecStart=/usr/bin/autossh -M 5178 -NR '''
AfterServiceContent=''':localhost:80 -i /root/.ssh/id_rsa goodmorning@199.188.100.90 -p 27278 >> /dev/null 2>&1
ExecReload=/bin/kill -HUP $MAINPID
ExecStop=/bin/kill -TERM $MAINPID
KillMode=process
Restart=no
[Install]
WantedBy=multi-user.target
WantedBy=graphical.target


'''

BeforeServerContent = '''
server {
    listen 80;
    listen [::]:80;
    server_name mirror.fastspeedgo.xyz;
    # enforce https
    return 301 https://mirror.fastspeedgo.xyz;
}

server
    {
        listen 443 ssl http2;
        #listen [::]:443 ssl http2;
        server_name mirror.fastspeedgo.xyz;
        index index.html index.htm index.php default.html default.htm default.php;
        #root  /home/wwwroot/fastspeedgo.xyz;
                access_log /simpledrive/static/mirror.fastspeedgo.xyz.log;

        ssl_certificate /usr/local/nginx/conf/ssl/cloud.fastspeedgo.xyz/fullchain.cer;
        ssl_certificate_key /usr/local/nginx/conf/ssl/cloud.fastspeedgo.xyz/cloud.fastspeedgo.xyz.key;
        ssl_session_timeout 5m;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
        ssl_prefer_server_ciphers on;
        ssl_ciphers "TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-128-CCM-8-SHA256:TLS13-AES-128-CCM-SHA256:EECDH+CHACHA20:EECDH+CHACHA20-draft:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5";
        ssl_session_cache builtin:1000 shared:SSL:10m;
        # openssl dhparam -out /usr/local/nginx/conf/ssl/dhparam.pem 2048
        ssl_dhparam /usr/local/nginx/conf/ssl/dhparam.pem;

                proxy_redirect http:// $scheme://;
        port_in_redirect on;
        location ~ ^/ {
        proxy_buffering off;
           proxy_pass http://127.0.0.1:'''
AfterServerContent = ''';
           proxy_http_version 1.1;
                   proxy_set_header  Host $host:$server_port;
          # proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass_header User-Agent;
        #proxy_pass_header X-Forwarded-Proto;
        proxy_set_header X-Forwarded-Proto $scheme;
           client_max_body_size 10240M;
           client_body_timeout 5m;
        #keepalive_timeout  30;

          }

    }


 '''




if __name__=='__main__':
    os.system('rm -rf /tmp/index.htm*')
    os.system('wget -P /tmp/ https://mirror.fastspeedgo.xyz/ --proxy=no --timeout=10 -t 1')
    if os.path.exists('/tmp/index.html'):
        os.system('rm -rf /tmp/index.htm*')
    else:
        randomPort = random.randint(100, 999)
        os.system('systemctl stop ssh-retransfer-80to27281.service')
        os.system('rm -rf /usr/lib/systemd/system/ssh-retransfer-80to27281.service')
        with open('/usr/lib/systemd/system/ssh-retransfer-80to27281.service', 'w') as f:
            f.write(BeforeServiceContent + str('28') + str(randomPort) + AfterServiceContent)
        os.system('systemctl daemon-reload')
        os.system('systemctl start ssh-retransfer-80to27281.service')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        ssh.connect(hostname='199.188.100.90', port=27278, username='root')
        ssh.exec_command('rm -rf /usr/local/nginx/conf/vhost/mirror.fastspeedgo.xyz.conf')
        ssh.exec_command('echo '+"'"+BeforeServerContent+str('28')+str(randomPort)+AfterServerContent+"' >/usr/local/nginx/conf/vhost/mirror.fastspeedgo.xyz.conf")
        ssh.exec_command('service nginx stop')
        ssh.exec_command('service nginx start')
        ssh.close()
