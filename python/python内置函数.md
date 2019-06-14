你会不会有些好奇Python为什么可以直接使用一些内建函数，而不用显式的导入它们？比如 str()、int()、dir()、id()、type()，max()，min()，len()等，许多许多非常好用，快捷方便的函数。

因为这些函数都是一个叫做`builtins`模块中定义的函数，而`builtins`模块默认在Python环境启动的时候就自动导入，所以你可以直接使用这些函数。

我们可以在IDLE里查证一番：

```python
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}

>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

globals()函数可以查看当前状态下，全局变量有哪些，其中最后一个`'__builtins__': <module 'builtins' (built-in)>`就是我们说的builtins模块。再使用dir()函数查看它的成员属性，巴拉巴拉一大堆。

builtins模块里有接近80个内置函数，60多个内置异常，还有几个内置常数，特殊名称以及模块相关的属性。

Python通过这个近80个内置函数，为我们提供了丰富、强大、高效、快速的解决方案，大多数时候，我们根本不需要导入第三方库，甚至标准库都不需要。不需要自己造轮子，简简单单地使用Python的内置函数就好了！

| 内置函数      |             |              |            |                |
| :------------ | :---------- | :----------- | :--------- | :------------- |
| abs()         | dict()      | help()       | min()      | setattr()      |
| all()         | dir()       | hex()        | next()     | slice()        |
| any()         | divmod()    | id()         | object()   | sorted()       |
| ascii()       | enumerate() | input()      | oct()      | staticmethod() |
| bin()         | eval()      | int()        | open()     | str()          |
| bool()        | exec()      | isinstance() | ord()      | sum()          |
| bytearray()   | filter()    | issubclass() | pow()      | super()        |
| bytes()       | float()     | iter()       | print()    | tuple()        |
| callable()    | format()    | len()        | property() | type()         |
| chr()         | frozenset() | list()       | range()    | vars()         |
| classmethod() | getattr()   | locals()     | repr()     | zip()          |
| compile()     | globals()   | map()        | reversed() | `__import__()` |
| complex()     | hasattr()   | max()        | round()    |                |
| delattr()     | hash()      | memoryview() | set()      |                |

由于Python内置函数的强大、丰富、方便，在此特地用单独的章节进行介绍。因为内容编排的原因，小80个条目中有一部分在前面已经介绍过，有一部分留待后面介绍。

### abs()：

绝对值函数。如abs（-1）= 1

```python
>>> abs(-10)
10
>>> f = abs
>>> f(-1)
1
>>> abs=id
>>> abs(1)
1869788224
```

以abs()函数为例，展示两个特性。一是，内置函数是可以被赋值给其他变量的，同样也可以将其他对象赋值给内置函数，这时就完全变了。所以，内置函数不是Python关键字，要注意对它们的保护，不要使用和内置函数重名的变量名，这会让代码混乱，容易发生难以排查的错误。

### all()

接收一个可迭代对象，如果对象里的所有元素的bool运算值都是True，那么返回True，否则False。不要小瞧了这个函数，用好了，有化腐朽为神奇的特效。

```python
>>> all([1,1,1])
True
>>> all([1,1,0])
False
```

### any()

接收一个可迭代对象，如果迭代对象里有一个元素的bool运算值是True，那么返回True，否则False。与all()是一对兄弟。

```
>>> any([0,0,1])
True
>>> any([0,0,0])
False
```

### ascii()

调用对象的`__repr__()`方法，获得该方法的返回值。`__repr__()`方法是由对象所属类型实现的方法。不可以简单地理解为print或echo。

```python
>>>s = “haha”
>>> ascii(s)
"'haha'"
>>> a = [1,2,3]
>>> ascii(a)
'[1, 2, 3]'
```

### bin()、oct()、hex()

三个函数是将十进制数分别转换为2/8/16进制。

```
>>> i = 10
>>> bin(i)
'0b1010'
>>> oct(i)
'0o12'
>>> hex(i)
'0xa'
```

### bool()

测试一个对象或表达式的执行结果是True还是False。这个在布尔数据类型章节中已经很详细的介绍过了。Ps:实际上bool是一个类，不是函数，bool()的返回值是一个布尔类型的实例。builtins中的很多函数，其实都是类，比如bytes()，str()等等。只是因为称呼的习惯，我们叫它函数，严格意义上说，这是不对的，大家心里有数就可以，后面就不再重复说明。

```python
>>> bool(1==2)
False
>>> bool(abs(-1))
True
>>> bool(None)
False
```

### bytearray

实例化一个bytearray类型的对象。参数可以是字符串、整数或者可迭代对象。bytearray是Python内置的一种可变的序列数据类型，具有大多数bytes类型同样的方法。

当参数是字符串的时候，需要指定编码类型。

当参数是整数时，会创建以该整数为长度，包含同样个数空的bytes对象的数组。

当参数是个可迭代的对象时，该对象必须是一个取值范围`0 <= x < 256`的整数序列。

```python
>>> a = bytearray("asdff",encoding='utf-8')
>>> b = bytearray(10)
>>> b
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> d = bytearray([1,2,3])
>>> d
bytearray(b'\x01\x02\x03')
>>> d = bytearray([1,2,300])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d = bytearray([1,2,300])
ValueError: byte must be in range(0, 256)
```

### bytes()

将对象转换成字节类型。例如：`s = '张三';m = bytes(s,encoding='utf-8')`

```python
>>> i=2
>>> bytes(i)
b'\x00\x00'
>>> s = 'haha'
>>> bytes(s)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    bytes(s)
TypeError: string argument without an encoding
>>> bytes(s, encoding="utf-8")
b'haha'
>>> bytes(s, encoding="GBK")
b'haha'
```

### str()

将对象转换成字符串类型，同样也可以指定编码方式。例如：`str(bytes对象，encoding='utf-8')`

```python
>>> i =  2
>>> str(i)
'2'
>>> b = b"haha"
>>> str(b)      # 注意！
"b'haha'"
>>> str(b,encoding="gb2312")
'haha'
>>> str([1,2,3,])
'[1, 2, 3]'
```

Bytes和string之间的互相转换，更多使用的是encode()和decode()方法。

### callable()

判断对象是否可以被调用。如果某个对象具有`__call__`方法，那它就能被调用。 例如，`def f1(): pass`,那么`callable(f1)`返回True。

```python
>>> def f1():
    pass
