'''
特殊メソッド：__call__の使い方
'''

class Person:

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is ',self.name)

man = Person('hajime') 
man() #インスタンス名を呼ぶだけで、callメソッドが使用できる