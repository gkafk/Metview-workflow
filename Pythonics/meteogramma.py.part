# (C) Copyright 2017- ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
#

import metview as mv
import xarray as xr
import os
import tkinter
from tkinter import *

output_folder = "/home/george/data/output"
# date_var    = "20210516"
# run_var     = "1200"
levels_var  = "0"

# steps1 = [ format(x,"2d") for x in range(3,120,3) ]
# print(steps1)

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

# συνάρτηση για total precipitation
def preci_def(dat):
    fields  = int( mv.count(dat) )
    dat     = (dat[1:fields] - dat[0:fields-1])*1000
    return dat

# συνάρτηση για να σβήνει κρυφά αρχεία κτλ από λίστα
def remove_hidden_files(lista):
    for item in lista[:]:
        if item.startswith(".") or "ERROR" in item:
            lista.remove(item)

def return_grib_data(prod,steps,levs="0"):
    grib_path   = output_folder +"/" + str(date_var.get()) +"/"+str(run_var.get()) +"/"+ prod +"/"+ levs
    grib        = os.listdir(grib_path)
    if grib[0].endswith(levs+".grib"):
        path_to_grib = grib_path + "/" +grib[0]
        data    = mv.read(path_to_grib)
        data    = mv.read(data =data, step=steps)
        return data

def return_fields_list(prod,steps):
    # pro_levels_path  = output_folder +"/" + date_var +"/"+ run_var +"/"+ prod +"/"
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
    
    
    # RH_1 = mv.mcont(
    r_cont = mv.mcont(
       LEGEND                       = "ON",
       CONTOUR                      = "OFF",
       CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
       CONTOUR_LEVEL_LIST           = [70,80,90,100,110 ],
       CONTOUR_LABEL_HEIGHT         = 0.3,
       CONTOUR_SHADE                = "ON",
       CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
       CONTOUR_SHADE_METHOD         = "AREA_FILL",
       CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.9333,0.9333,0.9333)","RGB(0.7176,0.7176,0.7176)","RGB(0.3825,0.2906,0.98)","RGB(0.1169,0.005676,0.959)","RGB(0.0107,0.3957,0.8991)","RGB(0.06621,0.6375,0.9926)","RGB(0.01176,1,0.4894)","RGB(0.06862,1,0.01961)","RGB(0.6514,1,0.003922)","RGB(0.9205,0.9687,0.003815)" ]
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
    t2m = return_grib_data("2 metre temperature",steps)
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
    preci = return_grib_data("Total precipitation",steps)
    preci = preci_def(preci)#/100
    
    # for each temperature type, get the weighted averages over an area
    # - returns a list of numbers, one for each field
    preci_int = mv.integrate(preci, area)
    print("preci int",preci_int)
    
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
                               y_max           = 90,
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
    pmk_image=mv.mimport(
        import_file_name    = "pmk.png",
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
    
    mv.plot(dw[0], nv_r, r_cont, nv_wind, wind_style, legend, title,pmk_image,
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
        message_def(" Πρέπει να δώσετε συντεταγμένες σημείου lat,lon πχ: 39.36, 21.42 ")    
    
    
#λίστα με τις ώρες των τρεξιμάτων του ευρωπαϊκού κέντρου
run_list = ["0000","1200"]

#===================================================================================================
#                Γραφικό περιβάλλον
#===================================================================================================

root = Tk()
root.geometry("400x300")
root.title("METEO ATA Meteograms v2.1")
root.iconphoto(True,PhotoImage(file='meteogram.png'))
# root.call("wm","iconphoto",root._w,PhotoImage(file="/home/metview/metview/System/Pythonics/pmk.png"))


frame_return = Frame(root,bd=2,bg="white",width=400,height=200,relief='sunken',pady=10,padx=10)
frame_return.grid(row=13,column=0,rowspan=10,columnspan=8, sticky = "NESW")



date_run = Label(root,text="Date", font=('Helvetica', 12), fg="blue",justify="center")
date_run.grid(row=1,column=0)

date_var  = StringVar(root)
date_var.set(date_list[0])
date_opt = OptionMenu(root, date_var, *date_list)
date_opt.config(width=12, font=('Helvetica', 12))
date_opt.grid(row=2,column=0)

label_run = Label(root,text="RUN", font=('Helvetica', 12), fg="blue",justify="center")
label_run.grid(row=1,column=1)

run_var  = StringVar(root)
run_var.set(run_list[0])
opt = OptionMenu(root, run_var, *run_list)
opt.config(width=8, font=('Helvetica', 12))
opt.grid(row=2,column=1)

label_run = Label(root,text="CW", font=('Helvetica', 12), fg="blue",justify="center")
label_run.grid(row=1,column=2)

cws_var  = StringVar(root)
cws_var.set(next(iter(loc_dict)))
cws_opt = OptionMenu(root, cws_var, *loc_dict.keys())
cws_opt.config(width=10, font=('Helvetica', 12))
cws_opt.grid(row=2,column=2,columnspan=1, sticky = "w")

label_days = Label(root,text="Days", font=('Helvetica', 12), fg="blue",justify="center")
label_days.grid(row=1,column=3)

days_list = range(1,6)
days_var  = StringVar(root)
days_var.set(days_list[4])
days_opt = OptionMenu(root, days_var, *days_list)
days_opt.config(width=10, font=('Helvetica', 12))
days_opt.grid(row=2,column=3,columnspan=1, sticky = "w")

Label(root, text="Coordinates",bg="white", font=('Helvetica', 12)).grid(row=3,column=0, sticky = "e")
coords = Entry(root)
coords.grid(row=3, column=1,columnspan=2, sticky = "w")

metg_button = Button( root,text="Met by coords", font=('Helvetica', 12), fg="blue", justify="center",width=10,command = metg_by_coords_def )
metg_button.grid( row=3,column=3,columnspan=2 )


message = Message(frame_return,text="Meteograms", font=('Arial', 16), fg='red',bg="white",width=400,justify="left")
message.pack(fill="both")

cws_var.trace("w", metgram_run)


def message_def(mes):
     message.configure(text="{}".format( mes ))
     
root.mainloop()

# if __name__ == '__main__':
#     metgram_def("LGSA",4)