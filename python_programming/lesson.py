# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
#
# list1 = [7, 8, 9]
# list2 = [10, 11, 12]
#
# tuple1 = (list1, list2, 4)
# tuple1[0][0] = 10000
# print(tuple1)
#
# list1 = list2
# tuple1 = (list1, list2, 4)
# print(tuple1)
#
# print(type(list1))
# print(type(tuple1))
#
# dic1 = {"apple": 100,
#         "banana": 200,
#         "grape": 300}
# dic2 = dict(grape="500",
#             kiwi="50")
# print(dic1)
# print(dic2)
# print(dic1["grape"])
# print(type(dic1))
#
# dic1.update(dic2)
# print('update')
# print(dic1)
# print('#######')
# print(dic1.items())
# print(type(dic1.items()))
# print('######################')
# for v, k in dic1.items():
#     print(v, ':', k)
# print('######################')
# days = ['Mon', 'Tue', 'Wen']
# fruits = ['banana', 'apple', 'kiwi']
# for i in days:
#     print(i)
# print('######################')
# for day, fruit in zip(days, fruits):
#     print(day, fruit)

#
# def dic_add_func(key, value, dic={}):
#     dic[key] = value
#     # dic_temp = {key: value}
#     # dic.update(dic_temp)
#     return dic
#
#
# f = dic_add_func(1, 'one')
# print(f)
# f = dic_add_func(2, 'two')
# print(f)
#
#
# def dic_new_func(key, value, dic=None):
#     if dic is None:
#         dic = {}
#     dic[key] = value
#     return dic
#
#
# f = dic_new_func(1, 'one')
# print(f)
# f = dic_new_func(2, 'two')
# print(f)


# def test_plural_args(dictionary=None, *args, **kwargs):
#     if dictionary is None:
#         dictionary = {}
#     for arg in args:
#         print(arg)
#     for k, v in kwargs.items():
#         print(k, v)
#         dictionary[k] = v
#     # print(dictionary)
#     #     dict[k] = v
#     # print(tuple)
#     # print(dict)
#
#
# t = ((1, 2, 3), (1, 4, 5))
# # t = (100, 400, 500)
# t += t
# # print(t)
#
# dic1 = {'1': 'one',
#         '2': 'two',
#         '3': 'three'
#         }
# dic2 = {'0': 'zero'}
# test_plural_args(None, *t, first='one', second='two')
# print('#################')
# test_plural_args(dic2, *t, **dic1)
# print(dic2)
#
#
# def func_in_func_closure(pi):   # 関数内関数、クロージャー関数
#     def circle_area(radius):
#         return radius * radius * pi
#
#     return circle_area
#
#
# ans1 = func_in_func_closure(3.14)
# ans2 = func_in_func_closure(3.141592)
# radius = 10
# print(ans1(radius), ans2(radius))

"""デコレーター"""


# def print_more(func):
#     def wrapper(*args, **kwargs):
#         print("func:", func.__name__)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
#
#
# def print_info(func):
#     def wrapper(*args, **kwargs):
#         print("info_call_func:", func.__name__)   #print_more(func)の戻り値 wrapper が入る
#         print('start')
#         result = func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
#
#
# @print_info
# @print_more
# def add_num(a, b):
#     return a+b
#
#
# r = add_num(10, 20)
# print(r)
# print('####')
# r2 = print_info(print_more(add_num(10, 20)))
# print(r2)


""" デコレーター
<html><body>文字列</body></html>
"""

#
# def html_deco(func):
#     def wrapper(*args, **kwargs):
#         res = '<html>'
#         res += func(*args, **kwargs)
#         res += '</html>'
#         return res
#     return wrapper
#
#
# def body_deco(func):
#     def wrapper(*args, **kwargs):
#         res = '<body>'
#         res += func(*args, **kwargs)
#         res += '</body>'
#         return res
#     return wrapper
#
#
# @html_deco
# @body_deco
# def get_content(content):
#     return content
#
#
# test0 = 'test0'
# print(get_content(test0))


"""##################################################################################################"""
"""
デコレーターに引数を渡すことで、コードを省略
<html><body>文字列</body></html>
"""


