## 定义

队列（queue）是一种遵循先入先出规则的线性数据结构。顾名思义，队列模拟了排队现象，即新来的人不断加入队列尾部，而位于队列头部的人逐个离开。

如图所示，我们将队列头部称为“队首”，尾部称为“队尾”，将把元素加入队尾的操作称为“入队”，删除队首元素的操作称为“出队”。

<img class="w-100" border="rounded" src="../images/queue.png">

----

## 常用操作

| 方法 | 描述 | 时间复杂度 |
| --- | --- | --- |
| push() | 元素入队，即将元素添加至队尾 | O(1) |
| pop() | 队首元素出队 | O(1) |
| peek() | 访问队首元素 | O(1) |
| size() | 获取队列的长度 | O(1) |
| is_empty() | 判断队列是否为空 | O(1) |

---

## Python 官方实现

```py
from collections import deque

# 初始化队列
# 在 Python 中，我们一般将双向队列类 deque 当作队列使用
# 虽然 queue.Queue() 是纯正的队列类，但不太好用，因此不推荐
que: deque[int] = deque()

# 元素入队
que.append(1)
que.append(3)
que.append(2)

# 访问队首元素
front: int = que[0]

# 元素出队
pop: int = que.popleft()

# 获取队列的长度
size: int = len(que)

# 判断队列是否为空
is_empty: bool = len(que) == 0
```

---

## 链表实现 - 基于数组