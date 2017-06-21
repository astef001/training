import unittest


def flatten_list(list_a, max_depth):
    list_b = []
    if max_depth == 0:
        return list_a
    for x in list_a:
        if isinstance(x, list):
            list_b.extend(x)
        else:
            list_b.append(x)
    return flatten_list(list_b, max_depth-1)


def flatten(list_a, list_b, max_depth):
    list_a_flatten = flatten_list(list_a, max_depth)
    list_b_flatten = flatten_list(list_b, max_depth)
    list_a_flatten.extend(list_b_flatten)
    return list_a_flatten


class TestFlatten(unittest.TestCase):
    def test_depth_one(self):
        list_a = [1, 2, [3, [4, 5, 6]]]
        list_b = [1, [[[2, 3], [4, 5]], 8]]
        result_list_a = [1, 2, 3, [4, 5, 6]]
        result_list_b = [1, [[2, 3], [4, 5]], 8]
        result_list_a.extend(result_list_b)
        self.assertEqual(flatten(list_a, list_b, 1), result_list_a)

    def test_depth_two(self):
        list_a = [1, 2, [3, [4, 5, 6]]]
        list_b = [1, [[[2, 3], [4, 5]], 8]]
        result_list_a = [1, 2, 3, 4, 5, 6]
        result_list_b = [1, [2, 3], [4, 5], 8]
        result_list_a.extend(result_list_b)
        self.assertEqual(flatten(list_a, list_b, 2), result_list_a)

    def test_depth_three(self):
        list_a = [1, 2, [3, [4, 5, 6]]]
        list_b = [1, [[[2, 3], [4, 5]], 8]]
        result_list_a = [1, 2, 3, 4, 5, 6]
        result_list_b = [1, 2, 3, 4, 5, 8]
        result_list_a.extend(result_list_b)
        self.assertEqual(flatten(list_a, list_b, 3), result_list_a)

    def test_empty_list(self):
        self.assertEqual(flatten([], [], 3), [])

if __name__ == '__main__':
    unittest.main()
