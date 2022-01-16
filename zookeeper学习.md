zookeeper 安装

### CfG说明

~~~
# The number of milliseconds of each tick
tickTime=2000 （服务心跳2s）
# The number of ticks that the initial
# synchronization phase can take
initLimit=10  (lender允许follow 2s*10  的延时)
# The number of ticks that can pass between
# sending a request and getting an acknowledgement
syncLimit=5 （数据操作10秒未维护的）
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just
# example sakes.
dataDir=/var/shengl/zk  (快照myid)
# the port at which the clients will connect
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the
# administrator guide before turning on autopurge.
#
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1

## Metrics Providers
#
# https://prometheus.io Metrics Exporter
#metricsProvider.className=org.apache.zookeeper.metrics.prometheus.PrometheusMetricsProvider
#metricsProvider.httpPort=7000
#metricsProvider.exportJvmInfo=tru
~~~

