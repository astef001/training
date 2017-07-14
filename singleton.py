import unittest


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs, **kwargs)
        cls._has_instance = None

    def __call__(cls, *args, **kwargs):
        if cls._has_instance is None:
            cls._has_instance=super().__call__(*args, **kwargs)
        return cls._has_instance


class TestClass(metaclass=Singleton):
   def __init__(self, var_one, var_two):
        self.var_one = var_one
        self.var_two = var_two


class TestSingleton(unittest.TestCase):
    def test_simple_singleton(self):
        a=TestClass(1,2)
        b=TestClass(3,4)
        self.assertEqual((a.var_one, a.var_two),(b.var_one, b.var_two))
        self.assertEqual(a,b)
