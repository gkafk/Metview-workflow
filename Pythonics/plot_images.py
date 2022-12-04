# !/usr/bin/python3
import metview as mv
from datetime import datetime
import traceback
import os,sys,multiprocessing
from products import *
import globalVariables as gbl


# Merged grib files folder
output_folder = gbl._OUTPUT_FOLDER

# Images exporting directory
images_folder = gbl._IMAGES_EXPORT_DIR

today = datetime.now().strftime("%Y%m%d")

time  =  datetime.now().strftime("%H")
print(today,time)


# 3 hour steps
time_steps = gbl._STEPS

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

# Creates files in output folder
# Functions and dictionaries are imported from module meteo.py
def export_products(product_name,product_level,steps,folder,subfolder):
    if folder:
        products_folder=output_folder +"/"+ folder +"/"+ subfolder + "/"
    else:
        products_folder=output_folder +"/"+ today +"/"+ run_folder + "/"
    # print("products_folder: ",products_folder," ",products_folder.split("/")[4])
    # gribs to be used
    gribs           = products_dict[product_name]["gribs"]
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
    # powered by metview text
    met_power       = texts_dict["met_power"]
    #define function to return for plotting
    data_to_plot    = products_dict[product_name]["function"]( products_folder, gribs, contours,
                                                               coastlines, maps, legend, text,
                                                               product_level, steps )
    # Products exporting directory
    export_to_folder= images_folder + product_name.replace(" ","_") +"/"+ product_level
    # Image file name
    img_name        = export_to_folder +"/"+ product_name
    # Create folder if not exists
    if not os.path.exists(export_to_folder):
        os.makedirs(export_to_folder)
    # define the output plot file
    mv.setoutput(mv.png_output(
                                output_font_scale=3.0,
                                output_name = img_name,
                                output_file_minimal_width = 2,
                                output_width=1800,
                                output_cairo_transparent_background="on",
                                output_cairo_antialias="on"
                                ) )
    # plot the return
    mv.plot(
        data_to_plot,
        organizations_image ,
        mv_image,
        #met_power
        )
    # print(products_folder, gribs, contours,   coastlines, maps, legend, text,  product_level, steps )

# Images for production
# [Name , geopotential height, steps]
products = gbl._PRODUCTS

if __name__=="__main__":
    # export_products("Static stability","850",time_steps)
    if sys.argv[1]:
        # print("args:",sys.argv)
        _folder=sys.argv[1]
        _sub_folder=sys.argv[2]
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - Start producing forecasting images")
    start_time = datetime.now()
    try:
        processes = []
        for item in products:
            try:
                # export_products(item[0],item[1],item[2],_folder,_sub_folder)
                multi_proc = multiprocessing.Process(target=export_products,args=(item[0],item[1],item[2],_folder,_sub_folder,))
                processes.append(multi_proc)
                multi_proc.start()
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - ", item[0],item[1])
                # multi_proc.join()
            except Exception as e:
                print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - Error in producing ", item[0],item[1])
                print(e,traceback.print_exc())
        for process in processes:
            process.join()
    except Exception as e:
        print(e,traceback.print_exc())
        # pass
    end_time = datetime.now()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - Forecast maps production ended in %s seconds" % (end_time - start_time))
