'''
クラスの継承と独自メソッドの追加
'''

class Person():
    
    def __init__(self, name) -> None:
        self.name = name
    
    def echo_name(self):
        print("My name is", self.name)

class BusinessPerson(Person):
    
    #Personを継承し、workメソッドを追加
    def work(self, time):
        print("I am working", time)
        

hajime = BusinessPerson("hajime")
hajime.echo_name()
hajime.work("at night")

'''
クラスの継承とメソッドのオーバーライド
'''

class Hardworker(BusinessPerson):
    
    #BusinessPersonを継承し、workメソッドをオーバーライド
    def work(self, time):
        print("Hard Work !", time)
        

hard = Hardworker("hajime")
hard.echo_name()
hard.work("at morning")


'''
基底クラスのメソッド呼び出し
'''

class SuperBusinesPerson(BusinessPerson):
    
    #BusinessPersonを継承し、workメソッドをオーバーライド
    def work(self, time):
        super().work(time) #superで基底クラスの関数を呼び出す
        print("super work!")
    
    #新しいメソッドの追加
    def call_work(self, time):
        super().work(time) #オーバーライドしなくても基底クラスの関数を呼び出せる
        

hard = SuperBusinesPerson("hajime")
hard.echo_name()
hard.work("at noon")
hard.call_work("at noon")

'''
複数クラスの継承
'''

class Human():
    
    def __init__(self, type) -> None:
        self.type = type
    
    def echo_type(self):
        print("I am", self.type)

class HumanBusinessPerson(Person, Human):
    #__init__はPerson,Humanともに持っているので明示して定義し直す
    def __init__(self, name, type) -> None:
        Person.__init__(self, name)
        Human.__init__(self, type)
        
    #新たにworkメソッドを追加
    def work(self, time):
        print("I am working", time)
        
multi_super_class = HumanBusinessPerson("hajime", "human")
multi_super_class.echo_name()
multi_super_class.echo_type()
multi_super_class.work("at morning")
