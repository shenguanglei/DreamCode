# Docker 学习路线图

## 一、基础入门（1 - 2 周）

### （一）理论知识

#### 1. 容器技术背景与概念



- 了解传统虚拟化技术（如 VMware）的局限性，明白容器技术诞生的背景和解决的问题。
- 掌握容器的基本概念，对比容器与虚拟机在资源利用、启动速度、隔离性等方面的差异。

#### 2. Docker 简介



- 了解 Docker 的发展历程、社区生态以及在企业中的应用场景，如持续集成 / 持续部署（CI/CD）、微服务架构等。
- 熟悉 Docker 的核心组件，包括镜像（Image）、容器（Container）、仓库（Registry）的定义和作用。

### （二）环境搭建

#### 1. 选择操作系统



- 对于初学者，推荐使用 Linux 系统，如 Ubuntu 或 CentOS，因为 Docker 原生支持 Linux 内核特性。也可以在 Windows 或 macOS 上通过 Docker Desktop 进行学习。

#### 2. 安装 Docker



- 按照官方文档的指引，在所选操作系统上完成 Docker 引擎的安装。
- 验证 Docker 是否安装成功，通过运行 `docker version` 命令查看 Docker 客户端和服务端的版本信息。

### （三）基础操作实践

#### 1. 镜像操作



- 使用 `docker search` 命令搜索 Docker Hub 上的公共镜像。
- 运用 `docker pull` 命令拉取所需镜像，如 `docker pull nginx`。
- 利用 `docker images` 命令查看本地已有的镜像列表。
- 学习 `docker rmi` 命令删除不需要的本地镜像。

#### 2. 容器操作



- 使用 `docker run` 命令创建并启动一个新容器，例如 `docker run -it ubuntu bash` 进入 Ubuntu 容器的交互式终端。
- 掌握 `docker ps` 命令查看正在运行的容器，使用 `docker ps -a` 查看所有容器（包括已停止的）。
- 学会使用 `docker start`、`docker stop`、`docker restart` 命令对容器进行启动、停止和重启操作。
- 运用 `docker rm` 命令删除已停止的容器。

## 二、中级进阶（2 - 4 周）

### （一）镜像深入学习

#### 1. Dockerfile 编写



- 学习 Dockerfile 的基本语法，包括 `FROM`、`RUN`、`COPY`、`ADD`、`CMD`、`ENTRYPOINT` 等指令的使用。
- 实践编写简单的 Dockerfile 来构建自定义镜像，例如构建一个包含 Python 环境和简单 Flask 应用的镜像。
- 理解 Docker 镜像的分层结构，以及如何通过优化 Dockerfile 减少镜像层数，从而减小镜像体积。

#### 2. 镜像构建与发布



- 使用 `docker build` 命令根据 Dockerfile 构建自定义镜像，掌握 `-t` 标签参数的使用来为镜像命名和打标签。
- 学习将本地构建的镜像推送到 Docker Hub 或其他私有镜像仓库，使用 `docker login` 登录仓库，`docker push` 推送镜像。

### （二）容器数据管理

#### 1. 数据卷（Volumes）



- 了解数据卷的概念和作用，它用于在容器和宿主机之间或多个容器之间共享数据。
- 学习使用 `docker volume create` 创建数据卷，`docker run -v` 命令将数据卷挂载到容器中。

#### 2. 绑定挂载（Bind Mounts）



- 掌握绑定挂载的使用方法，它允许将宿主机上的文件或目录直接挂载到容器中。
- 对比数据卷和绑定挂载的优缺点，根据不同场景选择合适的数据管理方式。

### （三）容器网络

#### 1. Docker 网络基础



- 了解 Docker 默认的网络模式，如桥接网络（bridge）、主机网络（host）、无网络（none）等。
- 学习使用 `docker network ls` 命令查看 Docker 网络列表，`docker network create` 命令创建自定义网络。

#### 2. 容器间通信



- 实践在不同网络模式下容器之间的通信，例如在桥接网络中通过容器名进行通信。
- 掌握端口映射的原理和使用方法，使用 `-p` 参数将容器内的端口映射到宿主机的端口，使容器内的服务可以被外部访问。

