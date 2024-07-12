import numpy as np


data_type = [('name', 'U15'), ('class', int), ('height', float)]


students = np.zeros(4, dtype=data_type)


students['name'] = ['amith', 'dhanush', 'hemanth', 'hitesh']
students['class'] = [5, 6, 5, 5]
students['height'] = [48.5, 53, 42.5, 40.0]


print("Original array:")
print(students)


print("Sort by height:")
print(np.sort(students, order='height'))
