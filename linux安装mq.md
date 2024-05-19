### 在linux上安装Maven

1、下载文件

wget https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz

2、解压文件

tar -zxf apache-maven-3.6.3-bin.tar.gz 

3、移动文件

mv apache-maven-3.6.3 /usr/local/

4、修改配置文件

修改文件名字：mv apache-maven-3.6.3/ maven

cd maven/

cd conf/

vi settings.xml

~~~
<mirror>
    <id>aliyunmaven</id>
    <mirrorOf>*</mirrorOf>
    <name>阿里云公共仓库</name>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>
~~~



5、配置环境变量

修改：/etc/profile

source /etc/profile

export M2_Home=/usr/local/maven

export PATH=$PATH:$M2_HOME/bin

6、进入rocketmq主目录编译项目

mvn -Prelease-all -DskipTests  clean install -U



