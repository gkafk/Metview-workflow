# !/usr/bin/python3
import metview as mv
import xarray as xr
import os
import traceback
import subprocess
import math
from datetime import date,timedelta
import tkinter
from tkinter import *
# import local ata moduless
from products import *
import globalVariables as gbl

# Merged grib files folder
output_folder = gbl._OUTPUT_FOLDER

# 3 hour steps
steps = gbl._STEPS

# True for loading products default configuration
# False when new level or contour is choosen in the same product
defaults_flag = True

today = date.today().strftime("%Y_%m_%d")
# print(today)
data_saved=[]

# removing hidden files from list
def remove_hidden_files(lista):
    for item in lista[:]:
        if item.startswith(".") or "ERROR" in item:
            lista.remove(item)




# ECMWF Logo
organizations_image=mv.mimport(
    import_file_name    = "ECMWF_Master_Logo.png",
    import_x_position   = 0.4,
    import_y_position   = 20,
    import_width        = 2.0,
    import_height       = 0.4
    )


# MV Logo
mv_image=mv.mimport(
    import_file_name    = "Metview_logo.png",
    import_x_position   = 28.0,
    import_y_position   = 0.3,
    import_width        = 1.0,
    import_height       = 0.9
    )

# Locations dictionary
loc_dict ={
            "LGLR": [39.65, 22.46],
            "LGBL": [39.21, 22.79],
            "LGEL": [38.06, 23.55],
            "LGTS": [40.52, 22.97],
            "LGTG": [38.33, 23.56],
            "LGSA": [35.53, 24.14],
            "LGRX": [38.14, 21.42],
            "LGAD": [37.92, 21.29],
            "LGKL": [37.07, 22.02],
            "LGTL": [35.19, 25.33],
            "LGSY": [38.97, 24.48],
            "LGLM": [39.92, 25.23]
           }
#===================================================================================================
#        Buttons values init
#===================================================================================================
#date_list =[str(today)]
date_list =sorted( os.listdir(output_folder) ,reverse=True )
remove_hidden_files(date_list)

# ECMWF RUN times list - taken from day subfolders
run_list = sorted( os.listdir(output_folder+"/"+date_list[0]) ,reverse=True )
remove_hidden_files(run_list)
# run_list = ["0000","1200"]


# Geopotential heights
levels_list = gbl._LEVELS_STEADY_LIST
#  isentropic levels
isentropic_levels = gbl._ISENTROPIC_LEVELS

# Products dictionary
panel_products_dict = {
        #  Synoptics**********************************************************
        "Synoptics":{
                "Temperature":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Temperature 500":{
                            "default_level" : "500",
                            "levels"        : levels_list
                            },
                "Geopotential Height":{
                            "default_level" : "500",
                            "levels"        : levels_list
                            },
                "RH-VV":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Absolute humidity":{
                            "default_level" : "1000",
                            "levels"        : levels_list
                            },
                "Relative humidity":{
                            "default_level" : "200",
                            "levels"        : levels_list
                            },
                "Relative vorticity":{
                            "default_level" : "500",
                            "levels"        : levels_list
                            },
                "Mean sea level pressure":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Wind speed":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Jet":{
                            "default_level" : "300",
                            "levels"        : levels_list
                            },
                "Vertical velocity":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "CAPE":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Run Difference":{
                            "default_level" : "500",
                            "levels"        : levels_list
                            },
                "Synoptics":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                    },
        #  Dynamics *********************************************************
        "Dynamics":{
                "PT":{
                            "default_level" : "500",
                            "levels"        : levels_list
                            },
                "Divergence":{
                            "default_level" : "500",
                            "levels"        : levels_list
                            },
                "T-advection":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Potential vorticity":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Potential vorticity isentropic":{
                            "default_level" : "315",
                            "levels"        : isentropic_levels
                            },
                "Thermal wind":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Static stability":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                "Q-vectors":{
                            "default_level" : "850",
                            "levels"        : levels_list
                            },
                    },
        #  Surface **********************************************************
        "Surface":{
                "2 metre temperature":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "2 metre dewpoint temperature":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Mean sea level pressure":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Cloud base height":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Low cloud cover":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Medium cloud cover":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "High cloud cover":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Total cloud cover":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Preci - Lightnings":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Preci - snow":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Total precipitation":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Snowfall":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Sea surface temperature":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Visibility":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Opera":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Opera winds":{
                            "default_level" : "0",
                            "levels"        : levels_list
                            },
                "Opera wave":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "MIS":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Discomfort Index":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Total wave":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Lightnings AVG1H":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Lightnings AVG3H":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Lightnings radar":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Lightnings instant":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Zero level":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Precipitation type":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "10m Wind speed":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "10m Wind gust":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "100m Wind speed":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Large-scale precipitation":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Convective precipitation":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                "Critical limits":{
                            "default_level" : "0",
                            "levels"        : ["0"]
                            },
                    },
}



cross_section_products = ["Relative humidity", "Divergence","Potential vorticity", "Vorticity (relative)",
                            "U component of wind", "v component of wind", "Vertical velocity" ]


#===================================================================================================
#               Γραφικό περιβάλλον
#===================================================================================================
root = Tk()
root.geometry("860x600") #width x height
root.title("Panel metview v3.0")
root.iconphoto(True,PhotoImage(file='Metview_logo.png'))
#root.call("wm","iconphoto",root._w,PhotoImage(file="/home/metview/metview/System/Pythonics/pmk.png"))

