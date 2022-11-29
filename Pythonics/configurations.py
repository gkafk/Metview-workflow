'''
Set global variables and names for directories of all python scripts
'''
import os


# Ο φάκελος των αρχείων grib
_OUTPUT_FOLDER = "/data/grib_files/output"
# Ο φάκελος όπου εξάγονται οι εικόνες
_IMAGES_EXPORT_DIR ="/data/images/"
# Επιλέγουμε τα τρίωρα steps που θέλουμε να παραχθούν

_STEPS  = [ "3","to","120","by","3" ]
# _STEPS= [ "3","to","75","by","3" ]
# _STEPS = [ "0","to","9","by","3" ]

# Η λίστα των γεωδυναμικών υψών
_LEVELS_STEADY_LIST = ["100","150","200","300","400","500","700","800","850","900","925","1000"]


# print(".....",os.getcwd())

bash_conf_path= "../Constructors/global_variables.cfg"

# OR get the paths needed from file /Constructors/global_variables.cfg
bash_conf_file = open(bash_conf_path,"r")
lines = bash_conf_file.readlines()
for line in lines:
    # print("start line:",line)
    line=line.strip("\n'")
    if line.startswith("_OUTPUT_FOLDER"):
        _OUTPUT_FOLDER = line.split("=")[1].strip('"')
        print("_OUTPUT_FOLDER:",_OUTPUT_FOLDER)
    if line.startswith("_EXPORT_IMAGES_FOLDER"):
        _IMAGES_EXPORT_DIR = line.split("=")[1].strip('"')
        print("_IMAGES_EXPORT_DIR:",_IMAGES_EXPORT_DIR)
bash_conf_file.close()