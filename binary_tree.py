from collections import deque
import unittest


class BinaryTree(object):
    def __init__(self, binary_tree):
        self.key = binary_tree[0]
        self.left_sub_tree = binary_tree[1]
        self.right_sub_tree = binary_tree[2]

    def __iter__(self):
        self.stack = deque([(self.key,
                             self.left_sub_tree,
                             self.right_sub_tree)])
        return self

    def __next__(self):
        while len(self.stack):
            current = self.stack.popleft()
            if current is not None:
                self.stack.extend([current[1], current[2]])
                return current[0]
        raise StopIteration


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
