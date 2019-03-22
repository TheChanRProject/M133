from os import listdir, system, getcwd
from os.path import isfile, join, dirname
getcwd()
nb_path = dirname('/Volumes/DSDRIVE/DS/Python/Splash/M133' + '/nb')
print(nb_path)
onlyfiles = [f for f in listdir(nb_path) if isfile(join(nb_path, f))]
print(onlyfiles)
