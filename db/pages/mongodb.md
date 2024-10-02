
## MongoDB - 文档数据库

MongoDB 中的记录是一个文档，它是由字段和值对组成的数据结构。MongoDB 文档类似于**JSON**对象(BSON)。字段值可以包含其他文档、数组和文档数组。
下面是一个 MongoDB 文档的例子：
```json
{
  "name" : "MongoDB",
  "type" : "NoSQL",
  "year" : 2009,
  "versions": ["v1.0", "v2.0", "v3.0"]
}
```

使用文档的优点是：
- 文档对应于许多编程语言中的原生数据类型。
- 嵌入式文档和数组可以减少成本高昂的的连接操作。
- 动态模式支持流畅的多态性。

---

## MongoDB - 主要功能
- 高性能
- 查询 API
  - 读写操作(CRUD)
  - 数据聚合
  - 文本搜索 & 地理空间查询
- 高可用性 Replica Set
  - 自动故障转移
  - 数据冗余
- 横向可扩展性 Sharding
- 支持多种存储引擎
MongoDB 支持多种存储引擎：
  - WiredTiger 
  - In-Memory 

<!--
MongoDB 提供高性能数据持久性。尤其是，对嵌入式数据模型的支持减少了数据库系统上的 I/O 活动。索引支持更快的查询，并且可以包含嵌入式文档和数组的键。
副本集是一组 MongoDB 服务器，它们维护相同的数据集，并可提供冗余和提高数据可用性。
从 3.4 开始，MongoDB 支持基于分片键创建数据的区域。在均衡的集群中，MongoDB 仅将区域覆盖的读写定向到区域内的那些分片。
-->
---

## MongoDB - 安装

- 安装Mongodb Server
```bash
 docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```
- 安装Mongodb Client 命令行 mongosh
- 数据库操作


---

## MongoDB - CRUD 操作
<v-clicks depth="2">

- 插入文档
  - db.collection.insertOne()
  - db.collection.insertMany()
- 查询文档
  - db.collection.find()
- 更新文档
  - db.collection.updateOne()
  - db.collection.updateMany()
  - db.collection.replaceOne()
- 删除文档
  - db.collection.deleteOne()
  - db.collection.deleteMany()

</v-clicks>

---
layout: image
image: https://media.giphy.com/media/13GIgrGdslD9oQ/giphy.gif
---

### Coding Time

<style>
h3 {
  color: white !important;
  @apply !text-shadow-lg;
  @apply !text-center;
  @apply !text-8xl
}
</style>

---

## 优势
- 高灵活性 Flexable Schema
- 高可靠 (Reliability)
- 高性能 (Scalability) 
