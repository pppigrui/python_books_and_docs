Python中有大量类似`__doc__`这种以双下划线开头和结尾的特殊成员及“魔法方法”，它们有着非常重要的地位和作用，也是Python语言独具特色的语法之一！

比如：

```python
__init__ :      构造函数，在生成对象时调用
__del__ :       析构函数，释放对象时使用
__repr__ :      打印，转换
__setitem__ :   按照索引赋值
__getitem__:    按照索引获取值
__len__:        获得长度
__cmp__:        比较运算
__call__:       调用
__add__:        加运算
__sub__:        减运算
__mul__:        乘运算
__div__:        除运算
__mod__:        求余运算
__pow__:        幂
```

需要注意的是，这些成员里面有些是方法，调用时要加括号，有些是属性，调用时不需要加括号（废话！）。下面将一些常用的介绍一下，：

### 1. `__doc__`

说明性文档和信息。Python自建，无需自定义。

```python
class Foo:
    """ 描述类信息，可被自动收集 """

    def func(self):
        pass

# 打印类的说明文档 
print(Foo.__doc__)
```

### 2. `__init__()`

实例化方法，通过类创建实例时，自动触发执行。

```python
class Foo:

    def __init__(self, name):
        self.name = name
        self.age = 18

obj = Foo(jack') # 自动执行类中的 __init__ 方法
```

### 3. `__module__` 和 `__class__`

`__module__` 表示当前操作的对象在属于哪个模块。

`__class__` 表示当前操作的对象属于哪个类。

这两者也是Python内建，无需自定义。

```
class Foo:
    pass

obj = Foo()
print(obj.__module__)
print(obj.__class__)

------------
运行结果：
__main__
<class '__main__.Foo'>
```

### 4. `__del__()`

析构方法，当对象在内存中被释放时，自动触发此方法。

注：此方法一般无须自定义，因为Python自带内存分配和释放机制，除非你需要在释放的时候指定做一些动作。析构函数的调用是由解释器在进行垃圾回收时自动触发执行的。

```python
class Foo:

    def __del__(self):
        print("我被回收了！")


obj = Foo()

del obj
```

### 5. `__call__()`

如果为一个类编写了该方法，那么在该类的实例后面加括号，可会调用这个方法。

注：构造方法的执行是由类加括号执行的，即：`对象 = 类名()`，而对于`__call__()` 方法，是由对象后加括号触发的，即：`对象()` 或者 `类()()`

```python
class Foo:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):

        print('__call__')


obj = Foo()     # 执行 __init__
obj()       # 执行 __call__
```

那么，怎么判断一个对象是否可以被执行呢？能被执行的对象就是一个Callable对象，可以用Python内建的callable()函数进行测试，我们在前面的章节已经介绍过这个函数了。

```python
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False
>>> callable(int)
True
>>> callable(str)
True
```

### 6. `__dict__`

列出类或对象中的所有成员！非常重要和有用的一个属性，Python自建，无需用户自己定义。

```python
class Province:
    country = 'China'
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print（'func'）

# 获取类的成员
print(Province.__dict__)

# 获取 对象obj1 的成员 
obj1 = Province('HeBei',10000)
print(obj1.__dict__)

# 获取 对象obj2 的成员 
obj2 = Province('HeNan', 3888)
print(obj2.__dict__)
```

### 7. `__str__()`

如果一个类中定义了`__str__()`方法，那么在打印对象时，默认输出该方法的返回值。这也是一个非常重要的方法，需要用户自己定义。　

下面的类，没有定义`__str__()`方法，打印结果是：`<__main__.Foo object at 0x000000000210A358>`

```python
class Foo:
    pass

obj = Foo()
print(obj)
```

定义了`__str__()`方法后，打印结果是：'jack'。

```python
class Foo:

    def __str__(self):
        return 'jack'

obj = Foo()
print(obj)
```

### 8、`__getitem__()`、`__setitem__()`、`__delitem__()`

取值、赋值、删除这“三剑客”的套路，在Python中，我们已经见过很多次了，比如前面的`@property`装饰器。

Python中，标识符后面加圆括号，通常代表执行或调用方法的意思。而在标识符后面加中括号[]，通常代表取值的意思。Python设计了`__getitem__()`、`__setitem__()`、`__delitem__()`这三个特殊成员，用于执行与中括号有关的动作。它们分别表示取值、赋值、删除数据。

也就是如下的操作：

```python
a = 标识符[]　： 　　执行__getitem__方法
标识符[] = a  ： 　　执行__setitem__方法
del 标识符[]　： 　　执行__delitem__方法
```

如果有一个类同时定义了这三个魔法方法，那么这个类的实例的行为看起来就像一个字典一样，如下例所示：

