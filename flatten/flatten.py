import unittest


def flatten_list(list_a):
    list_b = []
    for x in list_a:
        if isinstance(x, list):
            list_b.extend(x)
        else:
            list_b.append(x)
    return list_b


def flatten(list_a, list_b, max_depth):
    list_a_flatten = []
    list_b_flatten = []
    if max_depth == 0:
        return list_a, list_b
    list_a_flatten = flatten_list(list_a)
    list_b_flatten = flatten_list(list_b)
    return flatten(list_a_flatten, list_b_flatten, max_depth-1)


class TestFlatten(unittest.TestCase):
    def test_depth_one(self):
        list_a = [1, 2, [3, [4, 5, 6]]]
        list_b = [1, [[[2, 3], [4, 5]], 8]]
        result_list_a = [1, 2, 3, [4, 5, 6]]
        result_list_b = [1, [[2, 3], [4, 5]], 8]
        self.assertEqual(flatten(list_a, list_b, 1),
                         (result_list_a, result_list_b))

    def test_depth_two(self):
        list_a = [1, 2, [3, [4, 5, 6]]]
        list_b = [1, [[[2, 3], [4, 5]], 8]]
        result_list_a = [1, 2, 3, 4, 5, 6]
        result_list_b = [1, [2, 3], [4, 5], 8]
        self.assertEqual(flatten(list_a, list_b, 2),
                         (result_list_a, result_list_b))

    def test_depth_three(self):
        list_a = [1, 2, [3, [4, 5, 6]]]
        list_b = [1, [[[2, 3], [4, 5]], 8]]
        result_list_a = [1, 2, 3, 4, 5, 6]
        result_list_b = [1, 2, 3, 4, 5, 8]
        self.assertEqual(flatten(list_a, list_b, 3),
                         (result_list_a, result_list_b))

    def test_empty_list(self):
        self.assertEqual(flatten([], [], 3), ([], []))

if __name__ == '__main__':
    unittest.main()
