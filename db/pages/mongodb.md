## 文档数据库

<br>

什么是文档数据库？
>文档数据库是一种数据库管理系统，它使用文档来存储和查询数据。文档数据库是一种NoSQL数据库，它使用文档来存储数据，而不是使用表格。文档数据库是一种非结构化数据库，它不需要固定的模式或结构。文档数据库是一种灵活的数据库，它可以存储任意类型的数据。

MongoDB官方对自己的类型定义是：
>MongoDB falls into the document database category, which is part of the more prominent NoSQL databases family. It stores information as structured or unstructured objects called documents. These documents are grouped in collections.

来源于[MongoDB官方](https://www.mongodb.com/resources/products/fundamentals/why-use-mongodb)

翻译过来就是：
>MongoDB属于文档数据库类别，是更大的NoSQL数据库家族的一部分。它将信息存储为称为文档的结构化或非结构化对象。这些文档被分组在集合中。

---

### 文档 - Document

MongoDB 中的记录是一个文档，它是由字段和值对组成的数据结构。MongoDB 文档类似于**JSON**对象(BSON)。字段值可以包含其他文档、数组和文档数组。
下面是一个 MongoDB 文档的例子：
```json
{
  "name" : "MongoDB",
  "type" : "NoSQL",
  "year" : 2009,
  "versions": [
    { "version": "8.0", "release_date": "2024-10-02" },
    { "version": "7.0", "release_date": "2023-08-15" }
  ]
  //...
}
```

使用文档的优点是：
- 文档(JSON)对应于软件开发中的对象，是微服务和前后端中交流的主要格式。
- 嵌入式文档和数组可以减少成本高昂的的连接操作。
- 动态Schema支持快速和多变的开发需求。

<!--
什么是Json? Json是一种轻量级的数据交换格式，易于阅读和编写。Json是基于JavaScript的一个子集。数据格式简单，易于读写，占用带宽小。Json格式是键值对的集合。数据在名称/值对中。数据由逗号分隔。大括号保存对象，中括号保存数组。
在软件开发中，一个对象或者类的实例经常是JSON对象的数据结构。例如这里的MongoDB文档就是一个JSON对象，它是一个键值对的集合。字段是name，year等，字段值可以包含其他文档、数组和文档数组。
在微服务架构中，服务之间的通信一般使用Json格式，因为Json格式的数据结构简单，易于解析，适合网络传输。
在前后端分离的开发中，前端和后端之间的数据交互也是使用Json格式。
MongoDB文档类似于关系数据库中的行，但有一个重要的区别，即文档可以包含嵌入式文档、数组和数组文档。这种灵活性使得MongoDB能够在一个文档中存储复杂的数据结构。
-->
---

### 术语和概念

|  SQL   | MongoDB    |
| --- | --- |
| 数据表（table） | 集合（collection） |
| 行（row） | 文档（document） |
| 列（column） | 字段（field） |
| 主键（primary key） | `_id` 字段 |
| 索引（index） | 索引（index） |
| 表连接 | 嵌入式文档 |
| 事务 | 事务（减少对多文档事务的需求） |

<!--
关系型网格Grid，一般由row、column组成table，而各个tables之间又存在一定的关系Relations。一个table的外键指向另一个table中的主键。
MongoDB中的数据模型是由文档和集合组成的，文档是一个键值对的集合。MongoDB中的文档可以包含其他文档，从而实现嵌套关系。
-->
---
layout: two-cols
layoutClass: gap-4
---

### 传统数据库的功能

<v-clicks depth="2">

- 强大的查询能力
  - 不亚于SQL语句的表达能力 - 各种操作符 & 聚合操作
  - 复杂的查询 - 文本搜索 & 地理空间查询
  - 索引
- ACID 事务
  - 原子性
  - 一致性
  - 隔离性
  - 持久性
- 企业级生态
  - 备份和恢复
  - 安全性
  - 审计
  - 字段加密

</v-clicks>

::right::

### NoSQL的附加能力

<v-clicks depth="2">

- 灵活数据结构
  - 单个集合中的文档不必具有相同的字段集
  - 字段的数据类型可能因集合中的文档而异
  - 为确保数据模型的一致性，可以创建模式验证规则
- 高可用性 Replica Set
  - 自动故障转移
  - 数据冗余
- 横向可扩展性 Sharding
- 支持多种存储引擎
  - WiredTiger
  - In-Memory (低延时)

</v-clicks>

<!--
由于大家对NoSQL数据库的认知，我们往往觉得NoSQL数据库只是为了解决特定的场景，比如Redis用于缓存，HBase用于大数据存储，Neo4j用于图数据库。但实际上，MongoDB是一个通用型的数据库，是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。
[click]
它具有传统数据库的所有功能，包括强大的查询语言，语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。
[click]
也提供高性能数据持久性。尤其是对嵌入式数据模型的支持减少了数据库系统上的 I/O 活动。索引支持更快的查询，并且可以包含嵌入式文档和数组的键。
[click]
提供各种企业级功能，包括备份和恢复，安全性，审计和字段加密。
[click]
MongoDB还提供了一些传统数据库不具备的功能，比如灵活的数据结构，高可用性，横向可扩展性，支持多种存储引擎。
[click]
灵活的数据结构，单个集合中的文档不必具有相同的字段集，字段的数据类型可能因集合中的文档而异。为确保数据模型的一致性，可以创建模式验证规则。
[click]
Replica Set是一组 MongoDB 服务器，它们维护相同的数据集，并可提供冗余和提高数据可用性。
[click]
支持基于分片键创建数据的区域。在均衡的集群中，MongoDB 仅将区域覆盖的读写定向到区域内的那些分片。
[click]
-->
---

## 安装

<br>

- 安装Mongodb Server

```bash
 docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```
- 安装Mongodb Client 命令行 mongosh
- 安装Mongodb Client GUI mongodb compass
- mongosh 数据库简单操作
  - `show dbs` 显示所有数据库
  - `use mydb` 切换到数据库
  - `db.createCollection("mycollection")` 创建集合
  - `db.mycollection.insertOne( { x: 1 } )` 插入文档
  - `db.mycollection.find()` 查询文档

<!--
Docker是一个开源的应用容器引擎，基于Go语言并遵从Apache2.0协议开源。Docker可以让开发者打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的Linux机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口。
我们的所有课程都是基于Docker容器化的，这样可以保证环境的一致性，方便学员在自己的电脑上进行实验。
MongoDB的安装也是通过Docker容器进行的，只需要一行命令就可以启动一个MongoDB容器，然后就可以使用mongosh命令行工具进行数据库操作。
-->
---
layout: two-cols
layoutClass: gap-4
---

<v-clicks depth="2">

- 创建集合
  - db.createCollection()
- 插入文档
  - db.collection.insertOne()
  - db.collection.insertMany()
- 更新文档
  - db.collection.updateOne()
  - db.collection.updateMany()
  - db.collection.replaceOne()
- 删除文档
  - db.collection.deleteOne()
  - db.collection.deleteMany()

</v-clicks>

::right::

<v-clicks depth="2">

- 查询文档
  - db.collection.find()
- 聚合操作
  - db.collection.aggregate()
- 创建索引
  - db.collection.createIndex()
- 删除索引
  - db.collection.dropIndex()
- 删除集合
  - db.collection.drop()

</v-clicks>
<!--
collection可以是任何名称，如果集合不存在，MongoDB会自动创建集合并插入文档。
-->
---

## 举个栗子🌰

<br>

下表列出了各种 SQL 语句和相应的 MongoDB 语句。该表中的示例假定以下条件：
- 这些 SQL 示例假设有一个名为 people 的表。
- MongoDB 示例假设一个名为 people 的集合包含以下原型的文档：
```json
{
  "_id" : ObjectId("507f191e810c19729de860ea"),
  "name" : "Alice",
  "age" : 25,
  "status" : "A"
}
```

---
layout: two-cols
layoutClass: gap-4
---

### SQL 创建和更改

<br>

```sql
CREATE TABLE people (
    id MEDIUMINT NOT NULL
        AUTO_INCREMENT,
    user_id Varchar(30),
    age Number,
    status char(1),
    PRIMARY KEY (id)
)

ALTER TABLE people
ADD join_date DATETIME

ALTER TABLE people
DROP COLUMN join_date

DROP TABLE people
```

::right::

### MongoDB 创建和更改

<br>

```javascript
// db.createCollection("people")
db.people.insertOne( {
    user_id: "abc123",
    age: 55,
    status: "A"
 } )
 

db.people.updateMany(
    {}, { $set: { join_date: new Date() } }
)

db.people.updateMany(
    {}, { $unset: { "join_date": "" } }
)

db.people.drop()
```

<!--
在第一个 insertOne() 或 insertMany() 操作上隐式创建。如果未指定 _id 字段，则会自动添加主键 _id。
集合并不描述或强制执行其文档的结构。`updateMany()`操作可以使用 $set 操作符将字段添加到现有文档中,也可以使用 $unset 操作符从文档中删除字段。
-->

---
layout: two-cols
layoutClass: gap-4
---

### SQL 插入语句
```sql
INSERT INTO people(user_id,
                  age,
                  status)
VALUES ("bcd001",
        45,
        "A")

CREATE INDEX idx_user_id_asc
ON people(user_id)

CREATE INDEX
       idx_user_id_asc_age_desc
ON people(user_id, age DESC)
```

::right::

### MongoDB insertOne语句

```javascript
db.people.insertOne( {
    user_id: "bcd001",
    age: 45,
    status: "A"
 } )

// 单个索引
db.people.createIndex( { user_id: 1 } )


// 复合索引
db.people.createIndex( { user_id: 1, age: -1 } )
```

---
layout: two-cols
layoutClass: gap-4
---

### SQL SELECT语句
```sql
SELECT * 
FROM people

SELECT id, user_id, status 
FROM people

SELECT *
FROM people
WHERE status = "A"

SELECT user_id, status
FROM people
WHERE status = "A"

SELECT *
FROM people
WHERE status = "A"
ORDER BY user_id ASC

SELECT COUNT(*)
FROM people
WHERE age > 30

SELECT *
FROM people
LIMIT 5
```

::right::

#### MongoDB find语句
```javascript
db.people.find()

db.people.find(
    {},
    { user_id: 1, status: 1 }
)

db.people.find(
    { status: "A" }
)

db.people.find(
    { status: "A" },
    { user_id: 1, status: 1 }
)

db.people.find( { status: "A" } )
  .sort( { user_id: 1 } )

db.people.find( { age: { $gt: 30 } } )
  .count()

db.people.find()
        .limit(5)
```

---
layout: two-cols
layoutClass: gap-4
---

### SQL 更新和删除语句

```sql
UPDATE people
SET status = "C"
WHERE age > 25

UPDATE people
SET age = age + 3
WHERE status = "A"

DELETE FROM people
WHERE status = "D"
```

::right::

### MongoDB updateMany() deleteMany() 语句

```javascript
db.people.updateMany(
   { age: { $gt: 25 } },
   { $set: { status: "C" } }
)

db.people.updateMany(
   { status: "A" } ,
   { $inc: { age: 3 } }
)

db.people.deleteMany( { status: "D" } )
```

---

### 建模
<br>

| 关系数据库 | 文档数据库 |
| -- | -- |
| 范式设计 | 数据的使用场景 |
| 在插入数据之前，您必须确定表格的模式 | 随着应用程序需求的变化，模式可能会随时间而变化|
| 经常需要确定多个不同表格的关联 | 避免多个集合之间的连接可以提高性能 |
| 事务是必需的，以确保数据的一致性 | 事务不是必需的，因为单个文档可以包含所有相关数据 |
| 为了提高性能，需要创建索引 | 创建索引以支持常见查询模式 |
| 分库分表 | 分片 |

<!--
- 关系数据库考虑范式设计，初衷就是为了减少数据冗余，提高数据的一致性。
- 关系数据库和文档数据库之间的一个重要区别是，关系数据库需要在插入数据之前确定表格的模式，而文档数据库不需要。这意味着，随着应用程序需求的变化，模式可能会随时间而变化。
- 文档数据库考虑数据的使用场景，数据的读写比例，数据的复杂度等。
-->
---

## 模式设计步骤

<br>
<v-clicks>

1. 确定工作负载: 确定您的应用程序最常运行的操作。
2. 映射关系: 确定应用程序数据中的关系，并决定是否链接或嵌入相关数据。
3. 应用设计模式: 应用模式设计模式来优化读取和写入。
4. 创建索引: 创建索引以支持常见查询模式。
</v-clicks>

<!--
[click]
确定工作负载: 用户为触发查询而采取的操作。查询类型（读取或写入）。由查询写入或返回的文档字段。您的应用程序运行查询的频率。经常运行的查询可从索引中获益，应对其进行优化以避免查找操作。该查询对于您的应用程序有多重要。
[click]
映射关系: 确定应用程序数据中的关系，并决定是否链接或嵌入相关数据。
[click]
应用设计模式: 应用模式设计模式来优化读取和写入。
[click]
创建索引: 创建索引以支持常见查询模式。
-->
---
layout: two-cols
layoutClass: gap-4
---

### 实体分析

假设我们有一个博客应用程序，用户可以发布文章并对文章进行评论。实体关系如下：
- 文章（Article）: 文章由标题、作者、正文和评论组成。
- 作者（Author）: 作者由名称、电子邮件和头像组成。
- 评论（Comment）: 评论由作者和评论文本组成。
- 标签（Tag）: 文章可以有多个标签。
- 类别（Category）: 文章可以属于多个类别。
- 阅读量（View）: 文章的阅读量。

::right::

<v-clicks>

<img class="w-100" border="rounded" src="../images/relationship.png">

传统关系型数据库设计: 五个表，每个表包含一个实体，使用外键关联。
- **优点**: 从数据出发，数据冗余少，数据一致性高。
- **缺点**: 没有考虑需求，查询性能低，需要多次连接操作。

</v-clicks>

<!--
- 在传统的关系数据库中，我们可能会将文章、作者和评论存储在不同的表中，并使用外键将它们关联起来。由于范式设计，我们可能会将作者信息, 评论信息，分类都存储在单独的表中，以避免数据冗余。
- 在范式的规定下，有意思的是不管谁来设计，除了命名和字段，结构都会差不多，因为范式设计是一种标准化的设计方法，是一种冗余最少的最佳实践。冗余最少也就意味着硬盘占用空间少，数据的一致性高。
- 但是这种设计方法有一个缺点，就是查询的时候需要进行多次连接操作，性能不高。
-->
---

### 确定工作负载

| 操作 | 类型 | 信息 | 频率 | 优先级 |
| --- | --- | --- | --- | --- |
| 提交新文章 | 写入 | 作者、文本 | 每天 10 次 | <span v-mark.circle.red="2"> 高 </span> |
| 提交对文章的评论 | 写入 | 用户，文本 | 每天 1,000 次 (10 每文章)| 中型 |
| 查看文章 | 读取 | 文章 ID、文本、评论 | <span v-mark.circle.red="2"> 每天 1,000,000 次 </span>  | <span v-mark.circle.red="2"> 高 </span> |
| 查看文章分析 | 读取 | 文章 ID、评论、点击 | 10 每小时 | 低 |

<v-clicks>

查询 vs 修改
- 操作的频率和优先级决定了我们应该如何设计数据库模式。
- 读取操作的频率比写入操作高，因此我们应该优化读取操作的性能。

如何优化查询性能？
- 将文章和评论存储在同一个文档中，这样可以在一个查询中检索文章和评论，而不必执行多个查询。

</v-clicks>
<!--
- 如何将对象分组到文档中，是由负载模式决定的。
- 提交新文章和查看文章都是高优先级。
- 查看文章的频率很高，所以我们应该优化读取操作的性能。
- 优化查询有可能会导致写入性能下降，但是影响可以接受。
-->
---

### 数据模式设计

我们可以使用以下模式(schema)来存储数据：
```json
{
  "_id" : ObjectId("507f191e810c19729de860ea"),
  "title" : "MongoDB",
  "author" : {
    "name": "alice123",
    "email": "alice@mycompany.com",
    "avatar": "photo1.jpg"
  },
  "body" : "NoSQL database bla bla bla...",
  "comments" : [
    {
      "author" : "Bob",
      "comment" : "Great article!"
    },
    {
      "author" : "Charlie",
      "comment" : "Thanks for sharing!"
    }
  ],
  "tags" : [
    "NoSQL",
    "Innovation"
  ],
  "category" : ["Technology", "Database"],
  "views" : 1000
}
```

---
layout: two-cols
layoutClass: gap-4
---

### 拆分数据

当然也不是所有的数据都应该存储在一个文档中。例如，我们可以将作者信息存储在单独的文档中：

```json
{
  "_id" : ObjectId("507f191e810c19729de860eb"),
  "name": "alice123",
  "email": "alice@mycompany.com",
  "avatar": "photo1.jpg"
}
```

::right::

```json
{
  "_id" : ObjectId("507f191e810c19729de860ea"),
  "title" : "MongoDB",
  "author" : ObjectId("507f191e810c19729de860eb"),
  "body" : "NoSQL database bla bla bla...",
  "comments" : [
    {
      "author" : "Bob",
      "comment" : "Great article!"
    },
    {
      "author" : "Charlie",
      "comment" : "Thanks for sharing!"
    }
  ],
  "tags" : [
    "NoSQL",
    "Innovation"
  ],
  "category" : ["Technology", "Database"],
  "views" : 1000
}
```

---

## 模式设计总结
<br>

<v-clicks depth="2">

- 负载分析
  - 确认数据容量
  - 确认操作量
  - 识别操作重要性
- 关系分析
  - 确认实体关系
  - 确认关系重要性
  - 嵌入 vs 引用
- 模式设计
  - Schema 演化

</v-clicks>

<!--
- 单个文件的大小限制为16MB，单个文档的字段数限制为100。如果一个文档的字段数超过100，可以考虑将文档拆分成多个文档。
- 考虑数据的完整性和一致性，如果数据之间有关联，可以考虑将数据存储在同一个文档中。便于查询和维护。
- 一起存储的数据应该是经常一起使用的数据。如果数据经常一起使用，那么将它们存储在一起可以减少查询时间。
- 考虑到内存占用，不频繁使用的数据应该存储在单独的文档中。
- Schema 演化: 随着应用程序需求的变化，模式可能会随时间而变化。可以通过添加新字段或者新文档来扩展模式。带来的优势是不需要修改现有的数据，不会影响现有的查询。数据库迁移不需要停机。
-->