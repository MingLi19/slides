堆 `heap` 是一种满足特定条件的完全二叉树, 主要可分为两种类型, 如图所示。

- 小顶堆 `min heap` 任意节点的值 <= 其子节点的值。
- 大顶堆 `max heap` 任意节点的值 >= 其子节点的值。

<img class="w-100 mx-auto" src="../images/heap/definition.png" />

堆作为完全二叉树的一个特例, 具有以下特性:
- 最底层节点靠左填充, 其他层的节点都被填满。
- 我们将二叉树的根节点称为“堆顶”, 将底层最靠右的节点称为“堆底”。
- 对于大顶堆（小顶堆）, 堆顶元素（根节点）的值是最大（最小）的。

---

## 堆的操作

<br>

| 操作 | 描述 | 时间复杂度 |
| --- | --- | --- |
| `push()` | 元素入堆 | O(log n) |
| `pop()` | 堆顶元素出堆 | O(log n) |
| `peek()` | 访问堆顶元素（对于大 / 小顶堆分别为最大 / 小值） | O(1) |
| `size()` | 获取堆的元素数量 | O(1) |
| `isEmpty()` | 判断堆是否为空 | O(1) |

---

## 堆在python中的实现

在实际应用中, 我们可以直接使用编程语言提供的堆类, 以 Python 的 `heapq` 为例。

```py {*|1-4|6-8|10-15|17-18|20-26|28-29|31-32|34-38}{maxHeight: '440px'}
# 初始化小顶堆
min_heap, flag = [], 1
# 初始化大顶堆
max_heap, flag = [], -1

# Python 的 heapq 模块默认实现小顶堆
# 考虑将“元素取负”后再入堆, 这样就可以将大小关系颠倒, 从而实现大顶堆
# 在本示例中, flag = 1 时对应小顶堆, flag = -1 时对应大顶堆

# 元素入堆
heapq.heappush(max_heap, flag * 1)
heapq.heappush(max_heap, flag * 3)
heapq.heappush(max_heap, flag * 2)
heapq.heappush(max_heap, flag * 5)
heapq.heappush(max_heap, flag * 4)

# 获取堆顶元素
peek: int = flag * max_heap[0] # 5

# 堆顶元素出堆
# 出堆元素会形成一个从大到小的序列
val = flag * heapq.heappop(max_heap) # 5
val = flag * heapq.heappop(max_heap) # 4
val = flag * heapq.heappop(max_heap) # 3
val = flag * heapq.heappop(max_heap) # 2
val = flag * heapq.heappop(max_heap) # 1

# 获取堆大小
size: int = len(max_heap)

# 判断堆是否为空
is_empty: bool = not max_heap

# 输入列表并建堆
min_heap: list[int] = [1, 2, 3, 4, 5, 4, 3, 2, 1]
heapq.heapify(min_heap) # 小顶堆 [1, 1, 3, 2, 5, 4, 3, 2, 4]
```

---

## 数组实现堆

前面讲过, 完全二叉树非常适合用数组来表示。由于堆正是一种完全二叉树, 因此我们将采用数组来存储堆。

当使用数组表示二叉树时, 元素代表节点值, 索引代表节点在二叉树中的位置。节点指针通过下面公式来实现。

- 对于下标 `i` 的节点：
  - 父节点：`(i - 1) // 2`
  - 左子节点：`2 * i + 1`
  - 右子节点：`2 * i + 2`

<img class="w-120 mx-auto" src="../images/heap/array_heap.png" />

<style>
li {
  font-size: 16px;
}
</style>
---

### 获取索引

```py
def left(self, i: int) -> int:
    """获取左子节点的索引"""
    return 2 * i + 1

def right(self, i: int) -> int:
    """获取右子节点的索引"""
    return 2 * i + 2

def parent(self, i: int) -> int:
    """获取父节点的索引"""
    return (i - 1) // 2  # 向下整除
```

<br>

### 访问堆顶元素

