import unittest
import os.path


def read_dicts(file):
    dictionaries = []
    with open(file, "r") as f:
        temp_dict = {}
        for inf in f:
            inf = inf.split()
            if not inf:
                dictionaries.append(temp_dict)
                temp_dict = {}
            else:
                for (k, v) in zip(inf[0::2], inf[1::2]):
                    temp_dict[k] = v
    if temp_dict:
        dictionaries.append(temp_dict)
    return dictionaries


def sort_dicts(input_file):
    sorting = True
    if not os.path.exists(input_file):
        return False
    dicts = read_dicts(input_file)
    order = [x for x in range(len(dicts))]
    while sorting:
        sorting = False
        for x in range(len(dicts)-1):
            if dicts[x][min(dicts[x])] > dicts[x+1][min(dicts[x+1])]:
                dicts[x], dicts[x+1] = dicts[x+1], dicts[x]
                order[x], order[x+1] = order[x+1], order[x]
                sorting = True
    return order

if __name__ == "__main__":
    fout = open("out.txt", "w+")
    fout.write(str(sort_dicts("in.txt")))


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
                         [1, 2, 0])
