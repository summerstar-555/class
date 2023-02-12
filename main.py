# 新建一个类
# 类范围比较大，对象是类的实例化
"""
class Student:
    name = None
    gender = None
    age = None

    # 方法即是写在类内部的函数
    def say_hello(self, msg):  # 在创建方法时self必须存在
        print(f"大家好，我叫{self.name},今年{self.age}岁,{msg}")
"""

# 使用类
"""
stu1 = Student()  # 使用类的格式为：变量名 = 类名称（）
stu1.name = "张三"
stu1.gender = "男"
stu1.age = 19
stu1.say_hello("很高兴认识诸位！")  # 在传参的时候可以忽略self这个形参
"""

# 构造方法 - __init__会自动运行
"""
class Student:
    def __init__(self, name1, gender1, age1):  # 需要加上形参;类似于函数，接受参数
        self.name = name1   # 在变量名前加上self.，后面的变量名是参数名。前者是一个函数内构建的变量名，后者是参数名
        self.gender = gender1      # 这里直接就声明变量并初始化了
        self.age = age1
        print("这个方法会自动运行")


stu1 = Student("张三", "男", 19)
print(stu1.name)
print(stu1.gender)
print(stu1.age)
"""

# 本打算练习__lt__魔术方法，但发现这个的作用其实并不大
"""
class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


stu1 = Student("小明", 16, "广东汕头")
stu2 = Student("小红", 12, "广东汕头")
print(stu1.age > stu2.age)
"""

# 案例 --私有变量/方法的意义：让用户使用不到，但是又必须存在
"""
class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phe = Phone()
phe.call_by_5g()
"""

# 继承
"""
class OldPho:
    IMEI = None  # 序列号
    producer = None  # 厂商

    def call_by_4g(self):
        print("4g通话")


class NewPho(OldPho):  # 继承旧手机的东西 / 单继承
    face_id = True

    def call_by_5g(self):   # 在原有的方法上进行修改
        print("2022最新5g通话")
"""

# 多继承
"""
class OldPho:
    IMEI = None  # 序列号
    producer = None  # 厂商

    def call_by_4g(self):
        print("4g通话")
        
        
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")
        

class NewPho(OldPho, NFCReader):  # 继承两个父类，可以使用其中的方法和变量
    pass    # 语法要求必须写什么上去。pass用来补上，没有实际用处
"""

# 在使用多个函数，而多个函数的形参一致时，这种场景就很适合类
'''
class DownloadPicture:
    def __init__(self, tag: str = None,pic_count: int = 0,  share_obj = None):
        """
        :param tag: 用户想要搜索的图片标签
        :param pic_count: 想要下载的图片数量
        :param share_obj: 共享对象，用于多进程共享内存
        """
        self.tag = tag
        self.share_obj = share_obj
        self.pic_count = pic_count
    def print_tag(self):
        print(self.tag)

test1 = DownloadPicture('4k')
test1.print_tag()
'''

# Python 中允许使用类名直接调用实例方法，但必须手动为该方法的第一个 self 参数传递参数，这种调用方法的方式被称为“非绑定方法”。
"""
class CLanguage:
    def info(self):
        print(self,"正在学 Python")
#通过类名直接调用实例方法
CLanguage.info("zhangsan")
"""

# 使用类时让它自动调用方法，利用__init__调用类就自动运行的特点
'''
class Test:

    def __init__(self, arg1):
        self.a = arg1
        self.count()        # 可以在init这个函数内调用方法
    def count(self):
        print(self.a + 1)

test = Test(1)
'''

# 单继承下super只是用来调用父类的方法
"""
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m     # 将m的值传入后再将n加上
        # 此时self是子类，子类的值就会受到影响


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))        # 目的就是看谁调用了add方法
        # 这里只是调用父类的方法，不会触发init方法
        super().add(m)    # 调用父类方法，这里可以把super理解为父类自身
        self.n += 3

# super().add(m) 调用父类方法 def add(self, m) 时, 此时父类中 self 并不是父类的实例而是子类的实例, 所以 b.add(2) 之后的结果是5而不是4

b = B()
b.add(2)
print(b.n)
"""

# 仅用类的方法也不会调用init方法
"""
class A:
    def __init__(self):
        print('init')

    def add(self, m):
        print(self)
        print('add', m)


A.add(None, 5)
"""


# 多继承
"""
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5


d = D()
d.add(2)
print(d.n)
"""