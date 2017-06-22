import unittest


def merge(obj_a, obj_b):
    if obj_a is None or obj_b is None:
        return obj_a or obj_b
    if type(obj_a) != type(obj_b):
        return obj_a, obj_b
    if isinstance(obj_a, (set, frozenset)):
        return obj_a | obj_b
    if isinstance(obj_a, dict):
        return merge_dict(obj_a, obj_b)
    if isinstance(obj_a, str):
        return "{obj_a}{obj_b}".format(obj_a=obj_a, obj_b=obj_b)
    return obj_a + obj_b


def merge_dict(obj_a, obj_b):
    result = {}
    for k in list(obj_a) + list(obj_b):
        result[k] = merge(obj_a.get(k), obj_b.get(k))
    return result


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.obj_a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]),
                        'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}

        self.obj_b = {'x': [4, 5, 6],
                        'y': 4,
                        'z': set([4, 2, 3]),
                        'w': 'asdf',
                        't': {'a': [3, 2]},
                        'm': "wer",
                        'different_key': "a value"}

        self.result = {'x': [1, 2, 3, 4, 5, 6],
                         'y': 5,
                         'z': set([1, 2, 3, 4]),
                         'w': 'qweqweasdf',
                         't': {'a': [1, 2, 3, 2]},
                         'm': ([1], "wer"),
                         'different_key': "a value"}

    def test_void_params(self):
        self.assertEqual(merge_dict({}, {}), {})

    def test_one_empty_param(self):
        self.assertEqual(merge_dict(self.obj_a, {}), self.obj_a)

    def test_merge(self):
        self.assertEqual(merge_dict(self.obj_a, self.obj_b), self.result)
