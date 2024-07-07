import random

# 元のリスト
list = [1, 2, 3, 4, 5]

# 元のリストと同じサイズのリストを作成し、全ての要素をNoneで埋める
new_list = [None] * len(list)
print(new_list)

# 元のリストと同じサイズのリストを作成し、全ての要素を0で埋める
new_list = [0] * len(list)
print(new_list)

# for - inでリスト作成
new_list = [i for i in range(100)]
print(new_list)

# for - inでランダムなリスト作成
new_list = [random.randint(1, 10) for _ in range(100)]
print(new_list)
