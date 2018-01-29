# 面向对象


class Student(object):

#这里属性带有__的属于private(私有的),外部是不能访问的(直接.属性就没有) 一个'_'是可以访问的,如果项目中出现了,作者表示的意思是尽量不要访问
    def __init__(self,name,height):
        self._name = name
        self.__height = height

    # def print_height(self):
    #     print('%s:%s' % (self.name,self.height))

    def get_grade(self):
        if self.__height > 90:
            return 'A'
        else:
            return 'B'

    def set_height(self):
        if  0 < self.__height < 200 :
            return self.__height
        else:
            return ValueError('input eroor 0 < height < 200')
    def set_name(self):
        print('%s' % self._name)



firstStudents = Student('lixueyuan',0)
#这里接收对象中返回的height对比的结果
fistResult = firstStudents.get_grade()

secondResult = firstStudents.set_height()
if type(secondResult) == ValueError:
    print('ValueError')

#这里表面修改了_name的属性,但实际上_name的值是没有发生改变的
firstStudents._name = 'haha'
print(firstStudents.set_name())
print('I want to access' + firstStudents._name)
#打印结果
print('This is first result ' + fistResult)


#-------这里我需要用到继承-----(上面我创建了一个student的class,那么学生分为good 或者 bad)那么我现在来创建一个goodStudent
class GoodStudent(Student):
    def __len__(self):
        return 100
    pass

#创建一个好学生的实例
firstGoodStudent = GoodStudent('张三',123)
print(firstGoodStudent.set_name())

#----使用type()----判断系统自带的类型.例如int string 或则 ValueError等等这样的类型我们可以直接用type()
#那么如果判断自己定义的class或者是通过集成创建的自定义类型我们就可以使用另一个函数来做判断
 #isinstance()
isStudent = isinstance(firstGoodStudent,GoodStudent)
print(isStudent)

#这里是一个新的函数
#dir()它可以直接获取到一个对象的所有属性和方法
#例如
getInfo = dir(firstGoodStudent)
#这里例如我要访问getInfo的长度我可以直接使用__len__去访问,如果你在自定义的class中也想使用这个函数,那么可以直接写一个(见48行)
print(firstGoodStudent.__len__())

#还有很多有用的函数例如:
#  lower()返回小写的字符串,
   #hasattr()判断 对象中是否有某属性,返回bool
      #setattr()设置 对象属性的值
         #getattr 获取 对象属性的值
#以上函数如果不存在就会抛出异常AttributeError的错误:
#下面这个用法,如果属性不存在,就给默认值,避免崩溃
#getattr(obj,'a',123)如果obj中不存在a属性,那么我返回123




