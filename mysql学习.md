### 1、描述一下数据库事务的隔离级别

ACID:

原子性：undo log (MVCC)

一致性：最核心和最本质的要求

隔离性：锁，MVCC (多版本并发控制)

持久性：redo log

数据库的事务级别有四种，分别是读未提交、读已提交、可重复读 、序列化、不同的隔离级别下会产生脏读、幻读、不可重复读等相关问题。因此，在选择隔离级别的时候，要根据应用场景来决定使用合适的隔离级别。

各种隔离级别和数据库异常情况对应情况如下。

### 2、MVCC的实现原理

### 3、mysql幻读怎么解决

### 4、sql join 原理

### 5、说明一下数据库索引原理、底层索引数据结构，叶子节点存储的是什么，索引失效的情况

### 6 、mysql 如何做分库分表的？

### 7、数据存储引擎有哪些

### 8、描述一下InnoDB和MYISAM的区别

### 9描述一下聚簇索引和非聚簇索引的区别

### 10、事务有哪些隔离级别，分别解决了什么问题

### 11、描述一下mysql主从复制的机制的原理？mqsql主从复制主要有几种模式？

### 12、如何优化sql,查询计划的结果中看那些关键数据

###  13、MYSQL 为什么选择B+书作为它的存储结构，为什么不选择Hash,二叉、红黑树？

### 14、描述一下mysql的乐观锁和悲观锁，锁的种类

###  15、mysql原子性和持久性是怎么保证的？







