'''
zipで要素をまとめる
'''

names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
points = [100, 85, 90]

for name, age, point in zip(names, ages, points):
    print(name, age, point)