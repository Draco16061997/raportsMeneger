import os

path = '/Users/mikita/Work/Продакшн/END/'

# print(os.listdir(path))
# for i in os.listdir(path):
#     print(i, type(i), path+"/"+i, os.path.isdir(path+"/"+i))

l =[]
def WalkFiles(path):
    # l = []
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            WalkFiles(path+'/'+i)
        else: l.append(i)
    return l


# WalkFiles(path)
for i in WalkFiles(path):
    s = i.split('_')
    t = len(s)
    if t == 5:
        print (s[0],s[2],s[3],s[4].replace(".mp4",""))


class folderParcer:

    def __init__(self, path):
        self.path = path