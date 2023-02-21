import numpy as np
from scipy import stats

new_matrix = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])

print(new_matrix)

print("speed mean, median and mode")
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

meanSpeed = np.mean(speed)
medianSpeed = np.median(speed)
modeSpeed = stats.mode(speed)

print(meanSpeed)
print(medianSpeed)
print(modeSpeed)