# def deco_tag(tag):
#     def _deco_tag(func):
#         def wrapper(*args, **kwargs):
#             print("func:", func.__name__)
#             result = '<' + tag + '>'
#             result += func(*args, **kwargs)
#             result += '<' + tag + '/>'
#             return result
#         return wrapper
#     return _deco_tag
#
#
# @deco_tag('html')
# @deco_tag('body')
# def make_line(string):
#     return string
#
#
# a = 'test'
# print(make_line(a))
#
# """デコレーターを分解して実行"""
#
#
# def put_line(string):
#     return string
#
#
# _deco_body = deco_tag('body')
# _deco_html = deco_tag('html')
# # wrapper_body = _deco_body(put_line)
# wrapper_body = _deco_body(lambda string: string)
# wrapper_html = _deco_html(wrapper_body)
# ret_html = wrapper_html('文字列')
# print(ret_html)


"""
デコレーターに
<html><body>文字列</body></html>
を渡すとデシリアライズして文字列を返す処理
"""
"""##################################################################################################"""
"""
ジェネレーター
"""
# ラムダ = lambda 引数: func(引数)
# padding = lambda string: print(string)
#
#
# def counter(num):
#     for _ in range(num):
#         ++_
#         if (_ % 2) != 0:
#             for i in range(100):
#                 ++i
#             yield i
#         else:
#             yield _
#
#
# generator = counter(5)
#
# print(next(generator))
# padding('#####')
# print(next(generator))
# padding('#####')
# print(next(generator))
# padding('#####')
# print(next(generator))
# padding('#####')
# print(next(generator))
# padding('#####')
# try:
#     print(next(generator))
# except StopIteration as ex:
#     print('エラー'.format(ex))
# except Exception as ex:
#     print('あらゆるエラー'.format(ex))
# else:
#     print('done')
# finally:
#     print('Generator End')

"""リスト、辞書、ジェネレーター内包表記"""
# """
# リスト内包表記
# """
# t = (1, 2, 3, 4, 5)
# r = []
#
# # 通常のタプル → リスト
# for i in t:
#     if (i % 2) == 0:
#         r.append(i)
# print(r)
#
# # リスト内包表記
# r = [i for i in t if i % 2 == 0]
# print(r)
# print('##################################')
# """
# 辞書内包表記
# """
# k = [1, 2, 3]
# v = ['one', 'two', 'three']
# d = {}
#
# # 通常のkey,value → 辞書
# for key, val in zip(k, v):
#     d[key] = val
# print(d)
#
# # 辞書内包表記
# d = {key: val for key, val in zip(k, v)}
# print(d)
# print('##################################')
# """
# ジェネレーター内包表記
# """
#
# # 通常のジェネレーター
#
#
# def gene():
#     for g in range(5):
#         if g % 2 == 0:
#             yield g
#
#
# gen = gene()       # ジェネレーターは関数を変数に置き換えが必要
# print(next(gen))
# print(next(gen))
# print(next(gen))
# try:
#     print(next(gen))
# except StopIteration as ex:
#     print('エラー'.format(ex))
# except Exception as ex:
#     print('あらゆるエラー'.format(ex))
# else:
#     print('done')
# finally:
#     print('Generator End')
#
#
# # ジェネレーター内包表記
# # yield を返値として指定しなくてもジェネレータが作成できる
# gen = (g for g in range(5) if (g % 2) == 0)         # ジェネレーター
# print(type(gen))
# for g in gen:
#     print(g)
#
#
# gen = tuple(g for g in range(5) if (g % 2) == 1)    # タプル
# print(type(gen))
# print(gen)


# Run -> Edit Configuration
# Script Path に py ファイルを指定
# Parameters に引数を指定
# C:\Users\yheci\PycharmProjects\python_programming\lesson.py
# import sys
#
# for i in sys.argv:
#     print(i)

