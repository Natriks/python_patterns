class SingletonMeta(type):

    __created_objects = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__created_objects:
            singletone_object = super().__call__(*args, **kwargs)
            cls.__created_objects[cls] = singletone_object
        return cls.__created_objects[cls]


class Singleton(metaclass=SingletonMeta):

    a = 0
    b = 0

    def summ(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b


s1 = Singleton()
s1.summ(2, 2)

s2 = Singleton()
s2.summ(3, 3)


if id(s1) == id(s2):
    print("Объект один.")
else:
    print("Объекта 2.")