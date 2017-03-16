配置新网站

==============

需要安装的包
*nginx
*Python 3
*Git
*pip
*virtualenv


ubuntu
 sudo apt-get install nginx git python3 python3-pip
 sudo pip3 install virtualenv

#配置Nginx虚拟主机

参考nginx.template.conf,把SITENAME替换成所需域名

#upstart任务
参考gunicorn-upstart.template.conf，把SITENAME替换成所需域名

#文件夹结构
/root
   ==sites
    ----SITENAME
       --database
       --source
       --static
       --virtualenv

