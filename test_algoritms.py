import unittest
from algoritms import *

class AlgoritmsCase(unittest.TestCase):
    """ Tests for 'algoritms.py'"""
    
    def test_binary_search(self):
        work_list = [1, 2, 4, 6, 7, 9, 11]
        output_value = binary_search(work_list, 2)
        self.assertEqual(output_value, 1)
    
    def test_find_smallest(self):
        arr = [5, 9, 8, 7, 1, 0, -3]
        smallest = find_smallest(arr)
        self.assertEqual(smallest, 6)
    
    def test_selection_sort(self):
        arr = [5, 9, 8, 7, 1, 0, -3]
        new_arr = selection_sort(arr)
        self.assertEqual(new_arr, [-3, 0, 1, 5, 7, 8, 9])
        
    def test_fact(self):
        number_fact = fact(3)
        self.assertEqual(number_fact, 6)
        
    def test_summ(self):
        summa = summ([2, 4, 6, 12])
        self.assertEqual(summa, 24)
        
    def test_count(self):
        answer = count([2, 4, 6, 12])
        self.assertEqual(answer, 4)
        
    def test_find_biggest(self):
        biggest = find_biggest([1, 4, 100, 12, 3])
        self.assertEqual(biggest, 100)
        
    def test_quick_sort(self):
        array = quick_sort([5, 7, 3, 1, 8, 2])
        self.assertEqual(array, [1, 2, 3, 5, 7, 8])
        

    def test_breadth_first_serach(self):
        graph = {
            "s":["a", "b"],
            "a":["d"],
            "b":["c", "e"],
            "c":["d"],
            "d":["f"],
            "e":["d"],
            "f":[],
        }
        
        seller_mango = breadth_first_serach("s", graph)
        self.assertEqual(seller_mango, False)
        
    def test_dijkstra_algoritm(self):
        graph = {}
        graph['s'] = {}
        graph['s']['a'] = 5
        graph['s']['b'] = 2
        graph['a'] = {}
        graph['a']['c'] = 2
        graph['a']['d'] = 4
        graph['b']={}
        graph['b']['a'] = 8
        graph['b']['c'] = 7
        graph['c'] = {}
        graph['c']['f'] = 1
        graph['d'] = {}
        graph['d']['c'] = 6
        graph['d']['f'] = 3
        graph['f'] = {}
        
        costs = {}
        costs['a'] = 5
        costs['b'] = 2
        costs['c'] = float("inf")
        costs['d'] = float("inf")
        costs['f'] = float("inf")
        
        parents = {}
        parents['a'] = 's'
        parents['b'] = 's'
        parents['c'] = None
        parents['d'] = None
        parents['f'] = None
        
        processed = []
        
        parent = dijkstra_algoritm(graph, costs, parents, processed)
        self.assertEqual(parent, {'a': 's', 'b': 's', 'c': 'a', 'd': 'a', 'f': 'c'})

unittest.main()