cross_section_frame  = LabelFrame(root,text="Cross Section",labelanchor="ne" ,bd=2,bg="grey",width=750,height=200,relief='sunken',pady=5,padx=5)
cross_section_frame.grid(row=5,column=0,rowspan=5,columnspan=8, sticky = "NESW")

metgram_frame  = LabelFrame(root,text="Meteograms",labelanchor="ne" ,bd=2,bg="ivory2",width=750,height=200,relief='sunken',pady=5,padx=5)
metgram_frame.grid(row=13,column=0,rowspan=5,columnspan=8, sticky = "NESW")

frame_return = Frame(root,bd=2,bg="white",width=750,height=200,relief='sunken',pady=5,padx=5)
frame_return.grid(row=19,column=0,rowspan=10,columnspan=8, sticky = "NESW")



date_run = Label(root,text="Date", font=('Arial', 12), fg="blue",justify="center")
date_run.grid(row=1,column=0)

date_var  = StringVar(root)
date_var.set(date_list[0])
date_opt = OptionMenu(root, date_var, *date_list)
date_opt.config(width=12, font=('Arial', 12))
date_opt.grid(row=2,column=0)

label_run = Label(root,text="RUN", font=('Arial', 12), fg="blue",justify="center")
label_run.grid(row=1,column=1)

run_var  = StringVar(root)
run_var.set(run_list[0])
opt = OptionMenu(root, run_var, *run_list)
opt.config(width=8, font=('Arial', 12))
opt.grid(row=2,column=1)


# products = sorted( panel_products_dict.keys())
products = panel_products_dict.keys()
products_var  = StringVar(root)
products_var.set( "Choose product" )
products_opt = OptionMenu(root, products_var, *products)
products_opt.config(width=40, font=('Arial', 12))
products_opt.grid(row=2,column=2,columnspan=3, sticky = "w")

main_menu = Menu(products_opt, tearoff=False)
products_opt.configure(menu=main_menu)

for item in products:
    menu = Menu(main_menu,tearoff=False)
    main_menu.add_cascade(label=item, menu=menu,font=('Arial', 12))
    for value in panel_products_dict[item].keys():
        menu.add_radiobutton(value=value, label=value, variable=products_var,font=('Arial', 12))


label_levels = Label(root,text="Levels", font=('Arial', 12), fg="blue", justify="center")
label_levels.grid(row=1,column=5)

levels_var  = StringVar(root)
levels_var.set(levels_list[0])
levels_opt = OptionMenu(root, levels_var, *levels_list)
levels_opt.config(width=8, font=('Arial', 12))
levels_opt.grid(row=2,column=5, sticky = "w")

label_contours = Label(root,text="Contours", font=('Arial', 12), fg="blue", justify="center")
label_contours.grid(row=3,column=0)

contours_var  = StringVar(root)
contours_var.set(next(iter(contours_dict)))
contours_opt = OptionMenu(root, contours_var, *contours_dict.keys())
contours_opt.config(width=12, font=('Arial', 12))
contours_opt.grid(row=4,column=0, sticky = "w")

label_coastlines = Label(root,text="Coastlines", font=('Arial', 12), fg="blue", justify="center")
label_coastlines.grid(row=3,column=1)

coastlines_var  = StringVar(root)
coastlines_var.set(next(iter(coastlines_dict)))
coastlines_opt = OptionMenu(root, coastlines_var, *coastlines_dict.keys())
coastlines_opt.config(width=8, font=('Arial', 12))
coastlines_opt.grid(row=4,column=1, sticky = "w")

label_legends = Label(root,text="Legends", font=('Arial', 12), fg="blue", justify="center")
label_legends.grid(row=3,column=2)

legends_var  = StringVar(root)
legends_var.set(next(iter(legends_dict)))
legends_opt = OptionMenu(root, legends_var, *legends_dict.keys())
legends_opt.config(width=8, font=('Arial', 12))
legends_opt.grid(row=4,column=2, sticky = "w")

label_texts = Label(root,text="Texts", font=('Arial', 12), fg="blue", justify="center")
label_texts.grid(row=3,column=3)

texts_var  = StringVar(root)
texts_var.set(next(iter(texts_dict)))
texts_opt  = OptionMenu(root, texts_var, *texts_dict.keys())
texts_opt.config(width=11, font=('Arial', 12))
texts_opt.grid(row=4,column=3, sticky = "w")

label_geoviews = Label(root,text="Geoviews", font=('Arial', 12), fg="blue", justify="center")
label_geoviews.grid(row=3,column=4)

geoviews_var  = StringVar(root)
geoviews_var.set(next(iter(geoviews_dict)))
geoviews_opt  = OptionMenu(root, geoviews_var, *geoviews_dict.keys())
geoviews_opt.config(width=12, font=('Arial', 12))
geoviews_opt.grid(row=4,column=4, sticky = "w")


message = Message(frame_return,text="Welcome to Metview python interface panel", font=('Arial', 16), fg='red',bg="white",width=440,justify="left")
message.pack(fill="both")

#===================== cross Section ================================================

Label(cross_section_frame, text="Line Coordinates",bg="grey").grid(row=0,column=0, sticky = "e")
line_coords = Entry(cross_section_frame)
line_coords.grid(row=0, column=1, sticky = "w")

Label(cross_section_frame, text="Step",bg="grey").grid(row=0,column=2, sticky = "e")

step_list = list(range(0,80,3))
step  = StringVar(cross_section_frame)
step.set(step_list[0])
step_opt = OptionMenu(cross_section_frame, step, *step_list)
step_opt.config(width=5, font=('Arial', 12))
step_opt.grid(row=0,column=3, sticky = "w")

