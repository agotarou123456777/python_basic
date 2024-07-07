'''
プロパティを使うことでセッターとゲッターを省略して管理できる
'''

class Person():
    
    def __init__(self, name):
        self.__name = name ##__(アンダースコア２つ)をつけておくとインスタンス変数を直接参照できない
    
    @property #ゲッターメソッドにはpropertyデコレータをつける
    def name_method(self): #ゲッターを定義
        return self.__name
    
    @name_method.setter #セッターメソッドにはpropertyデコレータをつける
    def name_method(self, val): #セッターを定義
        self.__name = val
    
man = Person("hajime")
#print(man.__name) ##__(アンダースコア２つ)をつけておくとインスタンス変数を直接参照できない
print(man.name_method) #ゲッターメソッドを使って変数を取得する
man.name_method = "tahara" #セッターメソッドを使って変数を書き換える
print(man.name_method)