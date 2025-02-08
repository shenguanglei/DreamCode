拿来主义：

。

### 一、更新系统

在安装Podman之前，建议首先更新您的CentOS 7系统到最新的软件包版本，以确保兼容性和安全性。可以使用以下命令来更新系统：

```bash
bash复制代码

sudo yum update
```

### 二、安装Podman

CentOS 7的官方仓库中可能不包含最新版本的Podman，但您可以通过启用额外的仓库或编译安装来获取较新版本的Podman。不过，对于大多数用户来说，通过官方仓库安装足够使用的版本是一个简单快捷的方法。

#### 使用官方仓库安装（版本可能较低）

1. **搜索Podman**（可选）：

   ```bash
   bash复制代码
   
   yum search podman
   ```

2. **安装Podman**：

   ```bash
   bash复制代码
   
   sudo yum -y install podman
   ```

   安装过程中，可能会自动安装一些依赖项，如`conmon`、`container-selinux`等。

#### 编译安装（获取更高版本）

如果您需要安装更高版本的Podman，可能需要从源代码编译安装。编译安装过程相对复杂，需要安装额外的依赖项，如Golang、Conmon、Runc等。以下是编译安装的大致步骤（以Podman 3.4.4为例，因为CentOS 7支持的最高版本可能受限）：

1. **安装依赖项**：

   ```bash
   sudo yum install -y gcc make glibc-devel glibc-headers libseccomp-devel \  
     device-mapper-devel btrfs-progs-devel libselinux-devel \  
     slirp4netns fuse-overlayfs
   ```

2. **安装Golang**（如果需要的话）：

   从Golang官网下载合适的版本并安装。

3. **安装Conmon和Runc**：

   这些通常作为Podman的依赖项一起编译或从官方仓库安装。

4. **下载Podman源代码**：

   从Podman的GitHub仓库下载源代码包。

5. **编译和安装Podman**：

   解压源代码包，配置编译选项，然后编译并安装。

### 三、验证安装

安装完成后，您可以通过运行以下命令来验证Podman是否成功安装：

```bash
bash复制代码

podman --version
```

如果看到Podman的版本信息，说明安装成功。

### 四、配置Podman（可选）

Podman支持多种配置选项，以满足不同的使用需求。您可以通过编辑配置文件（如`/etc/containers/storage.conf`）来配置存储驱动、网络设置等。

### 五、使用Podman

安装并配置好Podman后，您就可以开始使用它来管理容器了。Podman提供了丰富的命令来支持容器的生命周期管理，如拉取镜像、运行容器、停止容器等。

请注意，由于CentOS 7已经接近其生命周期的末尾，某些较新版本的软件可能不再支持在该系统上安装。因此，如果您需要更高版本的Podman或其他软件，可能需要考虑升级到更新的Linux发行版。



膜拜大佬：

https://blog.csdn.net/justlpf/article/details/129238001

~~~
Podman是Redhat公司推出的容器管理工具， Podman起初是 CRI-O的一部分，后来单独分离出来叫做 libpod，使用 Podman的命令几乎和 docker类似(我想这是 Redhat公司大力推举Podman替换Docker的同时又不是用户体验的诡计)，你可以通过alias docker=podman来替换Docker。
Podman在结构上与Docker不同，Podman没有使用daemon的方式去创建容器，而是直接调用OCI runtime，比如 runc， Podman由两部分组成， Podman CLI 和 conmon， Podman CLI方便用户交互，conmon负责container runtime，主要包括监控，日志，TTY分配等，简而言之，conmon是所有容器进程的父进程。
~~~

~~~
podman --help
##--------
可用命令:
  attach      连接到运行的容器
  build       使用Containerfiles中的说明构建image
  commit      基于更改的容器创建新image
  container   管理容器
  cp          在容器和本地文件系统之间复制文件/文件夹
  create      创建但不启动容器
  diff        检查容器文件系统上的更改
  events      显示podman事件
  exec        在正在运行的容器中运行进程
  export      将容器的文件系统内容导出为tar归档
  generate    生成的结构化数据
  healthcheck 管理健康检查
  help        关于任何命令的帮助
  history     显示指定image的历史记录
  image       管理图像
  images      列出本地存储中的images
  import      导入tarball以创建文件系统images
  info        显示podman系统信息
  init        初始化一个或多个容器
  inspect     显示容器或image的配置
  kill        使用特定信号杀死一个或多个正在运行的容器
  load        从容器存档加载image
  login       登录到容器注册表
  logout      注销容器注册表
  logs        获取容器的日志
  mount       装载工作容器的根文件系统
  network     管理网络
  pause       暂停一个或多个容器中的所有进程
  play        播放Podman
  pod         管理POD
  port        列出容器的端口映射或特定映射
  ps          列出容器
  pull        从注册表中提取image
  push        将image推送到指定的目标
  restart     重新启动一个或多个容器
  rm          移除一个或多个容器
  rmi         从本地存储中删除一个或多个图像
  run         在新容器中运行命令
  save        将image保存到存档
  search      在注册表中搜索image
  start       启动一个或多个容器
  stats       显示容器资源使用统计信息的实时流
  stop        停止一个或多个容器
  system      管理Podman
  tag         向本地image添加其他名称
  top         显示容器的运行进程
  umount      卸载工作容器的根文件系统
  unpause     取消暂停一个或多个容器中的进程
  unshare     在修改的用户命名空间中运行命令
  varlink     运行varlink接口
  version     显示Podman版本信息
  volume      管理卷
  wait        阻止一个或多个容器
 
标志:
      --cgroup-manager string     要使用的Cgroup管理器（cgroupfs或systemd）（默认为“systemd”）
      --cni-config-dir string     CNI网络配置目录路径
      --config string             详细说明容器服务器配置选项的libpod配置文件的路径
      --conmon string             conmon二进制文件的路径
      --cpu-profile string        cpu分析结果的路径
      --events-backend string     要使用的事件后端
      --help                      Podman帮助
      --hooks-dir strings         设置OCI挂钩目录路径（可以多次设置）
      --log-level string          高于指定级别的日志消息：调试、信息、警告、错误、致命或死机（默认为“错误”）
      --namespace string          设置libpod名称空间，用于在系统上创建容器和pod的单独视图
      --network-cmd-path string   用于配置网络的命令的路径
      --root string               存储数据（包括image）的根目录的路径
      --runroot string            存储所有状态信息的“运行目录”的路径
      --runtime string            用于运行容器的OCI兼容二进制文件的路径，默认为/usr/bin/runc
      --storage-driver string     选择用于管理image和容器存储的存储驱动程序（默认为覆盖）
      --storage-opt stringArray   用于将选项传递给存储驱动程序
      --syslog                    将日志记录信息输出到syslog和控制台
      --tmpdir string             tmp目录的路径
      --trace                     启用opentracing输出

~~~

## 卸载

1. *# 查询一个包是否被安装*
2. rpm -q podman
3.  
4. *# 卸载*
5. rpm -e podman
6. rm -rf /etc/containers

~~~

~~~

