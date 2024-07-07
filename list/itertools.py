'''
itertools.product()を使ってみる
'''
import itertools

l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']

p = itertools.product(l1, l2) # l1とl2の直積を求める

for v in p:
    print(v)

'''
3x3の正方形のセルの直積を求める
'''
x = 3
for i, j in itertools.product(range(x), repeat=2):
    print(i,j)