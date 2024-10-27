lst = []
allocated = 0
print("此时容量是: 0")

for item in range(100):
    lst.append(item)  # 添加元素

    # 计算ob_size
    ob_size = len(lst)

    # 判断ob_size和当前的容量
    if ob_size > allocated:
        # lst的大小减去空列表的大小, 再除以8显然就是容量的大小
        # 因为不管你有没有用, 容量已经分配了
        allocated = (lst.__sizeof__() - [].__sizeof__()) // 8
        print(f"列表扩容啦, 新的容量是: {allocated}")
