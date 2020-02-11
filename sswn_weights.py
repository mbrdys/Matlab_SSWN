import numpy as np


class Weights:

    def __init__(self, structure):
        self.structure = structure
        self.rows_number = self.structure.state_space_size + self.structure.number_of_outputs + \
                           2*(self.structure.number_of_inputs + self.structure.number_of_outputs +
                           self.structure.state_space_size)
        self.columns_number = self.structure.number_of_wavelons
        self.values = self.weight_init()

    def weight_init(self):

        return np.random.rand(*np.zeros((self.rows_number, self.columns_number), float).shape).dot(2)-1

    def anneal(self, temperature):

        melt_matrix = np.random.rand(*np.zeros((self.rows_number, self.columns_number), float).shape).dot(2*temperature)-temperature
        self.values = self.values + melt_matrix