```py
def peek(self) -> int:
    """访问堆顶元素"""
    return self.max_heap[0]
```

---

### 元素入堆

给定元素 `val` , 我们首先将其添加到堆底。添加之后, 由于 `val` 可能大于堆中其他元素, 堆的成立条件可能已被破坏, 因此需要修复从插入节点到根节点的路径上的各个节点, 这个操作被称为堆化 `heapify` 。

考虑从入堆节点开始, 从底至顶执行堆化。如图所示, 我们比较插入节点与其父节点的值, 如果插入节点更大, 则将它们交换。然后继续执行此操作, 从底至顶修复堆中的各个节点, 直至越过根节点或遇到无须交换的节点时结束。

<v-switch>
  <template #1>
    <img class="w-150 mx-auto" src="../images/heap/in1.png" />
  </template>
  <template #2>
    <img class="w-150 mx-auto" src="../images/heap/in2.png" />
  </template>
  <template #3>
    <img class="w-150 mx-auto" src="../images/heap/in3.png" />
  </template>
  <template #4>
    <img class="w-150 mx-auto" src="../images/heap/in4.png" />
  </template>
  <template #5>
    <img class="w-150 mx-auto" src="../images/heap/in5.png" />
  </template>
  <template #6>
    <img class="w-150 mx-auto" src="../images/heap/in6.png" />
  </template>
  <template #7>
    <img class="w-150 mx-auto" src="../images/heap/in7.png" />
  </template>
  <template #8>
    <img class="w-150 mx-auto" src="../images/heap/in8.png" />
  </template>
  <template #9>
    <img class="w-150 mx-auto" src="../images/heap/in9.png" />
  </template>
</v-switch>

---
  
设节点总数为 $n$ , 树的高度为 $O(\log n)$ 。堆化操作的循环轮数最多为 $O(\log n)$, 因此堆化操作的时间复杂度为 $O(\log n)$ 。

```py {*|1-6|8-|*}
def push(self, val: int):
    """元素入堆"""
    # 添加节点
    self.max_heap.append(val)
    # 从底至顶堆化
    self.sift_up(self.size() - 1)

def sift_up(self, i: int):
    """从节点 i 开始, 从底至顶堆化"""
    while True:
        # 获取节点 i 的父节点
        p = self.parent(i)
        # 当“越过根节点”或“节点无须修复”时, 结束堆化
        if p < 0 or self.max_heap[i] <= self.max_heap[p]:
            break
        # 交换两节点
        self.swap(i, p)
        # 循环向上堆化
        i = p
```

---

### 堆顶元素出堆

堆顶元素是二叉树的根节点, 即列表首元素。如果我们直接从列表中删除首元素, 那么二叉树中所有节点的索引都会发生变化, 这将使得后续使用堆化进行修复变得困难。为了尽量减少元素索引的变动, 我们采用以下操作步骤。
1. 交换堆顶元素与堆底元素（交换根节点与最右叶节点）。
2. 交换完成后, 将堆底从列表中删除（注意, 由于已经交换, 因此实际上删除的是原来的堆顶元素）。
3. 从根节点开始, 从顶至底执行堆化。

“从顶至底堆化”的操作方向与“从底至顶堆化”相反, 我们将根节点的值与其两个子节点的值进行比较, 将最大的子节点与根节点交换。然后循环执行此操作, 直到越过叶节点或遇到无须交换的节点时结束。

<v-switch>
  <template #1>
    <img class="w-100 mx-auto" src="../images/heap/out1.png" />
  </template>
  <template #2>
    <img class="w-100 mx-auto" src="../images/heap/out2.png" />
  </template>
  <template #3>
    <img class="w-100 mx-auto" src="../images/heap/out3.png" />
  </template>
  <template #4>
    <img class="w-100 mx-auto" src="../images/heap/out4.png" />
  </template>
  <template #5>
    <img class="w-100 mx-auto" src="../images/heap/out5.png" />
  </template>
  <template #6>
    <img class="w-100 mx-auto" src="../images/heap/out6.png" />
  </template>
  <template #7>
    <img class="w-100 mx-auto" src="../images/heap/out7.png" />
  </template>
  <template #8>
    <img class="w-100 mx-auto" src="../images/heap/out8.png" />
  </template>
  <template #9>
    <img class="w-100 mx-auto" src="../images/heap/out9.png" />
  </template>
  <template #10>
    <img class="w-100 mx-auto" src="../images/heap/out10.png" />
  </template>