```python
class Foo:

    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)

    def __delitem__(self, key):
        print('__delitem__',key)


obj = Foo()

result = obj['k1']      # 自动触发执行 __getitem__
obj['k2'] = 'jack'      # 自动触发执行 __setitem__
del obj['k1']             # 自动触发执行 __delitem__
```

### 9. `__iter__()`

这是迭代器方法！列表、字典、元组之所以可以进行for循环，是因为其内部定义了 `__iter__()`这个方法。如果用户想让自定义的类的对象可以被迭代，那么就需要在类中定义这个方法，并且让该方法的返回值是一个可迭代的对象。当在代码中利用for循环遍历对象时，就会调用类的这个`__iter__()`方法。

普通的类：

```python
class Foo:
    pass


obj = Foo()

for i in obj:
    print(i)

# 报错：TypeError: 'Foo' object is not iterable<br># 原因是Foo对象不可迭代
```

添加一个`__iter__()`，但什么都不返回：

```python
class Foo:

    def __iter__(self):
        pass

obj = Foo()

for i in obj:
    print(i)

# 报错：TypeError: iter() returned non-iterator of type 'NoneType'

#原因是 __iter__方法没有返回一个可迭代的对象
```

返回一个个迭代对象：

```python
class Foo:

    def __init__(self, sq):
        self.sq = sq

    def __iter__(self):
        return iter(self.sq)

obj = Foo([11,22,33,44])

for i in obj:
    print(i)

# 这下没问题了！
```

最好的方法是使用生成器：

```python
class Foo:
    def __init__(self):
        pass

    def __iter__(self):
        yield 1
        yield 2
        yield 3

obj = Foo()
for i in obj:
    print(i)
```

### 10、`__len__()`

在Python中，如果你调用内置的len()函数试图获取一个对象的长度，在后台，其实是去调用该对象的`__len__()`方法，所以，下面的代码是等价的：

```python
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

Python的list、dict、str等内置数据类型都实现了该方法，但是你自定义的类要实现len方法需要好好设计。

### 11. `__repr__()`

这个方法的作用和`__str__()`很像，两者的区别是`__str__()`返回用户看到的字符串，而`__repr__()`返回程序开发者看到的字符串，也就是说，`__repr__()`是为调试服务的。通常两者代码一样。

```python
class Foo:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "this is %s" % self.name

    __repr__ = __str__
```

### 12. `__add__`: 加运算 `__sub__`: 减运算 `__mul__`: 乘运算 `__div__`: 除运算 `__mod__`: 求余运算 `__pow__`: 幂运算

这些都是算术运算方法，需要你自己为类设计具体运算代码。有些Python内置数据类型，比如int就带有这些方法。Python支持运算符的重载，也就是重写。

```python
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
```

### 13. `__author__`

`__author__`代表作者信息！类似的特殊成员还有很多，就不罗列了。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
a test module
"""
__author__ = "Jack"

def show():
    print(__author__)

show()
```

### 14. `__slots__`

Python作为一种动态语言，可以在类定义完成和实例化后，给类或者对象继续添加随意个数或者任意类型的变量或方法，这是动态语言的特性。例如：

```python
def print_doc(self):
    print("haha")

class Foo:
    pass

obj1 = Foo()
obj2 = Foo()
# 动态添加实例变量
obj1.name = "jack"
obj2.age = 18
# 动态的给类添加实例方法
Foo.show = print_doc
obj1.show()
obj2.show()
```

但是！如果我想限制实例可以添加的变量怎么办？可以使`__slots__`限制实例的变量，比如，只允许Foo的实例添加name和age属性。

```python
def print_doc(self):
    print("haha")

class Foo:
    __slots__ = ("name", "age")
    pass


obj1 = Foo()
obj2 = Foo()
# 动态添加实例变量
obj1.name = "jack"
obj2.age = 18
obj1.sex = "male"       # 这一句会弹出错误
# 但是无法限制给类添加方法
Foo.show = print_doc
obj1.show()
obj2.show()
```

由于'sex'不在`__slots__`的列表中，所以不能绑定sex属性，试图绑定sex将得到AttributeError的错误。

```python
Traceback (most recent call last):
  File "F:/Python/pycharm/201705/1.py", line 14, in <module>
    obj1.sex = "male"
AttributeError: 'Foo' object has no attribute 'sex'
```

需要提醒的是，`__slots__`定义的属性仅对当前类的实例起作用，对继承了它的子类是不起作用的。想想也是这个道理，如果你继承一个父类，却莫名其妙发现有些变量无法定义，那不是大问题么？如果非要子类也被限制，除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。