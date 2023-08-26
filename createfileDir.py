import os

ld=os.listdir("f:\\STL\\08 - Gambody\\Missing")
for dir in ld:
    dr=dir
    os.mkdir(os.path.join("f:\\STL\\08 - Gambody\\Missing",dir,"Files"))
ll=0
