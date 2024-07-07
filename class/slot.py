'''
slotを使ったインスタンス変数の制限
'''

class Person():
    
    def __init__(self, name) -> None:
        self.name = name
    
class Person_slot():
    
    __slots__=['name', 'age'] # slotをつけるとインスタンス変数が制限される
    
    def __init__(self, name) -> None:
        self.name = name

man = Person('hajime')
man.age = 25
man.height = 170

print(man.name)
print(man.age)
print(man.height)


man_slot = Person_slot('hajime')
man_slot.age = 25
#man_slot.height = 170 #slotにheightが含まれないので、エラー

print(man.name)
print(man.age)
#print(man.height)
