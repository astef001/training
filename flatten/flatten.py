import unittest
def flatten(list_a,list_b,max_depth):
    list_a_flatten=[]
    list_b_flatten=[]
    if max_depth==0:
        return list_a,list_b
    for x in list_a:
        if isinstance(x,list):
            list_a_flatten+=x
        else:
            list_a_flatten+=[x]
    for x in list_b:
        if isinstance(x,list):
            list_b_flatten+=x
        else:
            list_b_flatten+=[x]
    return flatten(list_a_flatten,list_b_flatten,max_depth-1)

class TestFlatten(unittest.TestCase):
    def test_depth_one(self):
        self.assertEqual(flatten([1,2,[3,[4,5,6]]],[1,[[[2,3],[4,5]],8]],1),([1, 2, 3, [4, 5, 6]], [1, [[2, 3], [4, 5]], 8]))
    def test_depth_two(self):
        self.assertEqual(flatten([1,2,[3,[4,5,6]]],[1,[[[2,3],[4,5]],8]],2),([1, 2, 3, 4, 5, 6], [1, [2, 3], [4, 5], 8]))
    def test_depth_three(self):
        self.assertEqual(flatten([1, 2, [3, [4, 5, 6]]], [1, [[[2, 3], [4, 5]], 8]], 3),([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 8]))

if __name__== '__main__':
    unittest.main()