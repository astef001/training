import unittest
import os.path


def read_dicts(file):
    dictionaries = []
    with open(file, "r") as f:
        while True:
            temp_dict = {}
            inf = f.readline()
            if not inf:
                break
            inf = inf.rstrip("\n\r")
            inf = str.split(inf, ' ')
            for i in range(0, len(inf)-1, 2):
                temp_dict[format(inf[i])] = inf[i+1]
            dictionaries.append(temp_dict)
    return dictionaries


def sort_dicts(input_file):
    sorting = True
    if not os.path.exists(input_file):
        return False
    dicts = read_dicts(input_file)
    while sorting:
        sorting = False
        for x in range(len(dicts)-1):
            if dicts[x][min(dicts[x])] > dicts[x+1][min(dicts[x+1])]:
                dicts[x], dicts[x+1] = dicts[x+1], dicts[x]
                sorting = True
    return dicts


class TestSort(unittest.TestCase):
    def testNoFile(self):
        self.assertEqual(sort_dicts("noFile"), False)

    def testEmptyFile(self):
        self.assertEqual(sort_dicts("emptyFile.txt"), [])

    def testSimpleList(self):
        first_dict = {'a': '1', 'b': '3', 'c': '4'}
        second_dict = {'a': '8', 'b': '2', 'c': '3'}
        third_dict = {'a': '1', 'b': '1', 'c': '1'}
        self.assertEqual(sort_dicts("in.txt"),
                         [first_dict, third_dict, second_dict])