</v-switch>


<style>
li {
  font-size: 16px;
}
</style>
---

```py {*|-13|15-|*}{maxHeight: '500px'}
def pop(self) -> int:
    """元素出堆"""
    # 判空处理
    if self.is_empty():
        raise IndexError("堆为空")
    # 交换根节点与最右叶节点（交换首元素与尾元素）
    self.swap(0, self.size() - 1)
    # 删除节点
    val = self.max_heap.pop()
    # 从顶至底堆化
    self.sift_down(0)
    # 返回堆顶元素
    return val

def sift_down(self, i: int):
    """从节点 i 开始, 从顶至底堆化"""
    while True:
        # 判断节点 i, l, r 中值最大的节点, 记为 ma
        l, r, ma = self.left(i), self.right(i), i
        if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
            ma = l
        if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
            ma = r
        # 若节点 i 最大或索引 l, r 越界, 则无须继续堆化, 跳出
        if ma == i:
            break
        # 交换两节点
        self.swap(i, ma)
        # 循环向下堆化
        i = ma
```

---

### 常见应用

<br>

- 优先队列：堆通常作为实现优先队列的首选数据结构, 其入队和出队操作的时间复杂度均为 $O(\log n)$ , 而建堆操作为 $O(n)$ , 这些操作都非常高效。
- 堆排序：给定一组数据, 我们可以用它们建立一个堆, 然后不断地执行元素出堆操作, 从而得到有序数据。然而, 我们通常会使用一种更优雅的方式实现堆排序。
- 获取最大的 k 个元素：这是一个经典的算法问题, 同时也是一种典型应用, 例如选择热度前 10 的新闻作为微博热搜, 选取销量前 10 的商品等。

---

## 建堆操作

我们首先创建一个空堆, 然后遍历列表, 依次对每个元素执行“入堆操作”, 即先将元素添加至堆的尾部, 再对该元素执行“从底至顶”堆化。

每当一个元素入堆, 堆的长度就加一。由于节点是从顶到底依次被添加进二叉树的, 因此堆是“自上而下”构建的。

设元素数量为 `n` , 每个元素的入堆操作使用 $O(\log n)$ 的时间, 因此建堆操作的时间复杂度为 $O(n \log n)$ 。

实际上, 我们可以实现一种更为高效的建堆方法, 共分为两步。
1. 将列表所有元素原封不动地添加到堆中, 此时堆的性质尚未得到满足。
2. 倒序遍历堆（层序遍历的倒序）, 依次对每个非叶节点执行“从顶至底堆化”。

每当堆化一个节点后, 以该节点为根节点的子树就形成一个合法的子堆。而由于是倒序遍历, 因此堆是“自下而上”构建的。

之所以选择倒序遍历, 是因为这样能够保证当前节点之下的子树已经是合法的子堆, 这样堆化当前节点才是有效的。

---

由于叶节点没有子节点, 因此它们天然就是合法的子堆, 无须堆化。如以下代码所示, 最后一个非叶节点是最后一个节点的父节点, 我们从它开始倒序遍历并执行堆化：

```py {*|-7|9-|*}{maxHeight: '420px'}
def __init__(self, nums: list[int]):
    """构造方法, 根据输入列表建堆"""
    # 将列表元素原封不动添加进堆
    self.max_heap = nums
    # 堆化除叶节点以外的其他所有节点
    for i in range(self.parent(self.size() - 1), -1, -1):
        self.sift_down(i)

def sift_down(self, i: int):
    """从节点 i 开始, 从顶至底堆化"""
    while True:
        # 判断节点 i, l, r 中值最大的节点, 记为 ma
        l, r, ma = self.left(i), self.right(i), i
        if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
            ma = l
        if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
            ma = r
        # 若节点 i 最大或索引 l, r 越界, 则无须继续堆化, 跳出
        if ma == i:
            break
        # 交换两节点
        self.swap(i, ma)
        # 循环向下堆化
        i = ma
```

