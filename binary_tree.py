import unittest


class BinaryTree(object):
    def __init__(self, binary_tree):
        self.key = binary_tree[0]
        self.left_sub_tree = binary_tree[1]
        self.right_sub_tree = binary_tree[2]
        self.stack = [(self.key,
                       self.left_sub_tree,
                       self.right_sub_tree)]

    def __iter__(self):
        for x in self.stack:
            if x is not None:
                self.stack.extend([x[1], x[2]])
                yield x[0]
            del x


class TestBinaryTree(unittest.TestCase):
    def test_empty_tree(self):
        tree = BinaryTree((None, None, None))
        res = list(x for x in tree)
        self.assertEqual(res, [None])

    def test_simple_tree(self):
        tree = BinaryTree(('b', ('a', None, None),
                          ('z', ('c', None, None),
                          ('zz', None, None))))
        res = list(x for x in tree)
        self.assertEqual(res, ['b', 'a', 'z', 'c', 'zz'])
