import numpy as np

file_name = "./data/test"
file_size = 100*pow(2,20) # byte

data = np.random.bytes(file_size)
print("Add "+str(file_size)+" bytes to file")
f = open(file_name,"wb")
f.write(data)
f.close
