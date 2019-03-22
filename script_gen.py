from os import listdir, system, getcwd
from os.path import isfile, join, dirname
nb_path = 
onlyfiles = [f for f in listdir(nb_path) if isfile(join(nb_path, f))]
print(onlyfiles)
