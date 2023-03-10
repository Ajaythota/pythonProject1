import os, time,shutil
import datetime
def mkDir(folder):
    os.mkdir(folder)
def rmDir(folder):
    shutil.rmtree(folder) # deletes directory with files

expiredBy=time.time()-(10*86400)
print(expiredBy)
Dir=f"{os.getcwd()}\\demo"
fn=str(datetime.datetime.today().date())
#fn=fn-datetime.timedelta(days=8)
#Folder=f"{Dir}\\{fn}"
Folder = os.path.join(Dir, fn)
print(Dir)
print(fn)
if os.path.exists(Folder):
    print("folder already exists")
else:
    mkDir(Folder)

for i in os.listdir(Dir):
    Folders = os.path.join(Dir, i)
    print(Folders)

    if os.stat(Folders).st_mtime <= expiredBy :
        #print(os.stat(Folders).st_mtime)
       #rmDir(Folders)
       print(" folder deleted")
       #break #break-point can removed once coded properly tested
    else:
        print("no folder/files to delete" )
        print(os.stat(Folders).st_mtime)



