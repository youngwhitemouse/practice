'''
python魔法方法“Magic Method”：
    python 中内置好的用“__”双划线包起来的特定方法，在进行特定的操作时会自动被调用
    
    __init__    __new__     __class__
    __str__     __repr__
    __iter__    __next__
    __enter__   __exit__
    __doc__     __module__      __dict__
    __getitem__     __setitem__     __delitem__
    
    __mro__    __call__     __del__ 
    __all__
'''


# __new方法：创建并返回这个类的实例, __init方法：将传入的参数来初始化 该实例，两个共同构成“构造函数”
# class A(object):
#     def __init__(self,world):
#         print("init方法被调用了")
#         self.world = world
#
#     # new 方法必须要有返回值，返回实例化出来的实例
#     def __new__(cls,world):
#         print("new方法被调用了")
#         return object.__new__(cls)
#
#     # __str__方法：打印对象的描述信息，可读性，给用户看的
#     # 必须返回一个字符串类型的返回值
#     def __str__(self):
#         return 'world is %s str' % self.world
#
#     # __repr__方法，具有准确性,给开发人员看的，在控制台直接敲实例对象的名称
#     # def __repr__(self):
#     #     return 'world is %s repr' % self.world
#
#     # 当对象被删除时，会自动被调用，析构函数
#     def __del__(self):
#         print("__del__方法被调用")
#
#     # __call__方法
#     def __call__(self):
#         print("__call__方法别调用了")
#
#     # __iter__ 在类里面定义__iter__方法创建的对象就是可迭代对象
#     def __iter__(self):
#         pass
#
# t = A("hello")
# print(t)
# t()
# result = isinstance(t, Iterable)
# print(result)




# __class__方法：获得已知对象的类
# class A(object):
#     pass
# a = A()
# print(a.__class__)

# __class__方法的另一个用处：当一个类中的某个成员 变量是所有类的对象的公共变量时
# class A(object):
#     count = 0
#
#     def addcount(self):
#         # self.__class__.count += 1
#         self.count += 1
#
# a = A()
# a.addcount()
# print(a.count)
# print("*"*50)
# b = A()
# b.addcount()
# print(b.count)





# __mro__: Method Resolution Order,方法解析顺序
# class A(object):
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# class D(B, C):
#     pass
# print(D.__mro__)






# 实现了 __enter__() 和 __exit__() 方法的对象都可称为上下文管理器
# class File():
#
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         print("entering")
#         self.f = open(self.filename, self.mode)
#         return self.f
#
#     def __exit__(self, *args):
#         print("will exit")
#         self.f.close()
#
#
# with File('out.txt', 'w') as f:
#     print("writing")
#     f.write('hello, python')




# __doc__ 描述类信息
# class Foo:
#     """ 描述类信息，测试__doc__方法 """
#     def func(self):
#         pass
#
# print(Foo.__doc__)





# __dict__  获取类或对象中的所有属性
# class Province(object):
#     country = 'China'
#
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
#     def func(self, *args, **kwargs):
#         print('func')
#
# # 获取类的属性，即：类属性、方法、
# print(Province.__dict__)
#
# obj1 = Province('山东', 10000)
# print(obj1.__dict__)
# # 获取 对象obj1 的属性
#
# obj2 = Province('山西', 20000)
# print(obj2.__dict__)
# # 获取 对象obj2 的属性





# __module__ 方法获取当前操作的对象在哪个模块
# from 测试__module__ import Person
#
# obj = Person()
# print(obj.__module__)







# __getitem__、__setitem__、__delitem__用于索引操作，如字典,分别表示获取、设置、删除数据
# class Foo(object):
#
#     def __getitem__(self, key):
#         print('__getitem__', key)
#
#     def __setitem__(self, key, value):
#         print('__setitem__', key, value)
#
#     def __delitem__(self, key):
#         print('__delitem__', key)
#
#
# obj = Foo()
#
# result = obj['k1']      # 自动触发执行 __getitem__
# obj['k2'] = 'laotie'    # 自动触发执行 __setitem__
# del obj['k1']           # 自动触发执行 __delitem__






# __all__:可以限制模块中的函数和方法是否被导入
# _all__魔法方法只针对通过 from xx import *这种导入方式有效
__all__ = ["a", "b"]
def a():
    print("a被导入")
def b():
    print("b被导入")
def c():
    print("c被导入")

if __name__ == '__main__':
    pass

















