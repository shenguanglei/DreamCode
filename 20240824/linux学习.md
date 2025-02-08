# centos

## 优化网络管理：

systemctl stop NetworkManger 临时关闭

systemctl disable NetworkManger 永久关闭

```bash
sudo systemctl disable NetworkManager
```

但请注意，禁用 `NetworkManager` 可能会导致您的网络连接配置变得复杂，特别是如果您依赖于 `NetworkManager` 来管理网络连接（如Wi-Fi连接）的话。

如果您之后决定重新启用 `NetworkManager`，可以使用以下命令：

```bash
bash复制代码

sudo systemctl enable NetworkManager
```

然后，如果需要，您可以启动该服务：

```bash
bash复制代码

sudo systemctl start NetworkManager
```

总之，确保您正确拼写服务名称，并根据需要使用 `sudo` 来获取必要的权限。

## 设置服务器静态IP 地址

GATEWAY ----  网关

IPADDR IP---- 地址

NETMASK ---子网掩码

DNS ---域名解析

![image-20240824180803328](D:\github\image-20240824180803328.png)

~~~
1、找到网络配置文件
cd /etc/sysconfig/network-scripts/ 
2、下载修改配置文件工具
yum install y vim
3、备份网络配置文件
cp -r ifcfg-ens33 ifcfg-ens33bak
4、查看备份成功
ls -a -l
5、修改网络配置文件
GATEWAY=10.0.0.2
IPADDR=10.0.0.132
NETMASK=255.255.255.0
DNS1=10.0.0.2
DNS2=1.2.4.8

GATE
6、重启网络配置文件
systemctl restart network
date                      # 查看时间
yum install ntp           # 安装ntp
systemctl enable ntpd     # 开机启动
systemctl start ntpd      # 启动服务
timedatectl set-timezone Asia/Shanghai # 更改时区
timedatectl set-ntp yes   # 启用ntp同步
ntpq -p # 同步时间         # 如果报错执行下面命令
 
service ntpd start        # 启动ntpd
ntpdate -u cn.pool.ntp.org 
~~~



1. **设置静态IP**：
   假设你的网络接口名称是`ens33`，你可以使用以下命令来设置静态IP。这里以IP地址`192.168.1.100`，子网掩码`255.255.255.0`（或CIDR表示法`/24`），网关`192.168.1.1`，DNS服务器`8.8.8.8`为例：

   ```bash
   sudo nmcli con mod ens33 ipv4.addresses 192.168.1.100/24  
   sudo nmcli con mod ens33 ipv4.gateway 192.168.1.1  
   sudo nmcli con mod ens33 ipv4.dns "8.8.8.8"  
   sudo nmcli con mod ens33 ipv4.method manual  
   sudo nmcli con up ens33
   ```

   注意：`ipv4.method manual`表示使用静态IP。

2. **验证设置**：
   使用`ip addr`或`nmcli con show`来验证你的设置。

### 方法2：直接编辑网络配置文件

如果你不使用NetworkManager，或者出于某种原因想要直接编辑网络配置文件，你可以这样做：

1. **找到网络配置文件**：
   对于CentOS 7，网络配置文件通常位于`/etc/sysconfig/network-scripts/`目录下，文件名类似于`ifcfg-ens33`（这里的`ens33`是你的网络接口名称）。

2. **编辑配置文件**：
   使用文本编辑器（如`vi`或`nano`）编辑该文件。你需要设置或确认以下行：

   ```bash
   BOOTPROTO=static  
   ONBOOT=yes  
   IPADDR=192.168.1.100  
   NETMASK=255.255.255.0  
   GATEWAY=192.168.1.1  
   DNS1=8.8.8.8
   ```

   注意：`BOOTPROTO=static`表示使用静态IP。

3. **重启网络服务**：
   如果你正在使用`network`服务而不是NetworkManager，你可以通过以下命令重启网络服务来应用更改：

   ```bash
   bash复制代码
   
   sudo systemctl restart network
   ```

   或者，如果你仍然使用`service`命令：

   ```bash
   bash复制代码
   
   sudo service network restart
   ```

   但是，请注意，CentOS 7默认使用`systemd`，因此推荐使用`systemctl`命令。

4. **验证设置**：
   使用`ip addr`来验证你的IP地址和其他网络设置。

选择哪种方法取决于你的具体需求和你是否使用NetworkManager。如果你不确定，可以先尝试使用`nmcli`，因为它提供了更现代的接口来管理网络设置。

## 修改linux源

### 找到目录

cd /etc/yum.repos.d/

1、帮助 man

2、快捷方式

3、目录管理

cd / ~ . ..  cd ~

ls命令

ls -l  

ls -a  

ls -a  -l 隐藏文件或目录

pwd命令 任意目录下都可以获取当前的工作路劲

mkdir命令

​	mkdir 目录名

​	mkdir -p 第一层、第二层

rmdir 删除一个空目录

rm 命令

​	rm -r  删除目录-目录子目录和文件-一层一层递归删除

​	rm -f  不需要确认-强制删除-需谨慎

​	rm -r 删除的时候需要确认信息

cp 命令

​	cp -r  递归复制目录和目录下子目录以及文件

mv命令

​	相同目录下-重命名

​	非相同目录下-移动/剪切

ehco 输出重定向

