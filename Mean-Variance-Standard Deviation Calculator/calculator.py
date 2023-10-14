import numpy as np

def calculate(li):
    if len(li) != 9:
      raise ValueError("List must contain nine numbers.")
    ar = np.array(li).reshape((3,3))
    l_mean = list((list(ar.mean(axis = 0)), list(ar.mean(axis = 1)), ar.mean()))
    l_var = list((list(ar.var(axis = 0)), list(ar.var(axis = 1)), ar.var()))
    l_std = list((list(ar.std(axis = 0)), list(ar.std(axis = 1)), ar.std()))
    l_max = list((list(ar.max(axis = 0)), list(ar.max(axis = 1)), ar.max()))
    l_min = list((list(ar.min(axis = 0)), list(ar.min(axis = 1)), ar.min()))
    l_sum = list((list(ar.sum(axis = 0)), list(ar.sum(axis = 1)), ar.sum()))
    calculations = {'mean': l_mean, 'variance': l_var, 'standard deviation': l_std, 'max': l_max, 'min': l_min, 'sum': l_sum}
    return calculations