label_cross_1= Label(cross_section_frame,text="1st product", font=('Arial', 12), fg="orange", bg="grey", justify="center")
label_cross_1.grid(row=2,column=0,columnspan=2)

cross_1_var  = StringVar(cross_section_frame)
cross_1_var.set(cross_section_products[0])
cross_1_opt = OptionMenu(cross_section_frame, cross_1_var, *cross_section_products)
cross_1_opt.config(width=20, font=('Arial', 12))
cross_1_opt.grid(row=3,column=0,columnspan=2, sticky = "w")

cross_section_products_2 =["-"]
# changes the list with names in the button 2nd product
def onclick_bt_change(*args):
    cross_2_opt['menu'].delete(0,'end')
    if var1.get()==1:
        for item in cross_section_products:
            cross_2_opt['menu'].add_command(label=item,command=tkinter._setit(cross_2_var,item))
            cross_2_var.set(cross_section_products[0])
    if var1.get()==0:
        for item in cross_section_products_2:
            cross_2_opt['menu'].add_command(label=item,command=tkinter._setit(cross_2_var,item))
            cross_2_var.set(cross_section_products_2[0])

var1 = IntVar()
check_1 = Checkbutton(cross_section_frame, text='2nd Product?',variable=var1, onvalue=1, offvalue=0, command=onclick_bt_change)
check_1.grid(row=3,column=2,sticky = "w",padx=5,pady=5)


label_cross_2= Label(cross_section_frame,text="2nd product", font=('Arial', 12), fg="orange", bg="grey",justify="center")
label_cross_2.grid(row=2,column=3,columnspan=2)

cross_2_var  = StringVar(cross_section_frame)
cross_2_var.set(cross_section_products_2[0])
cross_2_opt = OptionMenu(cross_section_frame, cross_2_var, *cross_section_products_2)
cross_2_opt.config(width=20, font=('Arial', 12))
cross_2_opt.grid(row=3,column=3,columnspan=2, sticky = "w")

cr_1_label_contours = Label(cross_section_frame,text="Contour 1", font=('Arial', 12), fg="orange", bg="grey",justify="center")
cr_1_label_contours.grid(row=4,column=0,columnspan=2)

cr_1_contours_var  = StringVar(cross_section_frame)
cr_1_contours_var.set(next(iter(contours_dict)))
cr_1_contours_opt = OptionMenu(cross_section_frame, cr_1_contours_var, *contours_dict.keys())
cr_1_contours_opt.config(width=20, font=('Arial', 12))
cr_1_contours_opt.grid(row=5,column=0,columnspan=2, sticky = "w")

cr_2_label_contours = Label(cross_section_frame,text="Contour 2", font=('Arial', 12), fg="orange", bg="grey",justify="center")
cr_2_label_contours.grid(row=4,column=3,columnspan=2)

cr_2_contours_var  = StringVar(cross_section_frame)
cr_2_contours_var.set(next(iter(contours_dict)))
cr_2_contours_opt = OptionMenu(cross_section_frame, cr_2_contours_var, *contours_dict.keys())
cr_2_contours_opt.config(width=20, font=('Arial', 12))
cr_2_contours_opt.grid(row=5,column=3,columnspan=2, sticky = "w")

label_from = Label(cross_section_frame,text="from CW", font=('Arial', 12), bg="grey",fg="blue",justify="center")
label_from.grid(row=6,column=0)

from_var  = StringVar(cross_section_frame)
from_var.set("Origin")
from_opt = OptionMenu(cross_section_frame, from_var, *loc_dict.keys())
from_opt.config(width=10, font=('Arial', 12))
from_opt.grid(row=7,column=0,columnspan=1, sticky = "w")

label_to = Label(cross_section_frame,text="to CW", font=('Arial', 12), bg="grey",fg="blue",justify="center")
label_to.grid(row=6,column=1)

to_var  = StringVar(cross_section_frame)
to_var.set("Destination")
to_opt = OptionMenu(cross_section_frame, to_var, *loc_dict.keys())
to_opt.config(width=10, font=('Arial', 12))
to_opt.grid(row=7,column=1,columnspan=1, sticky = "w")

#===================== Meteograms ================================================


label_cws = Label(metgram_frame,text="CW", font=('Arial', 12), bg="ivory2",fg="blue",justify="center")
label_cws.grid(row=1,column=6)

cws_var  = StringVar(metgram_frame)
cws_var.set(next(iter(loc_dict)))
cws_opt = OptionMenu(metgram_frame, cws_var, *loc_dict.keys())
cws_opt.config(width=10, font=('Arial', 12))
cws_opt.grid(row=2,column=6,columnspan=1, sticky = "w")

label_days = Label(metgram_frame,text="Days", font=('Arial', 12),bg="ivory2", fg="blue",justify="center")
label_days.grid(row=1,column=5)

label_cor = Label(metgram_frame,text="Lat , Lon", font=('Arial', 12),bg="ivory2", fg="blue",justify="center")
label_cor.grid(row=1,column=1)

days_list = range(1,6)
days_var  = StringVar(metgram_frame)
days_var.set(days_list[4])
days_opt = OptionMenu(metgram_frame, days_var, *days_list)
days_opt.config(width=10, font=('Arial', 12))
days_opt.grid(row=2,column=5,columnspan=1, sticky = "w")

label_coords = Label(metgram_frame, text="Coordinates",bg="white", font=('Arial', 12))
label_coords.grid(row=2,column=0, sticky = "e")

coords = Entry(metgram_frame,)
coords.grid(row=2, column=1,columnspan=2, sticky = "w")



