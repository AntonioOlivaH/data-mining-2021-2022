'''
###!/bin/python3
### -*- encoding: utf-8 -*-
### by Antonio Hernandez Oliva, Ghislaine van den Boogerd, Otto Mättas
#######
### This script is for solving a classification problem
'''

import numpy as np

# Import data to a numpy array
import_data = np.genfromtxt('practice.txt', delimiter=',', dtype=int, names=True)
# Print column names for debugging
# print(import_data.dtype.names)

# Define variable for the class column
class_data = import_data['class']

def calculate_impurity(array):
    '''Calculate impurity for a vector using gini-index as impurity measure

        Parameters
        ----------
        array : array
            The array of binary class labels

        Raises
        ------
        RuntimeError
            Out of fuel

        Returns
        -------
        imp
            Impurity of a vector of (arbitrary length) of class labels
        '''
    # Define impurity variable
    imp = 0
    # Flatten array to 1d, treat all values equally
    array = array.flatten()
    # Sort array values
    array = np.sort(array)
    # Count array elements
    n_elements = array.shape[0]
    # Count 1s in array
    ones = np.count_nonzero(array)
    # Count 0s in array
    zeros = n_elements - ones
    # Probability of class 1
    p_ones = ones / n_elements
    # Probability of class 0
    p_zeros = zeros / n_elements
    # Calculate impurity
    imp = p_ones * p_zeros
    # Return impurity
    return imp

impurity = calculate_impurity(class_data)
print('Impurity is {0}'.format(impurity))