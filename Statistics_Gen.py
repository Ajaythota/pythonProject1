import numpy as np
import scipy.stats as st
from scipy.stats import norm
import statistics
list1=[3,5,7,15,25,30,3,5,7,15,25,30,3,5,7,15,25,30]
print(st.describe(list1))
print(norm.std())
print(norm.var())
print(statistics.mean(list1))
print(statistics.variance(list1))
print(statistics.stdev(list1))