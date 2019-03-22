from os import listdir, system
from os.path import isfile, join
from pathlib import Path
Path.cwd()
onlyfiles = [f for f in listdir('/Volumes/DSDRIVE/DS/Python/Splash/M133/nb') if isfile(join('/Volumes/DSDRIVE/DS/Python/Splash/M133/nb', f))]
print(onlyfiles)
file_names = [i[:-6].replace(' ', '-') for i in onlyfiles]
print(file_names)
py_names = [i+'.py' for i in file_names]
print(py_names)
for i in py_names:
    system(f"touch {i} && mv {i} src")
