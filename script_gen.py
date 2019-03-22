from os import listdir, system
from os.path import isfile, join
from pathlib import Path
Path.cwd()
onlyfiles = [f for f in listdir('/Volumes/DSDRIVE/DS/Python/Splash/M133/nb') if isfile(join('/Volumes/DSDRIVE/DS/Python/Splash/M133/nb', f))]
print(onlyfiles)
file_names = [i[:-6] for i in onlyfiles]
print(file_names)
