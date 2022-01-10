import numpy as np
import os

file_name = "./data/test"
file_size = 1*pow(2,10) # byte

data = np.random.bytes(file_size)
new_data = ""
with open(file_name,"rb") as f:
    current = f.tell()
    f.seek(0,2)
    length=f.tell()
    f.seek(current,0)
    new_data=data+ f.read(length)
    print("read success")
    f.close()

os.rename(file_name, file_name+"_old")
print("rename success")

with open(file_name,"wb") as f:
    f.write(new_data)
    f.close()

print("add end success")

