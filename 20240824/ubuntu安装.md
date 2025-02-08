一、安装包下载
1、从官网下载，网址如下：
官网：https://cn.ubuntu.com/download/desktop



2、清华镜像源（速度较快）
网址：https://mirrors.tuna.tsinghua.edu.cn/



二、安装过程
1、打开VM虚拟机，点击创建新的虚拟机，如下图所示：


2、选择自定义


3、根据虚拟机和Ubuntu系统的版本来选择


4、选择下面红框中的选项


5、操作系统选择Linux，版本选择Ubuntu64位


6、虚拟机的名称和位置都可以选择更改


7、处理器数量及处理器内核数量根据自己电脑的实力来选


8、这里内存选择两个G


9、这里选择第二个，如有需要，后面安装完成后，可在设置中更改


10、选择推荐的






11、磁盘大小根据自身需求选择


12、这一步默认选择


13、选择自定义硬件


14、选择第一步下载的映像文件，然后选择关闭，点击完成。




15、点击开启虚拟机，进行安装
















填写相关信息，并设置登录密码



16、安装完成后，重启即可

~~~
# 指定SSH服务的端口号，默认是22  
Port 22  
  
# 指定SSH服务监听的网络协议族，any表示同时监听IPv4和IPv6  
AddressFamily any  
  
# 指定SSH服务监听的IPv4地址，0.0.0.0表示监听所有IPv4地址  
ListenAddress 0.0.0.0  
  
# 指定SSH服务监听的IPv6地址，::表示监听所有IPv6地址  
# 如果不需要IPv6，可以注释掉这一行  
ListenAddress ::  
  
# 指定SSH主机密钥文件的位置  
HostKey /etc/ssh/ssh_host_rsa_key  
HostKey /etc/ssh/ssh_host_ecdsa_key  
HostKey /etc/ssh/ssh_host_ed25519_key  
  
# 指定SSH服务器支持的加密算法和密钥交换算法  
# 为了保证安全性，建议使用较新的算法，如aes256-gcm  
Ciphers aes256-gcm,aes128-cbc,3des-cbc  
KexAlgorithms curve25519-sha256,diffie-hellman-group14-sha256,diffie-hellman-group14-sha1  
  
# 指定在多少分钟后，如果没有数据传输，SSH服务器将自动重新生成密钥  
# 这有助于防止某些类型的攻击  
RekeyLimit default none  
  
# 其他安全性相关的配置  
# 禁止root用户直接登录  
PermitRootLogin no  
  
# 禁止密码认证，只允许密钥认证  
PasswordAuthentication no  
  
# 禁止空密码  
PermitEmptyPasswords no  
  
# 使用更安全的认证方法  
ChallengeResponseAuthentication no  
  
# 指定是否允许TCP转发  
AllowTcpForwarding yes  
  
# 指定是否允许X11转发  
X11Forwarding yes  
  
# 打印最后的登录信息  
PrintLastLog yes  
  
# 指定日志级别  
LogLevel INFO  
  
# 指定登录尝试的最大次数  
MaxAuthTries 6  
  
# 指定是否允许用户通过SSH隧道使用pty  
UsePAM yes
~~~

从您提供的`systemd`状态输出来看，SSH服务（`ssh.service`）未能启动，并且`ExecStartPre`阶段的`/usr/sbin/sshd -t`命令以状态码255退出，这通常表示有错误发生。`-t`选项是用于测试配置文件的语法是否正确。

要解决这个问题，请按照以下步骤操作：

1. **检查SSH配置文件**：
   打开`/etc/ssh/sshd_config`文件，并仔细检查是否有语法错误，比如不匹配的括号、缺少的关键字或者不正确的参数值。
2. **手动测试配置文件**：
   在命令行中运行`/usr/sbin/sshd -t`来手动测试配置文件的语法。如果输出显示有错误，请根据提示进行修正。
3. **查看系统日志**：
   查看`/var/log/auth.log`（Ubuntu系统）或相应的系统日志文件，以获取更多关于SSH服务启动失败的信息。
4. **重新启动SSH服务**：
   修正配置文件后，尝试重新启动SSH服务：`sudo systemctl restart ssh.service`。
5. **检查防火墙设置**：
   确保防火墙设置没有阻止SSH端口（默认是22）。
6. **检查SELinux状态**：
   如果您的系统上启用了SELinux，请确保SELinux的策略没有阻止SSH服务。
7. **回滚更改**：
   如果您最近对配置文件进行了更改，并且不确定哪些更改可能导致了问题，请尝试回滚这些更改。

按照这些步骤操作后，您应该能够诊断并解决SSH服务启动失败的问题。如果问题仍然存在，请考虑寻求更专业的帮助或联系系统管理员。