### （四）Docker Compose

#### 1. 概念与安装



- 理解 Docker Compose 的作用，它用于定义和运行多容器的 Docker 应用。
- 按照官方文档安装 Docker Compose。

#### 2. Compose 文件编写



- 学习 Docker Compose 文件（通常为 `docker-compose.yml`）的语法结构，包括服务（services）、网络（networks）、卷（volumes）等部分的配置。
- 实践编写一个包含多个服务的 Compose 文件，例如一个包含 Web 服务和数据库服务的应用。

#### 3. Compose 命令使用



- 掌握 `docker-compose up` 命令启动所有服务，`docker-compose down` 命令停止并删除所有服务。
- 学习使用 `docker-compose ps` 查看服务状态，`docker-compose logs` 查看服务日志。

## 三、高级应用（3 - 6 周）

### （一）Kubernetes 基础（可选）

#### 1. 容器编排概念



- 了解容器编排的需求和作用，明白为什么需要像 Kubernetes 这样的容器编排工具。
- 对比 Kubernetes 与 Docker Swarm 等其他容器编排工具的特点。

#### 2. Kubernetes 架构与组件



- 学习 Kubernetes 的核心架构，包括控制平面组件（如 API Server、Controller Manager、Scheduler 等）和工作节点组件（如 Kubelet、Kube - Proxy 等）。
- 理解 Pod、Deployment、Service 等 Kubernetes 资源对象的概念和作用。

#### 3. 本地环境搭建与实践



- 使用 Minikube 或 Kind 在本地搭建一个单节点的 Kubernetes 集群。
- 实践在 Kubernetes 集群中部署和管理 Docker 容器应用，如创建 Deployment 部署应用，创建 Service 暴露应用服务。

### （二）安全与监控

#### 1. Docker 安全



- 了解 Docker 安全的主要方面，包括容器隔离、镜像安全、访问控制等。
- 学习使用 Docker 安全扫描工具（如 Trivy）对镜像进行安全漏洞扫描。
- 掌握 Docker 容器的安全配置，如限制容器的资源使用、使用安全的用户权限等。

#### 2. 监控与日志管理



- 了解 Docker 容器的监控指标，如 CPU 使用率、内存使用率、网络流量等。
- 学习使用 Prometheus 和 Grafana 搭建 Docker 容器的监控系统，收集和可视化容器的监控数据。
- 掌握使用 ELK Stack（Elasticsearch、Logstash、Kibana）或 Fluentd 进行 Docker 容器的日志收集、存储和分析。

### （三）CI/CD 集成

#### 1. 持续集成概念



- 理解持续集成的定义和重要性，以及它在软件开发流程中的作用。

#### 2. 使用 Jenkins 或 GitLab CI/CD



- 学习使用 Jenkins 或 GitLab CI/CD 搭建持续集成 / 持续部署（CI/CD）流水线。
- 实践在 CI/CD 流水线中实现 Docker 镜像的构建、测试和部署，例如在代码提交后自动构建 Docker 镜像并推送到镜像仓库，然后部署到测试或生产环境。

## 四、实战项目与总结（1 - 2 周）

### （一）实战项目

#### 1. 微服务架构应用



- 构建一个简单的微服务架构应用，包含多个服务（如用户服务、订单服务、商品服务等）。
- 使用 Docker 容器化每个微服务，并使用 Docker Compose 或 Kubernetes 进行部署和管理。
- 实现微服务之间的通信和协调，如使用 API 网关、服务发现等机制。

#### 2. 复杂 Web 应用部署



- 部署一个复杂的 Web 应用，包括前端、后端、数据库等多个组件。
- 优化应用的性能和可靠性，如使用负载均衡、缓存等技术。

### （二）总结与拓展

#### 1. 知识总结



- 回顾学习过程中的重点知识和技能，总结经验和教训。
- 整理学习笔记和项目代码，形成自己的知识体系。

#### 2. 拓展学习



- 深入学习 Docker 的高级特性和技术，如 Docker Swarm、容器存储编排等。
- 关注 Docker 社区和行业动态，了解最新的技术发展和应用案例。