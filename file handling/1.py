# f=open("eg.txt","r")
# print(f.tell())
# print(f.read(9))
# print(f.seek(2))
# print(f.read(8))
# f.close()

import os
if os.path.exists("eg.txt"):
    os.remove("eg.txt")