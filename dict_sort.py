import unittest
import os.path


def read_dicts(file):
    dictionaries=[]
    if not os.path.exists(file):
        return False
    with open(file, "r") as f:
        while True:
            temp_dict = {}
            inf = f.readline()
            if not inf:
                break
            inf = inf.rstrip("\n\r")
            inf = str.split(inf,' ')
            for i in range(0,len(inf)-1,2):
                temp_dict["%s".format(inf[i])] = inf[i+1]
            dictionaries.append(temp_dict)
    return dictionaries


def sort_dicts(input_file):
    sorting = True
    dictionaries = read_dicts(input_file);
    if dictionaries == False:
        print("Failed to open file");
        return False;
    while sorting:
        sorting = False
        for x in range(len(dictionaries)-1):
            if dictionaries[x][min(dictionaries[x])] > dictionaries[x+1][min(dictionaries[x+1])]:
                dictionaries[x], dictionaries[x+1] = dictionaries[x+1],dictionaries[x]
                sorting = True
    return dictionaries


class TestSort(unittest.TestCase):
    def testNoFile(self):
        self.assertEqual(sort_dicts("noFile"), False)


    def testEmptyFile(self):
        self.assertEqual(sort_dicts("emptyFile.txt"), [])


    def simpleTest(self):
        self.assertEqual(sort_dicts("in.txt"),[{'a': '1', 'b': '3', 'c': '4'}, {'a': '8', 'b': '2', 'c': '3'}])
