'''
文字列に変数を埋め込んで出力
'''
s = 'Alice'
i = 25

print('Alice is %d years old' % i)
# Alice is 25 years old

print('%s is %d years old' % (s, i))
# Alice is 25 years old

print('{} is {} years old'.format(s, i))
# Alice is 25 years old

print('{name} is {age} years old'.format(name=s, age=i))
# Alice is 25 years old

##フォーマット指定
number = 0.45
print('{0:.4f} is {0:.2%}'.format(number))
# 0.4500 is 45.00%

print(f'{number:.4f} is {number:.2%}')
# 0.4500 is 45.00%


'''
フォーマット一覧
'''
i = 255

print('left   : {:<8}'.format(i))
print('center : {:^8}'.format(i))
print('right  : {:>8}'.format(i))
print('zero   : {:08}'.format(i))
print('bin    : {:b}'.format(i))
print('oct    : {:o}'.format(i))
print('hex    : {:x}'.format(i))
# left   : 255     
# center :   255   
# right  :      255
# zero   : 00000255
# bin    : 11111111
# oct    : 377
# hex    : ff

f = 0.1234

print('digit   : {:.2}'.format(f))
print('digit   : {:.6f}'.format(f))
print('exp     : {:.4e}'.format(f))
print('percent : {:.0%}'.format(f))
# digit   : 0.12
# digit   : 0.123400
# exp     : 1.2340e-01
# percent : 12%


'''
表示文字を更新
'''
import time
for i in range(10):
    print("\r"+str(i),end="")
    time.sleep(0.1)
print()