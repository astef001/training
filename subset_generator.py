import unittest


def subset_generator(elem):
    if len(elem) > 0:
        head = set([elem.pop()])
        for i in subset_generator(elem):
            yield head.union(i)
            yield i
    else:
        yield set()


class TestSubset(unittest.TestCase):
    def test_empty_set(self):
        self.assertEqual([x for x in subset_generator(set())], [set()])

    def test_simple_set(self):
        self.assertEqual([x for x in subset_generator(set([1, 2, 3]))],
                         [set([1, 2, 3]), set([2, 3]), set([1, 3]),
                          set([3]), set([1, 2]), set([2]), set([1]), set([])])
