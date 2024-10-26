## 链表

链表（linked list）是一种线性数据结构，其中的每个元素都是一个节点对象，各个节点通过“引用”相连接。引用记录了下一个节点的内存地址，通过它可以从当前节点访问到下一个节点。

链表的设计使得各个节点可以分散存储在内存各处，它们的内存地址无须连续。

<img class="w-100" border="rounded" src="../images/linkedlist.png">

内存空间是所有程序的公共资源，在一个复杂的系统运行环境下，空闲的内存空间可能散落在内存各处。我们知道，存储数组的内存空间必须是连续的，而当数组非常大时，内存可能无法提供如此大的连续空间。此时链表的灵活性优势就体现出来了。

<!--
链表的组成单位是节点（node）对象。每个节点都包含两项数据：节点的“值”和指向下一节点的“引用”。
链表的首个节点被称为“头节点”，最后一个节点被称为“尾节点”。
尾节点指向的是“空”，在 Python 中被记为 None 。
-->
---

## 链表节点 ListNode

链表节点 ListNode 除了包含值，还需额外保存一个引用（指针）。因此在相同数据量下，链表比数组占用更多的内存空间。

```py {all|1|3-5}
class ListNode:
    """链表节点类"""
    def __init__(self, val: int):
        self.val: int = val               # 节点值
        self.next: ListNode | None = None # 指向下一节点的引用     
```

---

## 链表的初始化

建立链表分为两步，第一步是初始化各个节点对象，第二步是构建节点之间的引用关系。初始化完成后，我们就可以从链表的头节点出发，通过引用指向 next 依次访问所有节点。
    
```py {1|2-6|7-10}
# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
# 1. 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 2. 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
```

----

在链表中插入节点非常容易。如图 4-6 所示，假设我们想在相邻的两个节点 n0 和 n1 之间插入一个新节点 P ，则只需改变两个节点引用（指针）即可，时间复杂度为 O(1)。

<img class="w-100" border="rounded" src="../images/linkedlist_insert.png">

相比之下，在数组中插入元素的时间复杂度为 O(n)，在大数据量下的效率较低。


```py
def insert(n0: ListNode, P: ListNode):
    """在链表的节点 n0 之后插入节点 P"""
    n1 = n0.next
    P.next = n1
    n0.next = P
```

---

在链表中删除节点也非常方便，只需改变一个节点的引用（指针）即可。

<img class="w-100" border="rounded" src="../images/linkedlist_delete.png">

```py
def remove(n0: ListNode):
    """删除链表的节点 n0 之后的首个节点"""
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1
```

<!--
请注意，尽管在删除操作完成后节点 P 仍然指向 n1 ，但实际上遍历此链表已经无法访问到 P ，这意味着 P 已经不再属于该链表了。
-->
---

## 链表的遍历

链表的遍历是指从链表的头节点出发，通过引用指向 next 依次访问所有节点。遍历链表的时间复杂度为 O(n)。

```py
def traverse(head: ListNode):
    """遍历链表"""
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
```

---

## 链表 vs 数组

链表和数组是两种最基本的数据结构，它们各有优势和劣势。链表的优势在于插入和删除操作的时间复杂度为 O(1)，而数组的优势在于随机访问的时间复杂度为 O(1)。

| 对比 | 数组 | 链表
| --- | --- | --- |
|存储方式 | 连续内存空间 | 分散内存空间|
|容量扩展 | 长度不可变 | 可灵活扩展|
|内存效率 | 元素占用内存少、但可能浪费空间 | 元素占用内存多|
|访问元素 | O(1) | O(n)|
|添加元素 | O(n) | O(1)|
|删除元素 | O(n) | O(1)|

---

<img class="w-100" border="rounded" src="https://labuladong.online/algo/images/linked-list-two-pointer/1.gif">