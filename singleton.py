import unittest


class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._has_instance = None

    def __call__(cls, *args, **kwargs):
        if cls._has_instance is None:
            cls._has_instance=super().__call__(*args, **kwargs)
        return cls._has_instance


class TestClass(metaclass=Singleton):
    pass


class TestSingleton(unittest.TestCase):
    def test_simple_singleton(self):
        self.assertEqual(TestClass(), TestClass())