"""パッケージ作成"""
# パッケージの作成
# lesson_package の作成、パッケージの中にファイルの作成 __init__.py utils.py を作成する
# lesson.py から utils.py の関数をコールする
#
# ファイルが存在するディレクトリ構造が変化した場合に対応するためにtry exceptで下記のように書ける
# try:
#     from lesson_package.nothing import utils
# except ImportError:
#     from lesson_package.tool import utils
#     from lesson_package.talk import animal
#     from lesson_package.talk import human
#
# #from lesson_package.talk import *
#
# r = utils.say_twice('Hello')
# print(r)
#
# print(human.cry() + ' and ' + human.sing())
# print(animal.cry() + ' and ' + animal.sing())
#
# # setup.py でパッケージ化して tar.gz 圧縮ファイルで配布する
# # Tools -> Create setup.py
# # Tools -> Run setup.py Task
# # sdist を選択しOKを押すと XXXXXXXX-ver.tar.gz が出力される

# 組込み関数
# import builtins
# builtins関数はimportしなくても使用することができる
#
# ranking = {
#     'A': 100,
#     'B': 85,
#     'C': 95
# }
# print(ranking.get('A'))
#
# list = sorted(ranking, key=ranking.get, reverse=True)
# print(type(list))
# print(list)

"""標準ライブラリ"""
# 標準ライブラリ　の関数を使用する場合は import が必要
# 文字列　'abcdabcdaabbccdd'
# key:１文字 value:該当文字の個数　を辞書型で出力する
#
# str = 'abcdabcdaabbccdd'
# dic = {}
#
# print('########################################################')
#
# """ ライブラリを使わない力技 """
# for letter in str:
#     if letter not in dic:
#         dic[letter] = 0     # key:letter に対する value を初期化
#     dic[letter] += 1
# print(dic)
#
# print('########################################################')
#
# """ setdefault を使う """
# """ setdefault って何か？ -> 辞書型変数の key,value の初期値を設定できる """
#
# str = 'abcdabcdaabbccdd'
# dic = {}
#
# for letter in str:
#     dic.setdefault(letter, 0)   # key:letter に対する value を 0 に設定
#     dic[letter] += 1
# print(dic)
#
# print('########################################################')
#
# """ ライブラリ：collections の defaultdict """
# """ defaultdict() はどのような処理をするか """
# """ dic = defaultdict(int)
#     デフォルトのvalue値に int オブジェクト（型）を入れる 辞書型の変数 を作成 """
#
#
# str = 'abcdabcdaabbccdd'
#
# from collections import defaultdict
# dic_int = defaultdict(int)
# print(dic_int)
#
# for letter in str:
#     dic_int[letter] += 1
#
# print(type(dic_int))
# print(dic_int)
#
# print(sorted(dic_int.items()))
#
#
# print('########################################################')
#
# """ dic = defaultdict(list)
#     デフォルトのvalue値に list オブジェクト（型）を入れる 辞書型の変数 dic になる """
#
# str = 'abcdabcdaabbccdd'
#
# from collections import defaultdict
# dic_list = defaultdict(list)
# print(dic_list)
#
# for letter in str:
#     dic_list[letter] = [1, 1]
#
# print(type(dic_list))
# print(dic_list)
#
# print(sorted(dic_list.items()))

"""pypi のサードパーティのライブラリ"""
# third package のライブラリの使用
# https://pypi.org/
# 上記サイトからパッケージをインストールするとパッケージが使える
# File -> Settings -> Python Interpreter で追加してもいいし、
# コンソール上で pip install termcolor のように打ってインストールしてもいい
# 今回は　termcolor というパッケージを例にしてサードパーティーのパッケージを使用してみる
#
# from termcolor import colored
#
# print(help(colored))
# print(colored('attention', color='red', on_color='on_grey'))
# import sys
#
# from termcolor import colored, cprint
#
# cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)
#
# text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
# print(text)
# cprint("Hello, World!", "green", "on_red")
#
# print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
# print_red_on_cyan("Hello, World!")
# print_red_on_cyan("Hello, Universe!")
#
# for i in range(10):
#     cprint(i, "magenta", end=" ")

"""パッケージの格納先"""
#
# import collections
# import sys
#
# import termcolor
#
# import lesson_package
#
# print(collections.__file__)
# print(termcolor.__file__)
# print(lesson_package.__file__)
#
# print(sys.path)

"""__name__ と __main__"""
# import lesson_package.talk.animal
# import lesson_package.talk.human
#
# import config
#
#
# def main():
#     print('lesson：' + __name__)
#
#
# if __name__ == '__main__':
#     main()

