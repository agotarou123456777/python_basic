'''
通常のクラスメソッド
'''
class Person():
    
    def __init__(self, name) -> None:
        self.name = name
        
    def show(self):
        print("My name is {}. This is normal closs method.".format(self.name))


man = Person('hajime')
man.show()

'''
動的なクラスメソッドの定義
クラスにメソッドを追加
'''
class Person_dynamic():
    
    def __init__(self, name) -> None:
        self.name = name
        
def dynamic_func(self):
    print("My name is {}. This is dynamic method".format(self.name))
    

Person_dynamic.show = dynamic_func #クラス自体にshowメソッドを追加した (クラス名).(メソッド名) = (動的に追加する関数)
man_dynamic = Person_dynamic('hajime dynamic')
man_dynamic.show()
man_dynamic2 = Person_dynamic('tahara dynamic')
man_dynamic2.show()

'''
動的なクラスメソッドの定義 (2)
インスタンスにメソッドを追加
'''
import types #typesモジュールが必須

class Person_dynamic_2():
    
    def __init__(self, name) -> None:
        self.name = name
        
def dynamic_func_2(self):
    print("My name is {}. This is dynamic method".format(self.name))
    
    
man_dynamic_2 = Person_dynamic_2('hajime dynamic_2')
#インスタンスにメソッドを追加 
#(インスタンス).(メソッド名) = types.MethodType((追加する関数), (インスタンス))
man_dynamic_2.show_method = types.MethodType(dynamic_func_2, man_dynamic_2) 
man_dynamic_2.show_method()
man_dynamic2_2 = Person_dynamic_2('tahara dynamic_2')
#man_dynamic2_2.show_method() #こちらのインスタンスにはメソッドを追加してないのでエラー