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

class ValidateSolution():

    def __init__(self, sudoku):
        self.sudoku = np.array(sudoku)

    def valid_solution(self):
        if(self.__test_squares(self.sudoku) and
            self.__test_cols(self.sudoku) and
            self.__test_rows(self.sudoku) and 
            self.__test_not_empty_cells(self.sudoku)):
            return True
        return False


    def __test_not_empty_cells(self, test_array):
        if ((test_array == 0).any()):
            return False
        return True

    def __test_squares(self, test_array):
        for i in range(0, len(test_array)-2, 3):
            for j in range(0, len(test_array)-2, 3):
                square = test_array[i:i+3, j:j+3]
                if len(square.flatten()) > len(set(square.flatten())):
                    return False
        return True

    def __test_rows(self, test_array):
        for i in range(0, len(test_array)):
            fila = test_array[i]
            if len(fila) > len(set(fila)):
                return False
        return True

    def __test_cols(self, test_array):
        for i in range(0, len(test_array)):
            col = test_array[:,i]
            if len(col) > len(set(col)):
                return False
        return True

solution = ValidateSolution(array1)
print(solution.valid_solution())
