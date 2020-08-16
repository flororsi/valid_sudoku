import unittest 
import validSolution
import numpy as np

array1 = np.array([
     [5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 5, 3, 4, 8],
     [1, 9, 8, 3, 4, 2, 5, 6, 7],
     [8, 5, 9, 7, 6, 1, 4, 2, 3],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 6, 1, 5, 3, 7, 2, 8, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 4, 5, 2, 8, 6, 1, 7, 9]
   ])
array2 = np.array([
     [5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 0, 3, 4, 8],
     [1, 0, 0, 3, 4, 2, 5, 6, 0],
     [8, 5, 9, 7, 6, 1, 0, 2, 0],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 0, 1, 5, 3, 7, 2, 1, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 0, 0, 4, 8, 1, 1, 7, 9]
   ])

class TestSudoku(unittest.TestCase):

    # Check if the solution is valid
    def test_valid_solution(self):
        result = validSolution.ValidateSolution(array1).valid_solution()
        self.assertTrue(result)

    # Check if the solution is invalid
    def test_invalid_solution(self):
        result = validSolution.ValidateSolution(array2).valid_solution()
        self.assertFalse(result)

    # Check if the array is composed of 2 dimensions
    def test_array_dimension(self):
        self.assertEqual(np.ndim(array1),2)
        self.assertEqual(np.ndim(array2),2)
 
    # Check if the number of columns are 9   
    def test_qty_colulmns(self):        
        for i in range(0, len(array1)):
            col = array1[:,i]
            self.assertEqual(len(col),9)  
        for i in range(0, len(array2)):
            col = array1[:,i]
            self.assertEqual(len(col),9)    

    # Check if the number of row is 9      
    def test_qty_rows(self):        
        for i in range(0, len(array1)):
            fila = array1[i]
            self.assertEqual(len(fila),9)
        for i in range(0, len(array2)):
            fila = array1[i]
            self.assertEqual(len(fila),9)

    # Check if the array is composed of integers between 0 and 9
    def test_data_type(self):     
        self.assertTrue((array1 >= 0).all() and (array1 <= 9).all())