>>> callable(f1)
True
>>> a = "123"
>>> callable(a)
False
>>> class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age        
>>> f_obj = Foo("jack",20)
>>> callable(f_obj)
False
>>> callable(Foo)
True
```

### chr()

返回某个十进制数对应的ASCII字符，例如：`chr(99) = ‘c’`。它可以配合`random.randint(65，91)`随机方法，生成随机字符，用于生产随机验证码。

```python
import random
for i in range(10):
    a = random.randint(65,91)
    c = chr(a)
    print(c)
```

### ord()

与chr()相反，返回某个ASCII字符对应的十进制数，例如，`ord('A') = 65`

```python
>>> ord("A")
65
>>> ord("\n")
10
```

### classmethod()、staticmethod()和property()

类机制中，用于生成类方法、静态方法和属性的函数。在面向对象章节会有详细介绍。

### compile()

将字符串编译成Python能识别或执行的代码。 也可以将文件读成字符串再编译。

```python
>>> s  = "print('helloworld')"
>>> r = compile(s,"<string>","exec")
>>> r
<code object <module> at 0x000001B23E6BE660, file "<string>", line 1>
>>> r()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    r()
TypeError: 'code' object is not callable
>>> exec(r)
helloworld
>>> eval(r)
helloworld
```

### complex()

通过数字或字符串生成复数类型对象。

```python
>>> complex(1,2)
(1+2j)
>>> complex('3+4j')
(3+4j)
>>> complex('3 +4j')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    complex('3 +4j')
ValueError: complex() arg is a malformed string
```

使用字符串的时候，+号左右不能有空白。

### delattr()、setattr()、getattr()、hasattr()

类机制中，分别用来删除、设置、获取和判断属性。后面会有详解。

### dir()

显示对象所有的属性和方法。最棒的辅助函数之一！

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'builtins', 'r', 's']

>>> dir([1,2,])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### int()、float()、list()、dict()、set()、tuple()

与bool()、str()、bytes()一样，它们都是实例化对应数据类型的类。

### divmod()

除法，同时返回商和余数的元组。

```python
>>> divmod(10,3)
(3, 1)
>>> divmod(11,4)
(2, 3)
```

### enumerate()

枚举函数，在迭代对象的时候，额外提供一个序列号的输出。注意：`enumerate(li,1)`中的1表示从1开始序号，默认从0开始。注意，第二个参数才是你想要的序号开始，不是第一个参数。

```python
dic = {
    "k1":"v1",
    "k2":"v2",
    "k3":"v3",
}

for i, key in enumerate(dic, 1):
    print(i,"\t",key)
