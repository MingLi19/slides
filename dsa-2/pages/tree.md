## 二叉树

二叉树 `Binary Tree` 是一种非线性数据结构，代表“祖先”与“后代”之间的派生关系，体现了“一分为二”的分治逻辑`Dive and Conquer`。与 `Linked List`类似，二叉树的基本单元是节点，每个节点包含值、左子节点引用和右子节点引用。

```py
class TreeNode:
    """二叉树节点类"""
    def __init__(self, val: int):
        self.val: int = val                # 节点值
        self.left: TreeNode | None = None  # 左子节点引用
        self.right: TreeNode | None = None # 右子节点引用
```

<img class="w-120 mx-auto" border="rounded" src="../images/tree/binary_tree.png">

<!--
每个节点都有两个引用（指针），分别指向左子节点（left-child node）和右子节点（right-child node），该节点被称为这两个子节点的父节点（parent node）。当给定一个二叉树的节点时，我们将该节点的左子节点及其以下节点形成的树称为该节点的左子树（left subtree），同理可得右子树（right subtree）。
-->
---

## 常见术语

<br>

- **根节点（root node）** 位于二叉树顶层的节点，没有父节点。
- **叶节点（leaf node）** 没有子节点的节点，其两个指针均指向 None 。
- **边（edge）** 连接两个节点的线段，即节点引用（指针）。
- **节点所在的层（level）** 从顶至底递增，根节点所在层为 1 。
- **节点的度（degree）** 节点的子节点的数量。在二叉树中，度的取值范围是 0、1、2 。
- **二叉树的高度（height）** 从根节点到最远叶节点所经过的边的数量。
- **节点的深度（depth）** 从根节点到该节点所经过的边的数量。
- **节点的高度（height）** 从距离该节点最远的叶节点到该节点所经过的边的数量。

---

## 初始化二叉树

<br>

1. 初始化节点
2. 构建节点之间的引用（指针）

<br>

```py {1-7|8-12}
# 初始化二叉树
# 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
# 构建节点之间的引用（指针）
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
```

---

## 插入与删除节点

<br>

```py
# 插入与删除节点
p = TreeNode(0)
# 在 n1 -> n2 中间插入节点 P
n1.left = p
p.left = n2
# 删除节点 P
n1.left = n2
```

<img class="w-130 mx-auto" border="rounded" src="../images/tree/bt_insert.png">

---
layout: two-cols
layoutClass: gap-2
---

<img class="w-100 mx-auto" border="rounded" src="../images/tree/perfect_bt.png">

<img class="w-100 mx-auto" border="rounded" src="../images/tree/full_bt.png">

::right::

<img class="w-100 mx-auto" border="rounded" src="../images/tree/complete_bt.png">

<img class="w-100 mx-auto" border="rounded" src="../images/tree/balanced_bt.png">
<!--
 所有层的节点都被完全填满。在完美二叉树中，叶节点的度为 0 ，其余所有节点的度都为 2 ；若树的高度为 h ，则节点总数为  $2^{h+1} - 1$ ，呈现标准的指数级关系，反映了自然界中常见的细胞分裂现象。
 只有最底层的节点未被填满，且最底层节点尽量靠左填充。请注意，完美二叉树也是一棵完全二叉树。
-->
---

## 二叉树的退化

展示了二叉树的理想结构与退化结构。当二叉树的每层节点都被填满时，达到“完美二叉树”；而当所有节点都偏向一侧时，二叉树退化为“链表”。

- 完美二叉树是理想情况，可以充分发挥二叉树“分治”的优势。
- 链表则是另一个极端，各项操作都变为线性操作，时间复杂度退化至 `O(n)`

<img class="w-100 mx-auto" border="rounded" src="../images/tree/degenerate.png">

---

## 二叉树的最佳结构与最差结构

在最佳结构和最差结构下，二叉树的叶节点数量、节点总数、高度等达到极大值或极小值。

|  | 完美二叉树 | 链表 |
| --- | --- | --- | 
| 第 `i` 层的节点数量 | $2^{i-1}$ | 1 |
| 高度为 `h` 的树的叶节点数量 | $2^h$ | 1 |
| 高度为 `h` 的树的节点总数 | $2^{h+1} - 1$ | $h+1$ |
| 节点总数为 `n` 的树的高度 | $\log_2(n+1) - 1$ | $n-1$ |

---

## 二叉树遍历

从物理结构的角度来看，树是一种基于链表的数据结构，因此其遍历方式是通过指针逐个访问节点。然而，树是一种非线性数据结构，这使得遍历树比遍历链表更加复杂，需要借助搜索算法来实现。

二叉树常见的遍历方式包括
- 层序遍历 `level-order traversal`
- 前序遍历 `pre-order traversal`
- 中序遍历 `in-order traversal`
- 后序遍历 `post-order traversal`

---

## 层序遍历

广度优先遍历通常借助“队列”来实现。队列遵循 <span v-mark.red>先进先出</span> 的规则，而广度优先遍历则遵循 <span v-mark.red>逐层推进</span> 的规则，两者背后的思想是一致的。

```py {*|1-5|6-7|8-16}
def level_order(root: TreeNode | None) -> list[int]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue: deque[TreeNode] = deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    # 遍历队列
    while queue:
        node: TreeNode = queue.popleft()  # 队列出队
        res.append(node.val)  # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right)  # 右子节点入队
    return res
```

---

## 前序、中序、后序遍历

相应地，前序、中序和后序遍历都属于深度优先遍历 `depth-first traversal`，也称深度优先搜索`depth-first search` 或 `DFS`。 它体现了一种 <span v-mark.red>先走到尽头，再回溯继续</span> 的遍历方式。

