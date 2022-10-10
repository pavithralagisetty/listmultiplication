import numpy as np
ar1=np.array(list1)
ar2=np.array(list2)
to=time.time()
prodlist=ar1*ar2
tp=time.time()
print(tp-to)
numpy_time=tp-to
print("The ratio of time taken is {}".format(list_time/numpy_time))
