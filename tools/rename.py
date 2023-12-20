import os

source_dir = rf'D:/AFE-Bench0/rename'
old_str = 'CyCTTNV'
new_str = 'CyCLTNV'


for filename in os.listdir(source_dir):
    if os.path.isfile(os.path.join(source_dir, filename)):
        new_filename = filename.replace(old_str, new_str)
        old_fullpath = os.path.join(source_dir,filename)
        new_fullpath = os.path.join(source_dir,new_filename)
        os.rename(new_fullpath,old_fullpath)