#===================================================================================================
#              Functions
#===================================================================================================

# Funtion for plotting products and configurations.
# Funtions and dictionaries are imported from products.py
def plotter(*args):
    global defaults_flag
    product_levels = levels_list
    product_name    = products_var.get()
    products_categories = panel_products_dict.keys()
    category=""
    for cat in products_categories:
        if product_name in panel_products_dict[cat].keys():
            product_levels = panel_products_dict[cat][product_name]["levels"]
            product_level = panel_products_dict[cat][product_name]["default_level"]
            category = cat
    #delete the old option menu list
    levels_opt['menu'].delete(0,'end')
    #load the geo levels list to option menu  list
    for item in product_levels:
        levels_opt['menu'].add_command(label=item,command=tkinter._setit(levels_var,item))
        # levels_var.set(product_levels[0])

    products_folder = output_folder +"/"+ str(date_var.get()) + "/" + str(run_var.get()) + "/"
    print("products_folder:",products_folder)
    # gribs to be used
    gribs           = products_dict[product_name]["gribs"]
    # φορτώνω τις default_values του προϊόντος, αν υπάρχουν, για την πρώτη φορά που επιλέγω το προϊόν.
    if  defaults_flag == True :
        product_level   = panel_products_dict[category][product_name]["default_level"]
        # contours to be used
        contours        = products_dict[product_name]["contours"]
        # coastlines to be used
        coastlines      = products_dict[product_name]["coastlines"]
        # map to be used
        maps            = products_dict[product_name]["map"]
        # legend to be used
        legend          = products_dict[product_name]["legend"]
        # text to be used
        text            = products_dict[product_name]["text"]
        #  set for defaults
        levels_var.set(product_level)
        contours_var.set(contours[0])
        coastlines_var.set(coastlines)
        geoviews_var.set(maps)
        legends_var.set(legend)
        texts_var.set(text)
    else:
        product_level   = str(levels_var.get())
        contours        = products_dict[product_name]["contours"]
        contours[0]     = contours_var.get()
        coastlines      = coastlines_var.get()
        maps            = geoviews_var.get()
        legend          = legends_var.get()
        text            = texts_var.get()
    # powered by metview text
    met_power       = texts_dict["met_power"]
    #define function to return for plotting
    data_to_plot    = products_dict[product_name]["function"]( products_folder, gribs, contours,
                                                               coastlines, maps, legend, text,
                                                               product_level, steps )

    mv.plot(
        data_to_plot,
        organizations_image ,
        mv_image,
        #met_power
        )
    # print(products_folder, gribs, contours,   coastlines, maps, legend, text,  product_level, steps )
    defaults_flag = True
    message_def(product_name + "    " +str(product_levels) + "   " +str(gribs))




# Changes the run time button list  according the choosen run Day
def on_run_bt_change(*args):
    # ECMWF run times list
    run_list = sorted( os.listdir(output_folder+"/"+ str(date_var.get())) ,reverse=True )
    remove_hidden_files(run_list)
    opt['menu'].delete(0,'end')
    for item in run_list:
        opt['menu'].add_command(label=item,command=tkinter._setit(run_var,item))
        run_var.set(run_list[0])


def change_flag(*args):
    global defaults_flag
    defaults_flag = False

# Products button deactivate default values for choosen product, so as to choose other configurations for the product
def on_prods_btn_run(*args):
    global defaults_flag
    defaults_flag = False
    try:
        plotter()
    except Exception as e:
        message.configure(text="Exception: \n{} \n{} ".format(e,traceback.print_exc()))

def return_grib_layout(*args):
    grib_path   = output_folder +"/" + str(date_var.get()) +"/"+ str(run_var.get())+"/"+str(products_var.get())+"/"+str(levels_var.get())
    grib        = os.listdir(grib_path)
    if grib[0].endswith(str(levels_var.get())+".grib"):
        path_to_grib = grib_path + "/" +grib[0]
        data    = mv.read(path_to_grib)
        return data



def return_fields_list(prod,steps):
    pro_levels_path  = output_folder +"/" + str(date_var.get()) +"/"+str(run_var.get()) +"/"+ prod +"/"
    level_folders    = os.listdir(pro_levels_path +"/" )
    remove_hidden_files(level_folders)
    level_folders    = sorted(level_folders,key = int)
    print(level_folders)
    gribs_read       = []
    for x in level_folders:
        if x =="50" or x=="150":
            continue
        grib    = str(os.listdir(pro_levels_path+ "/" + x +"/" )[0])
        # print(grib)
        a       = mv.read( pro_levels_path +"/" + x +"/"+grib)
        a       = mv.read(data=a, step = steps)
        # print(a)
        gribs_read.append(a)
    i=0
    while i < len(gribs_read)-1:
        if i == 0:
            all = gribs_read[i]
        else:
            all = mv.merge(gribs_read[i],all)
        i+=1
    # mv.write(prod+".grib",all)
    return all

# Επιστρέφει τα δεδομένα του grib για τα steps που επιλέγξαμε
def return_grib_datas(prod,steps,levs="0"):
    grib_path   = output_folder +"/" + str(date_var.get()) +"/"+str(run_var.get()) +"/"+ prod +"/"+ levs
    grib        = os.listdir(grib_path)
    if grib[0].endswith(levs+".grib"):
        path_to_grib = grib_path + "/" +grib[0]
        data    = mv.read(path_to_grib)
        data    = mv.read(data =data, step=steps)
        return data

