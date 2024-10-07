### 什么是图数据库（graph database）
​ 随着社交、电商、金融、零售、物联网等行业的快速发展，现实社会织起了了一张庞大而复杂的关系网，传统数据库很难处理关系运算。大数据行业需要处理的数据之间的关系随数据量呈几何级数增长，急需一种支持海量复杂数据关系运算的数据库，图数据库应运而生。

​ 世界上很多著名的公司都在使用图数据库，比如：
- **社交领域**：Facebook, Twitter, Linkedin用它来管理社交关系，实现好友推荐
- **零售领域**：eBay，沃尔玛使用它实现商品实时推荐，给买家更好的购物体验
- **金融领域**：摩根大通，花旗和瑞银等银行在用图数据库做风控处理
- **汽车制造领域**：沃尔沃，戴姆勒和丰田等顶级汽车制造商依靠图数据库推动创新制造解决方案
- **电信领域**：Verizon, Orange和AT&T 等电信公司依靠图数据库来管理网络，控制访问并支持客户360
- **酒店领域**：万豪和雅高酒店等顶级酒店公司依使用图数据库来管理复杂且快速变化的库存

图数据库是基于图论实现的一种NoSQL数据库，其数据存储结构和数据查询方式都是以图论为基础的，图数据库主要用于存储更多的连接数据。

>图论 ( Graph Theory ) 是数学的一个分支。它以图为研究对象图论中的图是由若干给定的点及连接两点的线所构成的图形，这种图形通常用来描述某些事物之间的某种特定关系，用点代表事物，用连接两点的线表示相应两个事物间具有这种关系。

---

## Neo4j - 基础

Neo4j是世界领先的图数据库。它是一个高性能的图形存储，具备成熟且稳健的数据库所需的所有功能，例如友好的查询语言和ACID事务。程序员可以使用灵活的节点和关系网络结构进行开发，而不是静态的表格——但仍然享有企业级数据库的所有优势。对于许多应用程序，Neo4j相比关系型数据库提供了数量级的性能提升。

---

### Neo4j - 数据模型

Neo4j的数据模型是一个图，由节点和关系组成。节点是图的基本单位，用于表示实体。关系用于表示节点之间的连接。节点和关系都可以有属性。

- **节点（Node）**：节点是图中的基本单位，用于表示实体。

- **关系（Relationship）**：关系用于表示节点之间的连接。关系总是从一个节点指向另一个节点，有一个方向。

- **属性（Property）**：属性是节点和关系的特征。属性是键值对，键是属性的名称，值是属性的值。属性的值可以是任何数据类型，如字符串、整数、浮点数、布尔值、日期等。

- **标签（Label）**：标签是节点的类型。标签用于表示节点的类型。节点可以有零个或多个标签。标签是一个字符串，用于表示节点的类型。

<img class="w-100" src="../images/neo4j_basic.png">

---

### 对比关系型数据库

|  关系型数据库（RDBMS）   |  图数据库   |
| --- | --- |
| 表 | 图 |
| 行 | 节点 |
| 列和数据 | 属性和关系 |
| 约束 | 关系 |

---

### Neo4j - 性能测试
<br>

> 为了测试Neo4j的性能，我们将使用一个简单的查询，该查询将返回一个用户的所有朋友的朋友的朋友的朋友的朋友。我们将测试这个查询的深度，从2到5。我们将在一个包含1000个用户的数据库上运行这个查询。我们在MySQL和Neo4j中构建了这个查询，并且结果是惊人的。执行时间以秒为单位，对于1000个用户。

|  深度   |  MySQL 计算时间   | Neo4j 计算时间 |
| --- | --- | --- |
| 2 | 0.016 | 0.010 |
| 3 | 30.267 | 0.168 |
| 4 | 1,543.505 | 1.359 |
| 5 | Not Finished in 1 Hour | 2.132 |

来源：[图数据库到底有多快](https://neo4j.com/news/how-much-faster-is-a-graph-database-really/)

---

### Neo4j - 安装

- 安装Neo4j Server
```bash
docker run --name neo4j -p 7474:7474 -p 7687:7687 -d neo4j
```
- 安装Neo4j Client Neo4j Desktop
- 建立数据库

---

### Neo4j - CRUD 操作

- 创建节点

```cypher
CREATE (n1:Person {name: 'Tom Hanks', born: 1956})
CREATE (n2:Person {name: 'Tom Cruise', born: 1962})
CREATE (m1:Movie {title: 'Top Gun', released: 1986})
CREATE (m2:Movie {title: 'Forrest Gump', released: 1994})
```

- 创建关系
```cypher
MATCH (a:Person), (m:Movie) WHERE a.name = 'Tom Cruise' AND m.title = 'Top Gun' CREATE (a)-[r:ACTED_IN]->(m) RETURN r
MATCH (a:Person), (m:Movie) WHERE a.name = 'Tom Hanks' AND m.title = 'Forrest Gump' CREATE (a)-[r:ACTED_IN]->(m) RETURN r
MATCH (a:Person), (b:Person) WHERE a.name = 'Tom Cruise' AND b.name = 'Tom Hanks' CREATE (a)-[r:KNOWS]->(b) RETURN r
```

- 查询节点
```cypher
MATCH (n:Person) WHERE n.name = 'Tom Hanks' RETURN n
```

- 更新节点
```cypher
MATCH (n:Person) WHERE n.name = 'Tom Hanks' SET n.born = 1957
```

- 删除节点
```cypher
MATCH (n:Person) WHERE n.name = 'Tom Hanks' DELETE n
```

<!--
CREATE是创建操作，Person是标签，代表节点的类型。花括号{}代表节点的属性，属性类似Python的字典。这条语句的含义就是创建一个标签为Person的节点，该节点具有一个name属性，属性值是John。
MATCH是查询操作，Person是标签，代表节点的类型。WHERE是过滤条件，n.name = 'John'是过滤条件，表示查询name属性值为John的节点。RETURN是返回操作，表示返回查询结果。
SET是更新操作，n.age = 30是更新操作，表示将age属性值更新为30。
DELETE是删除操作，表示删除查询到的节点。
-->
