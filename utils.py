import os
def create_dir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)