#  Συνάρτηση για cross Section
def cross_section_run(*args):
    # step_var = int(step.get())
    crossline = [38.87,21.06,39.95,23.46] #lat,lon,lat,lon
    if line_coords.get():
        import re
        crossline = re.split('[/ , ]',line_coords.get())
    elif str(from_var.get()) in loc_dict.keys() and str(from_var.get()) in loc_dict.keys():
        origin=str(from_var.get())
        destination=str(to_var.get())
        crossline = loc_dict[origin]+loc_dict[destination]
    # else:
    #     crossline = [38.87,21.06,39.95,23.46] #lat,lon,lat,lon
    print(repr(crossline))
    Horizontal_Axis = mv.maxis(
                              AXIS_TICK_LABEL_HEIGHT = 0.4
                              )

    Vert_axis = mv.maxis(
                      AXIS_TYPE               = "POSITION_LIST",
                      AXIS_TITLE_ORIENTATION  = "VERTICAL",
                      AXIS_TICK_POSITION_LIST = [ 1000,925,850,700,500,300,200 ],
                      AXIS_TICK_LABEL_HEIGHT  = 0.4
                      )
    cross_section_view = mv.mxsectview(
                                          BOTTOM_LEVEL               = 1000,
                                          TOP_LEVEL                  = 150,
                                          INTERPOLATE_VALUES         = "NO",
                                          # LINE                       = [ 37,10,37,35 ],
                                          LINE                       = crossline,
                                          WIND_PARALLEL              = "OFF",
                                          WIND_PERPENDICULAR         = "OFF",
                                          WIND_INTENSITY             = "OFF",
                                          WIND_UNPROJECTED           = "ON",
                                          # WIND_HORIZONTAL_COMPONENT  = "PAR",
                                          LNSP_PARAM                 = 152,
                                          U_WIND_PARAM               = 131,
                                          V_WIND_PARAM               = 132,
                                          W_WIND_PARAM               = 135,
                                          T_PARAM                    = 130,
                                          HORIZONTAL_POINT_MODE      = "INTERPOLATE",
                                          VERTICAL_COORDINATES       = "DEFAULT",
                                          W_WIND_SCALING_FACTOR_MODE = "AUTOMATIC",
                                          LEVEL_SELECTION_TYPE       = "FROM_DATA",
                                          VERTICAL_SCALING           = "LOG",
                                          SUBPAGE_CLIPPING           = "OFF",
                                          SUBPAGE_X_POSITION         = 7.5,
                                          SUBPAGE_Y_POSITION         = 7,
                                          SUBPAGE_X_LENGTH           = 85,
                                          SUBPAGE_Y_LENGTH           = 80,
                                          PAGE_FRAME                 = "OFF",
                                          PAGE_ID_LINE               = "OFF",
                                          SUBPAGE_FRAME              = "ON",
                                          SUBPAGE_FRAME_COLOUR       = "BLACK",
                                          SUBPAGE_FRAME_LINE_STYLE   = "SOLID",
                                          SUBPAGE_FRAME_THICKNESS    = 2,
                                          SUBPAGE_BACKGROUND_COLOUR  = "NONE",
                                          HORIZONTAL_AXIS            = Horizontal_Axis,
                                          VERTICAL_AXIS              = Vert_axis

                                    )
    # load contours
    contours      = contours_dict[cr_1_contours_var.get()]
    contours_2    = contours_dict[cr_2_contours_var.get()]
    contours_3    = contours_dict[contours_var.get()]
    # load coastlines
    coastlines    = coastlines_dict[coastlines_var.get()]
    # load geoviews and maps
    # maps        = geoviews_dict[geoviews_var.get()]
    maps = mv.geoview(
        map_area_definition = "corners",
        area                = [ 34,19,43.20,32 ],
        coastlines          = coastlines,
        subpage_y_lenght    = 75
        )
    # define wind plotting style
    wind_style = mv.mwind(
        wind_field_type="flags",
        # wind_thinning_mode="density",
        wind_thinning_factor=1.0,
        # wind_density = 5.0,
        wind_flag_colour="black",
        wind_flag_origin_marker="off",
        wind_flag_length=0.7,
    )
    # add texts on map
    left_map_text        =  Texts.left_cross_map
    right_map_text        =  Texts.right_cross_map
    # text        = texts_dict[texts_var.get()]

    # add legend on map
    # legend      = legends_dict[legends_var.get()]
    legend      =  Legends.cross_sec
    # title = mv.mtext(text_font_size = 0.5)

    # cross section line visualiser
    vis_line = mv.input_visualiser(
        input_plot_type        = "geo_points",
        input_longitude_values = [crossline[1],crossline[3]],
        input_latitude_values  = [crossline[0],crossline[2]]
        )

    graph_line = mv.mgraph(
        graph_line_colour    = "red",
        graph_line_thickness = 4
        )
        # define orography area
    orog_graph = mv.mgraph(
        graph_type         = "area",
        graph_shade_colour  = "charcoal",
    )
    map_page = mv.plot_page(
        bottom = 30,
        view   = maps
        )
    map_page_2 = mv.plot_page(
        bottom = 30,
        left   = 67,
        view   = maps
        )
    xs_page = mv.plot_page(
        top  = 30,
        view = cross_section_view
        )
    dw = mv.plot_superpage(
        pages = [map_page, map_page_2, xs_page]
        )

    level = int(levels_var.get())
    step_select  = int(step.get())
    # get winds
    u = return_fields_list( "U component of wind", str(step_select))
    u = mv.read(data=u, grid=[0.2,0.2])
    v = return_fields_list( "V component of wind", str(step_select))
    v = mv.read(data=v, grid=[0.2,0.2])
    U_V=mv.merge(u, v)

    global data_saved
    if data_saved:
        data_rev = mv.read(data=data_saved, step = step_select ,levelist=level)
    else:
        # data_get = return_grib_layout()
        data_get = return_grib_datas( str(cross_1_var.get()), step_select,str(level))
        data_rev = mv.read(data=data_get, step = step_select ,levelist=level)
    if var1.get()==1:
        all_1 = return_fields_list(cross_1_var.get(),str(step_select))
        all_2 = return_fields_list(cross_2_var.get(),str(step_select))
        all_1_level = mv.read(data=all_1, levelist=level)
        all_2_level = mv.read(data=all_2, levelist=level)
        mv.plot(dw[0], coastlines,all_1_level,contours, vis_line, graph_line ,left_map_text,
                dw[1], coastlines,all_2_level,contours_2, vis_line, graph_line ,right_map_text,
                dw[2], all_1, contours, all_2, contours_2,U_V,wind_style,orog_graph)
    else:
        all_1 = return_fields_list(cross_1_var.get(),str(step_select))
        # all_1 = mv.read(data=all_1, grid=[0.125,0.125])
        all_1_level = mv.read(data=all_1, levelist=level)
        mv.plot(dw[0],coastlines,all_1_level,contours, vis_line, graph_line ,left_map_text,legend,
                dw[1],coastlines,data_rev,contours_3, vis_line, graph_line ,right_map_text,legend,
                dw[2], all_1, contours,orog_graph,U_V,wind_style)

