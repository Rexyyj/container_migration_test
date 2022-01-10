import numpy as np
import os 
file_name = "./data/test"
file_size = 1#*pow(2,10) # byte

data = np.random.bytes(file_size)
with open(file_name,"rb") as f:
    currentPos = f.tell()
    f.seek(0,2)
    length = f.tell()
    f.seek(currentPos,0)
    data+=f.read(length)
    print("Read success!")
    f.close()

os.rename(file_name,file_name+"_old")
print("Remove success!")
with open(file_name,"wb") as f:
    f.write(data)
    f.close()
print("Recreate success!")