"""オブジェクトとクラス"""

""" クラスの定義 """
#
#
# class Person(object):
#
#     # コンストラクタ
#     def __init__(self, name='default_name', num=1):
#         self.name = name
#         self.num = num
#
#     def say_something(self):
#         print('Hello, I am {}.'. format(self.name))
#         self.run()
#
#     def run(self):
#         print('I\'m going to run {} times today.'. format(self.num))
#
#     # デストラクタ
#     def __del__(self):
#         print('{} オブジェクトの終了'.format(self.name))
#
#
# person1 = Person('Mike', num=2)
# person2 = Person('Mary', num=100)
# person1.say_something()
# person2.say_something()
#
# # デストラクトされる瞬間
# # person2は未だデストラクトされていない
# del person1
# print('##############################################################')
# del person2

# """ クラスの継承 """
# """ オーバーライド """
# """ super(). 親の～ """
#
#
# class Car(object):
#     def __init__(self, model=None, color=None):
#         self.model = model
#         self.color = color
#         print('I am Parent!!!')
#         print('Color is {}.'.format(color))
#
#     def run(self):
#         print('{} run slowly.'.format(self.model))
#
#
# class ToyotaCar(Car):   # run() をオーバーライドのしてみた 親のメソッドを super()で使用してみた
#     def run(self):
#         super().run()
#         print('{} run fast.'.format(self.model))
#
#
# class TeslaCar(Car):    # __init__ のオーバーライド / プロパティ
#     def __init__(self, model='Model S', color='Black',
#                  passwd='123', enable_auto_run=False):
#         super().__init__(model, color)  # 親クラスで記載した処理を記載しなくて済む
#         self.password = passwd
#         self._enable_auto_run = enable_auto_run
#
#     # プロパティの読込みと書き込み
#     # 読込み専用
#     @property
#     def read_only_enable_auto_run(self):
#         return self._enable_auto_run
#
#     # 書き込み専用
#     @read_only_enable_auto_run.setter
#     def write_only_enable_auto_run(self, is_enable):
#         if self.password == 123:
#             self._enable_auto_run = is_enable
#         else:
#             raise ValueError
#
#     def auto_run(self):
#         print('{} auto run.'.format(self.model))
#
#
# car = Car()
# car.run()
# print('##############################################################')
# toyota_car = ToyotaCar('Lexus')
# toyota_car.run()
# print('##############################################################')
# tesla_car1 = TeslaCar(passwd=123)
# tesla_car1.run()
# tesla_car1.auto_run()
# tesla_car1.write_only_enable_auto_run = True
# print(tesla_car1.read_only_enable_auto_run)
# print('##############################################################')
# tesla_car2 = TeslaCar(passwd=000)
# tesla_car2.run()
# tesla_car2.auto_run()
# tesla_car2.write_only_enable_auto_run = True
# print(tesla_car1.read_only_enable_auto_run)
#
# del car
# del toyota_car
# del tesla_car1
# del tesla_car2

""" ダックタイピング """
""" クラスの中で作成したメソッドを、他クラスのメソッドの中で呼び出す """
""" メソッドの引数にオブジェクトを入れて、そのオブジェクトのメソッドとしてコールするだけ """

#
# class Person(object):
#     def __init__(self, age=1):
#         self.age = age
#
#     def drive(self):
#         if self.age > 18:
#             print('OK')
#         else:
#             raise Exception('Under 18, No Drive')
#
#
# class Child(Person):
#     def __init__(self, age=1):
#         if age < 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
#
# class Adult(Person):
#     def __init__(self, age=18):
#         if age >= 18:
#             super().__init__(age)
#         else:
#             raise ValueError
#
#
# child = Child(17)
# adult = Adult(20)
# adult.drive()
#
#
# class Car(object):
#     def __init__(self, model=None, color=None):
#         self.model = model
#         self.color = color
#
#     def run(self):
#         print('{} run.'.format(self.model))
#
#     def drive(self, person=None):
#         print('##########')
#         person.drive()
#
#
# car = Car()
# car.drive(adult)
# car.drive(child)

""" 抽象クラス、多重継承、クラス変数、クラスメソッドとスタティックメソッド、特殊メソッド """


