# Συνάρτηση για meteograms
def metgram_def(coords_list,days,cw_name):
    days        = days
    hours       = str(24*days+3)
    steps = [ "3","to",hours,"by","3" ]

    #================================================ υγρασία ================================================

    delta = 0.3
    # The vertical hovmoeller module takes an area as an input.
    # We define the location by shrinking down the area to a point,
    # using a delta adjusted to the grid resolution (0.5x0.5 degrees)
    loc = coords_list # lat/lon Larisa
    # loc = [39.65, 22.46]  # lat/lon Larisa
    # loc = [40, 22]  # lat/lon
    # loc = [39.36, 21.42]  # lat/lon Argithea
    area = [loc[0] + delta, loc[1] - delta, loc[0] - delta, loc[1] + delta]  # N/W/S/E

    # read relative humidity, u and v fields
    r= return_fields_list("Relative humidity",steps)
    u= return_fields_list("U component of wind",steps)
    v= return_fields_list("V component of wind",steps)

    # compute vertical hovmoeller data
    hv_r = mv.mhovmoeller_vertical(data=r, area=area)
    hv_u = mv.mhovmoeller_vertical(data=u, area=area)
    hv_v = mv.mhovmoeller_vertical(data=v, area=area)

    # combine u and v into the same data unit so that we can
    # plot wind into the hovmoeller diagram.
    mv.write("_hv_u.nc", hv_u)
    mv.write("_hv_v.nc", hv_v)
    ds_u = xr.open_dataset("_hv_u.nc")
    ds_v = xr.open_dataset("_hv_v.nc")
    ds = xr.merge([ds_u, ds_v])
    ds.to_netcdf("_hv_wind.nc")
    hv_wind = mv.read("_hv_wind.nc")
    # print(mv.values(hv_wind))


    # # RH_1 = mv.mcont(
    # r_cont = mv.mcont(
    #    LEGEND                       = "ON",
    #    CONTOUR                      = "OFF",
    #    CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
    #    CONTOUR_LEVEL_LIST           = [70,80,90,100,110 ],
    #    CONTOUR_LABEL_HEIGHT         = 0.3,
    #    CONTOUR_SHADE                = "ON",
    #    CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
    #    CONTOUR_SHADE_METHOD         = "AREA_FILL",
    #    CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.9333,0.9333,0.9333)","RGB(0.7176,0.7176,0.7176)","RGB(0.3825,0.2906,0.98)","RGB(0.1169,0.005676,0.959)","RGB(0.0107,0.3957,0.8991)","RGB(0.06621,0.6375,0.9926)","RGB(0.01176,1,0.4894)","RGB(0.06862,1,0.01961)","RGB(0.6514,1,0.003922)","RGB(0.9205,0.9687,0.003815)" ]
    #    )


    # RH_1 = mv.mcont(
    r_cont = mv.mcont(
           LEGEND                       = "ON",
           CONTOUR                      = "OFF",
           CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
           CONTOUR_LEVEL_LIST           = [ 70,80,90,100,120 ],
           CONTOUR_LABEL                = "OFF",
           CONTOUR_SHADE                = "ON",
           CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
           CONTOUR_SHADE_METHOD         = "AREA_FILL",
           CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.5475,0.6913,0.9583)","RGB(0.3971,0.5968,0.9676)","RGB(0.2112,0.4806,0.981)","RGB(0.01564,0.3588,0.9961)" ]
           )



    # define wind plotting style
    wind_style = mv.mwind(
        WIND_FIELD_TYPE          ="flags",
        WIND_THINNING_FACTOR     = 1.00,
        WIND_FLAG_CALM_INDICATOR = "OFF",
        WIND_FLAG_COLOUR         = "BLACK",
        WIND_FLAG_LENGTH         = 0.5,
        WIND_FLAG_ORIGIN_MARKER  = "OFF",
        WIND_FLAG_THICKNESS      = 1.5,
        # WIND_ADVANCED_METHOD     = "ON",          #ta kanei xromatista
        # wind_flag_min_speed      = 8.00,
        # legend = "on"
    )

    # set up the hovmoeller vertical view as a cartesian view
    horizontal_axis = mv.maxis(
        axis_type="date",
        axis_date_type="hours",
        axis_tick_label_height=0.3,
        axis_tick_label_frequency=1,
        axis_grid                = "ON",
        axis_grid_line_style   = "DOT",
        axis_grid_colour       = "GREY",
        axis_days_label_height=0.3,
        axis_hours_label="on",
        axis_hours_label_quality="high",
        axis_hours_label_height=0.2
    )

    vertical_axis = mv.maxis(
        axis_title_text="Pressure (hPa)",
        axis_title_height=0.4,
        axis_grid                = "ON",
        axis_grid_line_style   = "DOT",
        axis_grid_colour       = "GREY",
        axis_tick_label_height=0.3
    )

    view_h = mv.cartesianview(
        x_automatic="on",
        x_axis_type="date",
        y_min=1000,
        y_max=200,
        horizontal_axis=horizontal_axis,
        vertical_axis=vertical_axis,
    )

    # the hovmoeller data is in a NetCDF format. We use
    # netcdf visualisers to plot them into the cartesian view
    nv_r = mv.netcdf_visualiser(
        netcdf_plot_type="xy_matrix",
        netcdf_x_variable="time",
        netcdf_y_variable="vertical",
        netcdf_value_variable="r",
        netcdf_data=hv_r,
    )

    nv_wind = mv.netcdf_visualiser(
        netcdf_plot_type="xy_matrix_vectors",
        netcdf_x_variable="time",
        netcdf_y_variable="vertical",
        netcdf_x_component_variable="u",
        netcdf_y_component_variable="v",
        netcdf_data=hv_wind,
    )

    # define legend
    legend = mv.mlegend(legend_text_font_size=0.4, legend_text_colour="charcoal")

    # define title
    date = mv.base_date(r[0]).strftime("%Y-%m-%d %H:%M")
    title = mv.mtext(
        text_font_size=0.4,
        text_lines=[
            cw_name +" Wind + Relative humidity",
            f"Run={date} UTC Lat={loc[0]} Lon={loc[1]}",
        ],
        text_colour="charcoal",
    )


    #============================================= θερμοκρασία ================================================

    # read a set of t2m and t2d forecast steps from a GRIB file
    t2m = return_grib_datas("2 metre temperature",steps)
    # filter the t2m into separate fieldsets (and K->C)
    t2m = mv.read(data = t2m, param = "2t",step=steps) - 273.15

    # for each temperature type, get the weighted averages over an area
    # - returns a list of numbers, one for each field
    t2m_int = mv.integrate(t2m, area)

    # get the valid times for each field
    times_t2m = mv.valid_date(t2m)

    # set up the Cartesian view to plot into
    # including customised axes so that we can change the size
    # of the labels and add titles
    haxis = mv.maxis(
                    axis_type = "date",
                    axis_date_type="hours",
                    axis_grid                = "ON",
                    axis_grid_line_style   = "DOT",
                    axis_grid_colour       = "GREY",
                     # axis_months_label_height = 0.45,
                     # axis_years_label_height = 0.45,
                     # axis_days_label_height = 0.45,
                    axis_hours_label="on",
                    # axis_hours_label_quality="high",
                    # axis_hours_label_height=0.2
                     )

    vaxis = mv.maxis(
                    axis_title_text = "Temperature",
                    axis_grid                = "ON",
                    axis_grid_line_style   = "DOT",
                    axis_grid_colour       = "GREY",
                    axis_title_height = 0.4
                     )

    ts_view = mv.cartesianview(
                                x_automatic = "on",
                                x_axis_type = "date",
                                y_automatic = "on",
                                horizontal_axis = haxis,
                                vertical_axis   = vaxis
                                )

    # create the curves for both parameters
    curve_2t = mv.input_visualiser(
                                input_x_type        = "date",
                                input_date_x_values = times_t2m,
                                input_y_values      = t2m_int
                                )


    # set up visual styling for each curve
    common_graph = {"graph_line_thickness" : 2, "legend" : 'on'}
    graph_2t = mv.mgraph(
                        common_graph, graph_line_colour = 'green',
                        legend_user_text = 't2m'
                        )

    # customise the legend
    legend = mv.mlegend(
                        legend_display_type = "disjoint",
                        legend_text_font_size = 0.4
                        )

    #=============================================  υετός ==================================================

    # read a set of preci forecast steps from a GRIB file
    preci_dat = return_grib_datas("Total precipitation",steps)
    # preci = preci_def(preci)#/100
    fields  = int( mv.count(preci_dat) )
    preci   = (preci_dat[1:fields] - preci_dat[0:fields-1])*1000

    # for each temperature type, get the weighted averages over an area
    # - returns a list of numbers, one for each field
    preci_int = mv.integrate(preci, area)

    # get the valid times for each field
    times_preci= mv.valid_date(preci)
    # print(times_preci)

    # set up the axis for the cartesian view
    v_axis = mv.maxis(
                        axis_title_text        = "Precipitation",
                        axis_tick_label_height = 0.30,
                        # axis_orientation       = "VERTICAL",
                        # axis_type              = "REGULAR",
                        # axis_tick_label_colour = "NAVY",
                        # axis_grid_thickness    = 1,
                        axis_grid              = "ON",
                        axis_grid_line_style   = "DOT",
                        axis_grid_colour       = "GREY"
                        )

    h_axis = mv.maxis(
                        axis_orientation         = "HORIZONTAL",
                        axis_grid_thickness      = 1,
                        axis_type                = "DATE",
                        axis_date_type           ="hours",
                        axis_grid                = "ON",
                        axis_grid_line_style     = "DOT",
                        axis_grid_colour         = "GREY",
                        # axis_months_label_height = 0.40,
                        # axis_years_label_height  = 0.50,
                        # axis_days_label_height   = 0.40,
                        axis_hours_label="on",
                        # axis_hours_label_quality="high",
                        # axis_hours_label_height=0.2
                        )

    my_view = mv.cartesianview(
                                x_automatic = "on",
                                x_axis_type = "date",
                                # y_automatic = "on",
                                # x_automatic = "on",
                               # y_automatic = "on",
                               # y_axis_type     = "regular",
                               y_min           = 0,
                               y_max           = 10,
                               horizontal_axis = h_axis,
                               vertical_axis   = v_axis,
                               # subpage_y_length= 70
                               )


    # define second set of input vectors to plot
    my_input2 = mv.input_visualiser(
                                    # input_plot_type      = "xy_area",
                                    input_x_type         = "date",
                                    input_y_values       = preci_int,
                                    input_date_x_values      = times_preci
                                    )

    # set up a bar plot for the second set
    my_graph2 = mv.mgraph(
                            graph_type                       = "BAR",
                          graph_shade_colour               = "BLUE",
                          graph_bar_annotation_font_colour = "CHARCOAL",
                          graph_bar_justification          = "CENTRE",
                          graph_bar_width                  = 1*3600,
                          graph_bar_annotation_font_size   = 0.30,
                          # graph_bar_annotation             = ["<font colour='evergreen'>Using bar style</font>"],
                          # legend_user_text                 = " ",
                          legend                           = "ON"
                          )

    # set up the title
    my_title = mv.mtext(
                        text_font_size     = 0.4,
                        text_lines         = ["Total Precipitation"],
                        text_justification = "CENTRE",
                        text_colour        = "CHARCOAL")
    # εικόνα ΠΜΚ
    organizations_image=mv.mimport(
        import_file_name    = "pmk_1.png",
        import_x_position   = 1,
        import_y_position   = 9,
        import_width        = 1,
        import_height       = 1

        )


    page_h = mv.plot_page(
        top=5, bottom=50, left=1, right=100,
        view   = view_h
    )


    page_preci = mv.plot_page(
        top=53, bottom=73, left=1, right=100,
        view   = my_view
    )

    page_temp = mv.plot_page(
        top=76, bottom=96, left=1, right=100,
        view   = ts_view
    )


    dw = mv.plot_superpage(
        # the order of these pages is used when indexing them in the plot() command
        pages = [ page_h, page_preci, page_temp]
    )

    mv.plot(dw[0], nv_r, r_cont, nv_wind, wind_style, legend, title,organizations_image,
            dw[1], my_input2,my_graph2,my_title,
            dw[2], curve_2t, graph_2t, legend
            )

    os.remove("_hv_u.nc")
    os.remove("_hv_v.nc")
    os.remove("_hv_wind.nc")

