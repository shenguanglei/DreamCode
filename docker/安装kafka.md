以下是一套完整的命令，用于通过 Docker 和 Docker Compose 安装并运行 Kafka。这些命令包括创建 `docker-compose.yml` 文件、启动 Kafka 和 Zookeeper、验证安装以及停止服务。

------

### 1. 创建项目目录并进入

bash

复制

```
mkdir kafka-docker && cd kafka-docker
```

------

### 2. 创建 `docker-compose.yml` 文件

bash

复制

```
cat <<EOF > docker-compose.yml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
EOF
```

------

### 3. 启动 Kafka 和 Zookeeper

bash

复制

```
docker-compose up -d
```

------

### 4. 验证 Kafka 是否正常运行

#### 进入 Kafka 容器

bash

复制

```
docker exec -it kafka-docker_kafka_1 bash
```

#### 创建一个测试主题

bash

复制

```
kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

#### 发送消息到主题

bash

复制

```
kafka-console-producer --topic test-topic --bootstrap-server localhost:9092
```

（输入一些消息，然后按 `Ctrl+C` 退出）

#### 消费消息

bash

复制

```
kafka-console-consumer --topic test-topic --bootstrap-server localhost:9092 --from-beginning
```

（你应该能看到之前发送的消息）

------

### 5. 停止 Kafka 和 Zookeeper

bash

复制

```
docker-compose down
```

------

### 6. 清理 Docker 资源（可选）

如果你想彻底清理 Docker 资源（包括容器、网络和未使用的镜像），可以运行以下命令：

bash

复制

```
docker system prune -f
```

------

### 总结

- **`docker-compose up -d`**：启动 Kafka 和 Zookeeper。
- **`docker exec`**：进入 Kafka 容器并运行 Kafka 命令行工具。
- **`docker-compose down`**：停止并删除 Kafka 和 Zookeeper 容器。