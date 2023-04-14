'''
реализовать метакласс. позволяющий создавать
всегда один и тот же объект класса (см. урок)
'''


class Sample(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class FromSample(metaclass=Sample):
    pass


object_one = FromSample()
object_two = FromSample()

if id(object_one) == id(object_two):
    print("Созданы одинаковые объекты класса")
else:
    print("созданы разные объекты класса")