#date_list =[str(today)]
date_list =sorted( os.listdir(output_folder) ,reverse=True )
remove_hidden_files(date_list)

# δίνει τα ορίσματα για να καλέσει το μετεώγραμμα
def metgram_run(*args):
    cw_name   = str(cws_var.get())
    cw   = loc_dict[cw_name]
    days = int(days_var.get())
    print(cw,days)
    message_def(cw_name+"  "+str(days)+" days meteogram")
    metgram_def(cw,days,cw_name)

def metg_by_coords_def():
    days = int(days_var.get())
    if coords.get():
        coords_ = coords.get().split(",")
        coords_ =[float(i) for i in coords_]
        print(coords_)
        message_def(coords.get())
        metgram_def(coords_,days,"Unonymous")
    else:
        message_def("  Πρέπει να δώσετε συντεταγμένες σημείου lat,lon πχ: 39.36, 21.42  ")


def message_def(mes):
     message.configure(text="{}".format( mes ))


# def open_metgrams():
#     # os.system("/home/metview/metview/System/Pythonics/meteogramma.py 1")
#     subprocess.Popen("/home/metview/metview/System/Pythonics/meteogramma.py",shell=False)

#===================================================================================================
#           κλήσεις συναρτήσεων από κουμπιά
#===================================================================================================

#levels_var.trace("w", runner)
products_var.trace("w", plotter)
# run_var.trace("w", on_run_bt_change)
date_var.trace("w", on_run_bt_change)
contours_var.trace("w", change_flag)
levels_var.trace("w", change_flag)
cws_var.trace("w", metgram_run)

products_button = Button( root,text="Products", font=('Arial', 12), fg="blue", justify="center",width=40,command = on_prods_btn_run )
products_button.grid( row=1,column=2,columnspan=3 )


cross_section_button = Button( cross_section_frame ,text="Create Cross Section", font=('Arial', 14), fg="orange", justify="center",width=40,command = cross_section_run )
cross_section_button.grid( row=7,column=2,columnspan=4,padx=5,pady=5 )

metg_button = Button( metgram_frame,text="Met by coords", font=('Arial', 12), fg="blue", justify="center",width=10,command = metg_by_coords_def )
metg_button.grid( row=2,column=4 )

# meteogram_button = Button( root ,text="Meteogram", font=('Arial', 12), fg="black", justify="center",width=10,command = open_metgrams )
# meteogram_button.grid( row=4,column=5,padx=5,pady=5 )




#===================================================================================================
root.mainloop()