```

通常用于对那些无法提供序号的迭代对象使用。但对于字典，依然是无序的。

### eval()

将字符串直接解读并执行。例如：`s = "6*8"`，s是一个字符串，`d = eval(s)`， d的结果是48。

### exec()

执行字符串或compile方法编译过的字符串，没有返回值。

```python
>>> exec("print('this is a test')")
this is a test
>>> eval("print('this is a test')")
this is a test
```

### format()

执行format()，其实就是调用该对象所属类的`__format__`方法。类似print功能。

```python
>>> format("324324")
'324324'
>>> format([1,2,3])
'[1, 2, 3]'
```

### frozenset()

返回一个不能增加和修改的集合类型对象。

```python
>>> a
[1, 2, 3]
>>> b = frozenset(a)
>>> b
frozenset({1, 2, 3})
>>> dir(b)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
```

### globals()

列出当前环境下所有的全局变量。注意要与global关键字区分！在本节的开始，我们就已经展示了它的用法。

### hash()

为不可变对象，例如字符串生成哈希值的函数！

```python
>>> hash("i am jack")
5602200374213231465
>>> hash(1)
1
>>> hash(100000)
100000
>>> hash([1,2,3,])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    hash([1,2,3,])
TypeError: unhashable type: 'list'
>>> hash((1,2,3))
2528502973977326415
```

### help()

返回对象的帮助文档。谁用谁知道！

```python
>>> a = [1,2,3]
>>> help(a)
Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

### id()

返回对象的内存地址,常用来查看变量引用的变化，对象是否相同等。常用功能之一！

```python
>>> id(0)
1456845856
>>> id(True)
1456365792
>>> a = "Python"
>>> id(a)
37116704
```

### input()

接收用户输入，返回一个输入的字符串。

```python
>>> a = input("Please input a number:  ")
Please input a number:  100
>>> a
'100'
>>> type(a)
<class 'str'>
```

### isinstance()

判断一个对象是否是某个类的实例。比type()方法适用面更广。

```python
>>> isinstance("haha", str)
True
>>> isinstance(1, str)
False
```

### issubclass()

issubclass(a，b),判断a是否是b的子类。

```python
>>> class Foo:
    pass
>>> class Goo(Foo):
    pass
>>> issubclass(Goo, Foo)
True
```

### iter()

制造一个迭代器，使其具备next()能力。

```python
>>> lis = [1, 2, 3]
>>> next(lis)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    next(lis)
TypeError: 'list' object is not an iterator
>>> i = iter(lis)
>>> i
<list_iterator object at 0x0000000002B4A128>
>>> next(i)
1
```

### len()

返回对象的长度。不能再常用的函数之一了。

### locals()

返回当前可用的局部变量。

```python
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': '100', 'lis': [1, 2, 3], 'i': <list_iterator object at 0x0000000002B4A128>, 'dic': {'k1': 'v1'}}
```

### max()/min():

返回给定集合里的最大或者最小的元素。可以指定排序的方法！

```python
lst=['abcdhush8','abc9iujtwertwert','abcdjlas','abcdj897h']
a = min(lst,key=len)
print(a)
```

### memoryview(obj)

返回obj的内存视图对象。obj只能是bytes或bytesarray类型。memoryview对象的使用方法如下：

```python
>>> v = memoryview(b'abcefg')
>>> v[1]
98
>>> v[-1]
103
>>> v[1:4]
<memory at 0x7f3ddc9f4350>
>>> bytes(v[1:4])
b'bce'
```

### next()

通过调用迭代器的`__next__()`方法，获取下一个元素。

### object()

该方法不接收任何参数，返回一个没有任何功能的对象。object是Python所有类的基类。

### open()

打开文件的方法。在Python2里，还有一个file()方法，Python3中被废弃了。后面章节会详细介绍open()的用法。

### pow()

幂函数。

```python
>>> pow(3, 2)
9
```

### print()

这个还用介绍吗？

### range()

没错，这是Python内置的函数，前面已经介绍了。

### repr()

调用对象所属类的`__repr__`方法，与print功能类似。

```
>>> s = "hashdfh"
>>> repr(s)
"'hashdfh'"
```

### reversed()

反转，逆序对象

```python
>>> reversed            # reversed本身是个类
<class 'reversed'>
>>> reversed([1,2,3,4,5])   # 获得一个列表反转器
<list_reverseiterator object at 0x0000022E322B5128>
>>> a = reversed([1,2,3,4,5])
>>> a
<list_reverseiterator object at 0x0000022E32359668>
>>> list(a)         # 使用list方法将它转换为一个列表
[5, 4, 3, 2, 1]
```

### round()

四舍五入．

```python
>>> round(1.5)
2
>>> round(1.4)
1
```

### slice()

