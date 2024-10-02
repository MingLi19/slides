---

### why is redis so fast

<img class="w-80 opacity-50" border="rounded" src="./images/redis-fast.png" alt="why-redis-so-fast">

---

### 数据类型

Redis 主要支持以下几种数据类型：

- **string**（字符串）: 基本的数据存储单元，可以存储字符串、整数或者浮点数。
  hash（哈希）:一个键值对集合，可以存储多个字段。
  list（列表）:一个简单的列表，可以存储一系列的字符串元素。
  set（集合）:一个无序集合，可以存储不重复的字符串元素。
  zset(sorted set：有序集合): 类似于集合，但是每个元素都有一个分数（score）与之关联。
  位图（Bitmaps）：基于字符串类型，可以对每个位进行操作。
  超日志（HyperLogLogs）：用于基数统计，可以估算集合中的唯一元素数量。
  地理空间（Geospatial）：用于存储地理位置信息。
  发布/订阅（Pub/Sub）：一种消息通信模式，允许客户端订阅消息通道，并接收发布到该通道的消息。
  流（Streams）：用于消息队列和日志存储，支持消息的持久化和时间排序。
  模块（Modules）：Redis 支持动态加载模块，可以扩展 Redis 的功能。

---

### String 常用命令

SET key value：设置键的值。
GET key：获取键的值。
INCR key：将键的值加 1。
DECR key：将键的值减 1。
APPEND key value：将值追加到键的值之后。