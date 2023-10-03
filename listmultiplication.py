import time
import numpy as np

list1 = np.arange(1000000)
list2 = np.arange(1000000)

start_time = time.time()
prod_lists = list1 * list2
end_time = time.time()

print(end_time - start_time)