---

## Top-k 问题

<br>

> 给定一个长度为 `n` 的无序数组 `nums` , 请返回数组中最大的 `k` 个元素。

<br>

1. 方法一：遍历选择

我们可以进行图所示的 `k` 轮遍历, 分别在每轮中提取第 `1、2、... k` 大的元素, 时间复杂度为 $O(nk)$ 。

此方法只适用于 `k << n` 的情况, 因为当 `k` 接近 `n` 时, 其时间复杂度趋向于 $O(n^2)$ , 非常耗时。

<img class="w-120 mx-auto" src="../images/heap/topk1.png" />

---

2. 方法二：排序

如图所示, 我们可以先对数组 `nums` 进行排序, 再返回最右边的 `k` 个元素。时间复杂度为 $O(n \log n)$ 。

显然, 该方法“超额”完成任务了, 因为我们只需找出最大的 `k` 个元素即可, 而不需要排序其他元素。

<img class="w-170 mx-auto" src="../images/heap/topk2.png" />

---

3. 方法三：堆

我们可以基于堆更加高效地解决 `Top-k` 问题, 流程如图所示。
1. 初始化一个小顶堆, 其堆顶元素最小。
2. 先将数组的前 `k` 个元素依次入堆。
3. 从第 `k + 1` 个元素开始, 若当前元素大于堆顶元素, 则将堆顶元素出堆, 并将当前元素入堆。
4. 遍历完成后, 堆中保存的就是最大的 `k` 个元素。

<v-switch>
  <template #1>
    <img class="w-130 mx-auto" src="../images/heap/topk31.png" />
  </template>
  <template #2>
    <img class="w-130 mx-auto" src="../images/heap/topk32.png" />
  </template>
  <template #3>
    <img class="w-130 mx-auto" src="../images/heap/topk33.png" />
  </template>
  <template #4>
    <img class="w-130 mx-auto" src="../images/heap/topk34.png" />
  </template>
  <template #5>
    <img class="w-130 mx-auto" src="../images/heap/topk35.png" />
  </template>
  <template #6>
    <img class="w-130 mx-auto" src="../images/heap/topk36.png" />
  </template>
  <template #7>
    <img class="w-130 mx-auto" src="../images/heap/topk37.png" />
  </template>
  <template #8>
    <img class="w-130 mx-auto" src="../images/heap/topk38.png" />
  </template>
  <template #9>
    <img class="w-130 mx-auto" src="../images/heap/topk39.png" />
  </template>
</v-switch>

---
  
```py {*|3-4|5-7|8-9|10-13|14|*}
def top_k_heap(nums: list[int], k: int) -> list[int]:
    """基于堆查找数组中最大的 k 个元素"""
    # 初始化小顶堆
    heap = []
    # 将数组的前 k 个元素入堆
    for i in range(k):
        heapq.heappush(heap, nums[i])
    # 从第 k+1 个元素开始, 保持堆的长度为 k
    for i in range(k, len(nums)):
        # 若当前元素大于堆顶元素, 则将堆顶元素出堆、当前元素入堆
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])
    return heap
```


总共执行了 n 轮入堆和出堆, 堆的最大长度为 k , 因此时间复杂度为 $O(n \log k)$ 。该方法的效率很高, 当 k 较小时, 时间复杂度趋向 $O(n)$ 。当 k 较大时, 时间复杂度不会超过 $O(n \log n)$ 。

另外, 该方法适用于动态数据流的使用场景。在不断加入数据时, 我们可以持续维护堆内的元素, 从而实现最大的 k 个元素的动态更新。