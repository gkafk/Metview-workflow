# !/usr/bin/python3
'''
Set global variables and names for directories for all python scripts
'''
import os


# Selecting hour steps
_STEPS  = [ "3","to","120","by","3" ]
# _STEPS = [ "3","to","75","by","3" ]
# _STEPS = [ "0","to","9","by","3" ]


#  European Airports coorfinates Lat,Lon
_LOCATIONS_DICT = {
            "LIRA": [41.80, 12.59],
            "LFPO": [48.72, 02.39],
            "LEMD": [40.49, -03.58],
            "LPPT": [38.76, -09.13],
            "EFHK": [60.3, 24.9],
}



# [From , To , Steps*3]
_ROUTES_LIST = [
            ["LGAV","LEMD",5],
            ["LGAV","EFHK",5],
]


# forecasting Images for production with plot_images.py
# Uncomment lists lines for activating their production
#           [Name ,         geopotential height, steps]
_PRODUCTS = [
            ["Temperature",             "850",  _STEPS],
            ["Temperature 500",         "500",  _STEPS],
            #["2 metre temperature",     "0",    _STEPS],
            #["10m Wind speed",          "0",    _STEPS],
            #["10m Wind gust",           "0",    _STEPS],
            #["Cloud base height",       "0",    _STEPS],
            #["Total cloud cover",       "0",    _STEPS],
            #["Total precipitation",     "0",    _STEPS],
            #["Preci - Lightnings",      "0",    _STEPS],
            #["Preci - snow",            "0",    _STEPS],
            #["Snowfall",                "0",    _STEPS],
            #["Relative humidity",       "200",  _STEPS],
            #["Relative humidity",       "300",  _STEPS],
            #["Relative humidity",       "500",  _STEPS],
            #["Relative humidity",       "700",  _STEPS],
            #["Relative humidity",       "850",  _STEPS],
            #["Relative humidity",       "925",  _STEPS],
            #["Relative humidity",       "1000", _STEPS],
            #["Absolute humidity",       "1000", _STEPS],
            #["Mean sea level pressure", "0",    _STEPS],
            #["Sea surface temperature", "0",    _STEPS],
            #["Visibility",              "0",    _STEPS],
            #["Opera",                   "0",    _STEPS],
            #["Discomfort Index",        "0",    _STEPS],
            #["Total wave",              "0",    _STEPS],
            #["Wind speed",              "200",  _STEPS],
            #["Wind speed",              "300",  _STEPS],
            #["Wind speed",              "500",  _STEPS],
            #["Wind speed",              "700",  _STEPS],
            #["Wind speed",              "850",  _STEPS],
            #["Wind speed",              "925",  _STEPS],
            #["Wind speed",              "1000", _STEPS],
            #["Jet",                     "200",  _STEPS],
            #["Jet",                     "300",  _STEPS],
            #["T-advection",             "500",  _STEPS],
            #["T-advection",             "700",  _STEPS],
            #["T-advection",             "850",  _STEPS],
            #["Potential vorticity",     "500",  _STEPS],
            #["Potential vorticity",     "700",  _STEPS],
            #["Potential vorticity",     "850",  _STEPS],
            #["Relative vorticity",      "500",  _STEPS],
            #["Thermal wind",            "500",  _STEPS],
            #["Thermal wind",            "700",  _STEPS],
            #["Thermal wind",            "850",  _STEPS],
            #["Static stability",        "500",  _STEPS],
            #["Static stability",        "700",  _STEPS],
            #["Static stability",        "850",  _STEPS],
            #["Lightnings radar",        "0"  ,  _STEPS],
            #["Lightnings AVG3H",        "0"  ,  _STEPS],
            #["Lightnings instant",      "0"  ,  _STEPS],
            #["Zero level",              "0"  ,  _STEPS],
            #["Precipitation type",      "0"  ,  _STEPS],
            #["Total precipitation rate","0"  ,  _STEPS],
            #["MIS",                     "0",    _STEPS],
            #["Run Difference",          "500",  _STEPS], # needs 2 runs
            ["Potential vorticity isentropic","315",  _STEPS],
        ]


# Geopotential height levels
_LEVELS_STEADY_LIST = ["100","150","200","300","400","500","700","800","850","900","925","1000"]

#  isentropic levels
_ISENTROPIC_LEVELS = ["300","315","330"]

# print(".....",os.getcwd())

bash_conf_path= "../Constructors/global_variables.cfg"

# OR get the paths needed from file /Constructors/global_variables.cfg
bash_conf_file = open(bash_conf_path,"r")
lines = bash_conf_file.readlines()
for line in lines:
    # print("start line:",line)
    line=line.strip("\n'")
    if line.startswith("_OUTPUT_FOLDER"):
        _OUTPUT_FOLDER = os.path.expantuser(line.split("=")[1].strip('"'))
        print("_OUTPUT_FOLDER:",_OUTPUT_FOLDER)
    if line.startswith("_EXPORT_IMAGES_FOLDER"):
        _IMAGES_EXPORT_DIR = os.path.expantuser(line.split("=")[1].strip('"'))
        print("_IMAGES_EXPORT_DIR:",_IMAGES_EXPORT_DIR)
bash_conf_file.close()
