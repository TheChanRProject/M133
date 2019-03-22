from os import listdir, system
from os.path import isfile, join
nb_path = system("cd nb")
onlyfiles = [f for f in listdir(nb_path) if isfile(join(nb_path, f))] 