返回一个切片类型的对象。slice是一个类，一种Python的数据类型。Python将对列表等序列数据类型的切片功能单独拿出来设计了一个slice类，可在某些场合下使用。

```python
>>> s = slice(1, 10, 2)
>>> s
slice(1, 10, 2)
>>> type(s)
<class 'slice'>
>>> lis = [i for i in range(10)]
>>> lis
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> lis[s]          # 注意用法
[1, 3, 5, 7, 9]
```

### sum()

求和．

```python
>>> sum(1,2,3)          # 需要传入一个可迭代的对象
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sum(1,2,3)
TypeError: sum expected at most 2 arguments, got 3
>>> sum([1,2,3])            # 传入一个列表
6
>>> sum({1:1,2:2})          # 突发奇想，作死传入一个字典
3
```

### super()

调用父类。面向对象中类的机制相关。后面介绍。

### type()

显示对象所属的数据类型。常用方法！前面已经展示过。

### vars()

与dir()方法类似，不过dir()方法返回的是key，vars()方法返回key的同时还把value一起打印了。

```python
>>> vars()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': <list_reverseiterator object at 0x0000022E32359668>, 's': 'ha'}
```

## map()

映射函数。使用指定的函数，处理可迭代对象，并将结果保存在一个map对象中，本质上和大数据的mapreduce中的map差不多。

使用格式：`obj = map(func, iterable)`,func是某个函数名，iterable是一个可迭代对象。

细心的同学可能发现了，我除了组合一些成对的或者同类系列的内置函数。还有map()函数，连同后面的filter()、zip()、sorted()和`__import__()`函数都没有介绍。因为这几个内置函数功能非常强大，使用场景非常多，Python非常贴心地帮我们实现并内置了！

```python
li = [1,2,3]
data = map(lambda x :x*100,li)  # 这里直接使用了一个匿名函数

print(type(data))       # 返回值是一个map对象，它是个迭代器。
data = list(data)       # 可以用list方法将map对象中的元素全部生成出来，保存到一个列表里。
print(data)

------------------------------------------------------
运行结果：

<class 'map'>
[100, 200, 300]
```

## filter()

过滤器，用法和map类似。在函数中设定过滤的条件，逐一循环对象中的元素，将返回值为True时的元素留下（注意，不是留下返回值！），形成一个filter类型的迭代器。

```python
def f1(x):
    if x > 3:
        return True
    else:
        return False
li = [1,2,3,4,5]
data = filter(f1,li)
print(type(data))
print(list(data))

----------------------------
运行结果：

<class 'filter'>
[4, 5]
```

或者：

```python
li = [11,22,33,44,55]
result = filter(lambda x: x>33,li)
print(list(result))
----------------------------------------------
结果：

[44, 55]

-------------------------------------------
# 等同于
li = [11,22,33,44,55]
y = [a for a in li if a > 33]
print(y)
```

## zip()

组合对象。将对象逐一配对。

```python
list_1 = [1,2,3]
list_2 = ['a','b','c']
s = zip(list_1,list_2)
print(list(s))
--------------------------------
运行结果：

[(1, 'a'), (2, 'b'), (3, 'c')]
```

组合3个对象：

```
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', "d"]
list_3 = ['aa', 'bb', 'cc', "dd"]
s = zip(list_1, list_2, list_3)
print(list(s))

运行结果：
[(1, 'a', 'aa'), (2, 'b', 'bb'), (3, 'c', 'cc'), (4, 'd', 'dd')]
```

那么如果对象的长度不一致呢？多余的会被抛弃！以最短的为基础！

```python
list_1 = [1,2,3]
list_2 = ['a','b','c',"d"]
s = zip(list_1,list_2)
print(list(s))
--------------------------------
运行结果：
[(1, 'a'), (2, 'b'), (3, 'c')]
```

## sorted()

排序方法。有key和reverse两个重要参数。

基础用法: 直接对序列进行排序

```python
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

**指定排序的关键字**。关键字必须是一个可调用的对象。例如下面的例子，规则是谁的绝对值大，谁就排在后面。

```python
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```

指定按反序排列。下面的例子，首先按忽略大小写的字母顺序排序，然后倒序排列。

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

## `__import__(name)`

这个方法为我们提供了一种通过字符串反射包、库或模块的手段。其中的name是你想要导入的库的名称的字符串。

```python
t = __import__("time")
print(t.time())
```

例子中，利用字符串“time”，导入了实际的time库，并赋值给t变量。这个变量实际就相当于import time的结果。然后使用t.time()进行调用。

在某些场景下，这个方法非常有用。但是很多时候，它也存在安全问题，Python官方不建议经常使用它