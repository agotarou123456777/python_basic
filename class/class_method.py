'''
クラスメソッドの呼び出し
クラスメソッドはインスタンス生成しなくても呼び出せる
'''

class Person:
    @classmethod #クラスインスタンスにはclassmethodデコレータをつける
    def echo_name(cls, first, last): #第一引数にclsを加える
        print("My name is {} {}".format(first, last))        

#
Person.echo_name("hajime", "tahara")

#インスタンス化してから使うこともできる
man = Person()
man.echo_name("sakai", "masato")

'''
クラスメソッドの活用例
クラスのインスタンス化を行うための関数として活用する：ファクトリーメソッド
'''
import requests

class Book:
    
    def __init__(self, code, title, price) -> None:
        self.code = code
        self.title = title
        self.price = price
    
    @classmethod
    def get_book_info(cls, code):
        res = requests.get(f'https://wings.msn.to/tmp/{code}.json') #webからisbnコードをキーにjsonを取得
        bs = res.json()
        return cls(bs['isbn'], bs['title'], bs['price']) #jsonから各キーを引数にしたインスタンスを返す
    
book = Book.get_book_info('978-4-7981-5112-0')
print(book.title)