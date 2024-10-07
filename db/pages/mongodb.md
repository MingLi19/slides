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

### MongoDB - 主要功能
- 高性能 & 灵活
- 查询 API
  - 读写操作(CRUD)
  - 数据聚合
  - 文本搜索 & 地理空间查询
- 高可用性 Replica Set
  - 自动故障转移
  - 数据冗余
- 横向可扩展性 Sharding
- 支持多种存储引擎
  - WiredTiger 
  - In-Memory 

<!--
MongoDB 提供高性能数据持久性。尤其是，对嵌入式数据模型的支持减少了数据库系统上的 I/O 活动。索引支持更快的查询，并且可以包含嵌入式文档和数组的键。
副本集是一组 MongoDB 服务器，它们维护相同的数据集，并可提供冗余和提高数据可用性。
从 3.4 开始，MongoDB 支持基于分片键创建数据的区域。在均衡的集群中，MongoDB 仅将区域覆盖的读写定向到区域内的那些分片。
-->
---

### MongoDB - 术语和概念

|     |     |
| --- | --- |
| 数据表（table） | 集合（collection） |
| 行（row） | 文档（document） |
| 列（column） | 字段（field） |
| 主键（primary key） | `_id` 字段 |
| 索引（index） | 索引（index） |
| 表连接 | 嵌入式文档 |
| 事务 | 事务（减少对多文档事务的需求） |
---

### MongoDB - 安装

- 安装Mongodb Server
```bash
 docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```
- 安装Mongodb Client 命令行 mongosh
- 数据库操作


---

### MongoDB - CRUD 操作
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
- 聚合操作
  - db.collection.aggregate()
</v-clicks>

---

### MongoDB - 举例

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

### SQL VS MongoDB DDL
<div grid="~ cols-2 gap-4">
<div>

#### SQL

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
</div>
<div>

#### MongoDB

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
</div>
</div>

<!--
在第一个 insertOne() 或 insertMany() 操作上隐式创建。如果未指定 _id 字段，则会自动添加主键 _id。
集合并不描述或强制执行其文档的结构。`updateMany()`操作可以使用 $set 操作符将字段添加到现有文档中,也可以使用 $unset 操作符从文档中删除字段。
-->

---

### SQL VS MongoDB 索引
<div grid="~ cols-2 gap-4">
<div>

#### SQL
单个索引
```sql
CREATE INDEX idx_user_id_asc
ON people(user_id)
```
复合索引
```sql
CREATE INDEX
       idx_user_id_asc_age_desc
ON people(user_id, age DESC)
```
</div>
<div>

#### MongoDB
单个索引
```javascript
db.people.createIndex( { user_id: 1 } )
```
复合索引
```javascript
db.people.createIndex( { user_id: 1, age: -1 } )
```
</div>
</div>
---

### SQL VS MongoDB Insert

<div grid="~ cols-2 gap-4">
<div>

#### SQL 插入语句
```sql
INSERT INTO people(user_id,
                  age,
                  status)
VALUES ("bcd001",
        45,
        "A")
```
</div>
<div>

#### MongoDB insertOne语句
```javascript
db.people.insertOne( {
    user_id: "bcd001",
    age: 45,
    status: "A"
 } )
```
</div>
</div>

---

### SQL VS MongoDB Select
<div grid="~ cols-2 gap-4">
<div>

#### SQL SELECT语句
```sql
SELECT *
FROM people

SELECT id,
       user_id,
       status
FROM people

SELECT user_id, status
FROM people

SELECT *
FROM people
WHERE status = "A"

SELECT user_id, status
FROM people
WHERE status = "A"
```
</div>

<div>

#### MongoDB find语句
```javascript
db.people.find()

db.people.find(
    {},
    { user_id: 1, status: 1 }
)

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
```
</div>
</div>