<img class="w-150 mx-auto" border="rounded" src="../images/tree/dfs.png">

---

```py {1-8|10-17|19-26}
def pre_order(root: TreeNode | None):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root: TreeNode | None):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root: TreeNode | None):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)
```

---

## 二叉树数组表示

如何将二叉树表示为数组？给定一棵完美二叉树，我们将所有节点按照层序遍历的顺序存储在一个数组中，则每个节点都对应唯一的数组索引。

根据层序遍历的特性，我们可以推导出父节点索引与子节点索引之间的 <span v-mark.red>映射公式</span>：若某节点的索引为 `i`, 则该节点的左子节点索引为 `2*i+1`, 右子节点索引为 `2*i+2`。

<img class="w-140 mx-auto" border="rounded" src="../images/tree/array.png">

<!--
映射公式的角色相当于链表中的节点引用（指针）。给定数组中的任意一个节点，我们都可以通过映射公式来访问它的左（右）子节点。
-->
---
layout: two-cols
layoutClass: gap-2
---

<img class="w-100 mx-auto" border="rounded" src="../images/tree/without_none.png">

```py
# 层序遍历的数组表示
tree = [1, 2, 3, 4, 6, 7, 8, 9, 12, 15]
```

::right::

<img class="w-100 mx-auto" border="rounded" src="../images/tree/with_none.png">

```py
# 使用 None 来表示空位
tree = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]
```

---

## 完全二叉树的数组表示

完全二叉树非常适合使用数组来表示。回顾完全二叉树的定义，`None` 只出现在最底层且靠右的位置，因此所有 None 一定出现在层序遍历序列的末尾。这意味着使用数组表示完全二叉树时，可以省略存储所有 `None`。

<img class="w-150 mx-auto" border="rounded" src="../images/tree/complete_bt_pro.png">

---

````md magic-move
```py 
class ArrayBinaryTree:
    def size(self):
        """列表容量"""
        pass

    def val(self, i: int) -> int | None:
        """获取索引为 i 节点的值"""
        pass

    def left(self, i: int) -> int | None:
        """获取索引为 i 节点的左子节点的索引"""
        pass

    def right(self, i: int) -> int | None:
        """获取索引为 i 节点的右子节点的索引"""
        pass

    def parent(self, i: int) -> int | None:
        """获取索引为 i 节点的父节点的索引"""
        pass
```
```py
class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        """构造方法"""
        self._tree = list(arr)

    def size(self):
        """列表容量"""
        return len(self._tree)

    def val(self, i: int) -> int | None:
        """获取索引为 i 节点的值"""
        # 若索引越界，则返回 None ，代表空位
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]

    def left(self, i: int) -> int | None:
        """获取索引为 i 节点的左子节点的索引"""
        return 2 * i + 1

    def right(self, i: int) -> int | None:
        """获取索引为 i 节点的右子节点的索引"""
        return 2 * i + 2

    def parent(self, i: int) -> int | None:
        """获取索引为 i 节点的父节点的索引"""
        return (i - 1) // 2
```
````

<!--
以下代码实现了一棵基于数组表示的二叉树，包括以下几种操作。
给定某节点，获取它的值、左（右）子节点、父节点。
获取前序遍历、中序遍历、后序遍历、层序遍历序列。
-->
---
layout: two-cols
layoutClass: gap-2
---

````md magic-move
```py 
    def level_order(self) -> list[int]:
        """层序遍历"""
        pass

    def dfs(self, i: int, order: str):
        """深度优先遍历"""
        pass
```
```py
    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        # 直接遍历数组
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res

    def dfs(self, i: int, order: str):
        """深度优先遍历"""
        if self.val(i) is None:
            return
        # 前序遍历
        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        # 中序遍历
        if order == "in":
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        # 后序遍历
        if order == "post":
            self.res.append(self.val(i))
```
````

::right::

````md magic-move
```py
    def pre_order(self) -> list[int]:
        """前序遍历"""
        pass

    def in_order(self) -> list[int]:
        """中序遍历"""
        pass

    def post_order(self) -> list[int]:
        """后序遍历"""
        pass
```
```py
    def pre_order(self) -> list[int]:
        """前序遍历"""
        self.res = []
        self.dfs(0, order="pre")
        return self.res

    def in_order(self) -> list[int]:
        """中序遍历"""
        self.res = []
        self.dfs(0, order="in")
        return self.res

    def post_order(self) -> list[int]:
        """后序遍历"""
        self.res = []
        self.dfs(0, order="post")
        return self.res        
```
````

---

## 二叉树总结

二叉树的数组表示主要有以下优点。

- 数组存储在连续的内存空间中，对缓存友好，访问与遍历速度较快。
- 不需要存储指针，比较节省空间。
- 允许随机访问节点。

然而，数组表示也存在一些局限性。

- 数组存储需要连续内存空间，因此不适合存储数据量过大的树。
- 增删节点需要通过数组插入与删除操作实现，效率较低。
- 当二叉树中存在大量 `None` 时，数组中包含的节点数据比重较低，空间利用率较低。

---

## 二叉搜索树

二叉搜索树（binary search tree）满足以下条件:

1. 对于根节点，`左子树中所有节点的值` < `根节点的值` < `右子树中所有节点的值`。
2. 任意节点的左、右子树也是二叉搜索树，即同样满足条件 `1.` 。

<img class="w-150 mx-auto" border="rounded" src="../images/tree/bst.png">

---

## 搜索操作