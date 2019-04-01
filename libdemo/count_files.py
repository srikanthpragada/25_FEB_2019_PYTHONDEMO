import os

files = os.walk("..")

for dirname,dirs,files  in files:
    if dirname.find(".git") >= 0:
        continue

    print( f"{dirname:30}   - {len(dirs)}  {len(files)}")