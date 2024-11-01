a = []
initial_size = a.__sizeof__()

for i in range(10):
    a.append(i)
    current_size = (a.__sizeof__() - initial_size) // 8
    print(current_size)