~~~
> 输出重定向覆盖的方式写入 例子： a.txt 
>> 输出重定向追加的方式写入 例子：
2>> 错误的信息追加
&>> 正确的和错误的命令追加
~~~

cat 命令高级-重定向输入

tac 从文件的最后一行显示文件的内容

nl 显示行号-从文件的第一行显示文件的内容

more 一页一页翻动显示-人性化的方式

​	更方便我们大家阅读

​	space键 就是向下翻页

​    b键-向上翻页

​	num 5 例子

less命令 一页一页的翻动显示

head命令- 取出文件的前几行

​	[root@10 day202408]# head -n 3 b.txt
​	北国风光，千里冰封，万里雪飘
​	江山如此多娇，引无数英雄竞折腰

tail命令 取出文件的后几行

​	[root@10 day202408]# tail -n 3 b.txt
​	7
​	8
​	9

~~~
[root@10 /]# mkdir day202408
[root@10 /]# cd day202408/
[root@10 day202408]# touch a.txt
[root@10 day202408]# touch 喜欢你.mp3
[root@10 day202408]# ls
a.txt  喜欢你.mp3
[root@10 day202408]# touch a1.txt 小红红.mp3
[root@10 day202408]# ls
a1.txt  a.txt  喜欢你.mp3  小红红.mp3
[root@10 day202408]# mkdir .test
[root@10 day202408]# ls
a1.txt  a.txt  喜欢你.mp3  小红红.mp3
[root@10 day202408]# ls -la
total 0
drwxr-xr-x.  3 root root  88 Aug 10 02:15 .
dr-xr-xr-x. 20 root root 261 Aug 10 02:10 ..
-rw-r--r--.  1 root root   0 Aug 10 02:12 a1.txt
-rw-r--r--.  1 root root   0 Aug 10 02:10 a.txt
drwxr-xr-x.  2 root root   6 Aug 10 02:15 .test
-rw-r--r--.  1 root root   0 Aug 10 02:10 喜欢你.mp3
-rw-r--r--.  1 root root   0 Aug 10 02:12 小红红.mp3
[root@10 day202408]# cd .test
[root@10 .test]# touch .a.txt
[root@10 .test]# ls
[root@10 .test]# ls -la
total 0
drwxr-xr-x. 2 root root 20 Aug 10 02:15 .
drwxr-xr-x. 3 root root 88 Aug 10 02:15 ..
-rw-r--r--. 1 root root  0 Aug 10 02:15 .a.txt
[root@10 .test]# clear
[root@10 .test]# ls
[root@10 .test]# 
[root@10 .test]# 
[root@10 .test]# cd ../
[root@10 day202408]# 
[root@10 day202408]# 
[root@10 day202408]# ls
a1.txt  a.txt  喜欢你.mp3  小红红.mp3
[root@10 day202408]# echo "helloworld">a.txt
[root@10 day202408]# cat a.txt
helloworld
[root@10 day202408]# 
[root@10 day202408]# 
[root@10 day202408]# echo "helloworld追加的方式写">>a.txt
[root@10 day202408]# cat a.txt
helloworld
helloworld追加的方式写
[root@10 day202408]# echo ">覆盖的方式写">a.txt
[root@10 day202408]# cat a.txt
>覆盖的方式写
[root@10 day202408]# echo ">>覆盖的方式写">>a.txt
[root@10 day202408]# cat a.txt
>覆盖的方式写
>>覆盖的方式写
[root@10 day202408]# clea
bash: clea: command not found...
[root@10 day202408]# clear
[root@10 day202408]# ls
a1.txt  a.txt  喜欢你.mp3  小红红.mp3
[root@10 day202408]# touch b.txt
[root@10 day202408]# ls
a1.txt  a.txt  b.txt  喜欢你.mp3  小红红.mp3
[root@10 day202408]# cat >b.txt<<EOF
> 北国风光，千里冰封，万里雪飘
> 江山如此多娇，引无数英雄竞折腰
> EOF
[root@10 day202408]# 
[root@10 day202408]# cat b.txt 
北国风光，千里冰封，万里雪飘
江山如此多娇，引无数英雄竞折腰
[root@10 day202408]# 
[root@10 day202408]# 
[root@10 day202408]# 
[root@10 day202408]# tac b.txt
江山如此多娇，引无数英雄竞折腰
北国风光，千里冰封，万里雪飘
[root@10 day202408]# nl b.txt
     1	北国风光，千里冰封，万里雪飘
     2	江山如此多娇，引无数英雄竞折腰
[root@10 day202408]# cat >b.txt<<EOF
北国风光，千里冰封，万里雪飘
江山如此多娇，引无数英雄竞折腰
EOF
[root@10 day202408]# cat >b.txt<<EOF
北国风光，千里冰封，万里雪飘
江山如此多娇，引无数英雄竞折腰
> 3
> 4
> 5
> 6
> 7
> 8
> 9
> EOF
[root@10 day202408]# more b.txt
北国风光，千里冰封，万里雪飘
江山如此多娇，引无数英雄竞折腰

3
4
5
6
7
8
9
[root@10 day202408]# more -3 b.txt
北国风光，千里冰封，万里雪飘
江山如此多娇，引无数英雄竞折腰

3
4
5
6
7
8
9

~~~



