# [linux下tomcat、jenkins环境搭建](https://www.cnblogs.com/lxs1314/p/8567652.html)



**1、安装JDK  我不列出来了，自行百度**

java -version

![img](https://images2018.cnblogs.com/blog/707331/201803/707331-20180314144854167-1796729210.png)

**2、安装tomcat**

（1）将下载的tomcat压缩包

​         `tar -zxvf apache-tomcat-8.5.29.tar.gz`

（2）复制tomcat文件到/opt目录并重命名

```sh
mv apache-tomcat-8.5.29 /opt

cd /opt

mv apache-tomcat-8.5.29  tomcat8
```



​         

（3）为启动的脚本文件添加环境变量

        ```sh
cd tomcat8/bin

vi startup.sh

JAVA_HOME=/usr/java/jdk1.8.0_161

JRE_HOME=/usr/java/jdk1.8.0_161/jre

PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME:$PATH

CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar

TOMCAT_HOME=/opt/tomcat8
        ```



（4）启动tomcat

​        `/startup.sh`

![img](https://images2018.cnblogs.com/blog/707331/201803/707331-20180314145300262-385416494.png)

（5）验证tomcat是否能够启动起来

打开浏览器访问：`localhost:8080`，页面显示的tomcat正常信息，表示配置成功

我这里修改了端口号的，`/conf/server.xml    8080修改成8082的`

![img](https://images2018.cnblogs.com/blog/707331/201803/707331-20180314145531728-1809065761.png)

**3、安装jenkins**

（1）将jenkins.war复制到tomcat的webapps

`cd /opt/tomcat8/webapps`

然后jenkins.war放在这里

（2）配置环境变量

`vi /etc/profile`

`export JENKINS_HOME=/opt/tomcat8/webapps/`

（3）保存退出，使设置生效

`source /etc/profile`

（4）启动tomcat

`cd /opt/tomcat8/bin`

`./startup.sh`

![img](https://images2018.cnblogs.com/blog/707331/201803/707331-20180314145300262-385416494.png)

（5）访问jenkins

浏览器打开http://localhost:8082/jenkins/，即进入jenkins页面

登录密码存在于：`/opt/tomcat8/webapps/jenkins/secrets/initialAdminPassword`

打开文件复制密码到密码栏登陆就行了

`cat /opt/tomcat8/webapps/jenkins/secrets/initialAdminPassword`

![img](https://images2018.cnblogs.com/blog/707331/201803/707331-20180314150219075-1699010133.png)

 

 注：习惯性去的看日志   cd /tomcat/logs      tail -f catalina.out

![img](https://images2018.cnblogs.com/blog/707331/201803/707331-20180314150521354-65378543.png)