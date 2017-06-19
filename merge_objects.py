import unittest


def merge(obj_a, obj_b):
    if type(obj_a) != type(obj_b):
        return obj_a, obj_b
    if isinstance(obj_a, (set, frozenset)):
        return set(obj_a | obj_b)
    if isinstance(obj_a, dict):
        result = {}
        for k in (list(obj_a.keys())+list(obj_b.keys())):
                result[k] = merge(obj_a[k], obj_b[k])
        return result
    return obj_a + obj_b


def main(obj_a, obj_b):
    obj_result = {}
    obj_result.update(obj_a)
    for k, v in obj_b.items():
        if k in obj_result.keys():
            obj_result[k] = merge(obj_result[k], v)
        else:
            obj_result[k] = v
    return obj_result


class TestMerge(unittest.TestCase):
    __obj_a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]),
               'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}

    __obj_b = {'x': [4, 5, 6],
               'y': 4,
               'z': set([4, 2, 3]),
               'w': 'asdf',
               't': {'a': [3, 2]},
               'm': "wer"}

    __result = {'x': [1, 2, 3, 4, 5, 6],
                'y': 5,
                'z': set([1, 2, 3, 4]),
                'w': 'qweqweasdf',
                't': {'a': [1, 2, 3, 2]},
                'm': ([1], "wer")}

    def test_void_params(self):
        self.assertEqual(main({}, {}), {})

    def test_one_void_param(self):
        self.assertEqual(main(self.__obj_a, {}), self.__obj_a)

    def test_merge(self):
        self.assertEqual(main(self.__obj_a, self.__obj_b), self.__result)
