import numpy as np
import os 
file_name = "./data/test"
new_size = 1*pow(2,10) # byte

data = np.random.bytes(new_size)

with open(file_name,"rb") as f:
    currentPos = f.tell()
    f.seek(0,2)
    length= f.tell()
    f.seek(currentPos,0)
    print("Length of file is "+str(length))
    temp = f.read(new_size)
    origin = f.read(length-new_size)
    data+= origin
    print("Read success!")
    f.close()

os.rename(file_name,file_name+"_old")
print("Rename success!")
with open(file_name,"wb") as f:
    f.write(data)
    f.close()
print("Recreate success!")
