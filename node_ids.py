import unittest
from os import path

def sort(string):
    lst = string.split("/")
    return lst[0], int(lst[1])


def merge_sets(file):
    res = []
    if not path.exists(file):
        return "Specified file does not exist"
    with open(file, "r") as f:
        a = f.readline().strip()
        while a:
            res = list(set().union(res, a.split(", ")))
            a = f.readline().strip()
    return ", ".join(sorted(res, key=lambda x: sort(x)))


class TestNodeIds(unittest.TestCase):
    def test_empty_file(self):
        self.assertEqual(merge_sets("empty_file"), "")

    def test_no_file(self):
        self.assertEqual(merge_sets("no_file"), "Specified file does not exist")

    def test_simple_set(self):
        result = "a/1, a/2, a/3, a/4, a/5, a/126, a/127, a/128, a/129, b/65, b/66, b/100, c/1, c/2, c/3, c/10, c/42, d/1"
        self.assertEqual(merge_sets("input.in"), result)
