# !/usr/bin/python3
import metview as mv
import xarray as xr
from datetime import datetime
import os,sys
from concurrent.futures import ThreadPoolExecutor
# from multiprocessing import Pool,freeze_support
import traceback
import time as tm
import globalVariables as gbl

# global r,u,v,t2m,preci
# grib files  directory
output_folder   = gbl._OUTPUT_FOLDER

# Images exporting directory
images_folder   = gbl._IMAGES_EXPORT_DIR

today           = datetime.now().strftime("%Y%m%d")

files_to_remove = []

time            =  datetime.now().strftime("%H")


# get Arguments from watchdog call
if sys.argv[1]:
    print("args:",sys.argv)
    _folder         = sys.argv[1]
    _sub_folder     = sys.argv[2]
    products_folder = output_folder +"/"+ _folder +"/"+ _sub_folder + "/"
else:
    products_folder = output_folder +"/"+ today +"/"+ run_folder + "/"



#  Airports dictionary name, Lat,Lon
loc_dict    = gbl._LOCATIONS_DICT

#  total precipitation function
def preci_def(dat):
    fields  = int( mv.count(dat) )
    print("fields: ",fields)
    dat     = (dat[1:fields] - dat[0:fields-1])*1000
    return dat

# function for removing hidden files from a list
def remove_hidden_files(lista):
    for item in lista[:]:
        if item.startswith(".") or "ERROR" in item:
            lista.remove(item)

def return_grib_data(prod,steps,levs="0"):
    grib_path   = products_folder + prod +"/"+ levs
    grib        = os.listdir(grib_path)
    if grib[0].endswith(levs+".grib"):
        path_to_grib = grib_path + "/" +grib[0]
        data    = mv.read(path_to_grib)
        data    = mv.read(data =data, step=steps)
        fields  = int( mv.count(data) )
        # mv.write(prod+".grib",data)
        return data

def return_fields_list(prod,steps):
    pro_levels_path  = products_folder+"/"+ prod +"/"
    level_folders    = os.listdir(pro_levels_path +"/" )
    remove_hidden_files(level_folders)
    level_folders    = sorted(level_folders,key = int)
    print("product: ",prod, "\nlevels: ",level_folders)
    gribs_read       = []
    for x in level_folders:
        if x =="50" or x=="150":
            continue
        grib    = str(os.listdir(pro_levels_path+ "/" + x +"/" )[0])
        a       = mv.read( pro_levels_path +"/" + x +"/"+grib)
        a       = mv.read(data=a, step = steps)
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

# Gets gribs data to variables for all meteograms
# variables have to be globalVariables
# The function's argument is the number of days for the meteogram
def collect_data(days):
    print("Collecting data from products.")
    hours       = str(24*days+3)
    steps       = [ "3","to",hours,"by","3" ]
    # read the gribs
    global r,u,v,t2m,preci
    r           = return_fields_list("Relative humidity",steps)
    u           = return_fields_list("U component of wind",steps)
    v           = return_fields_list("V component of wind",steps)
    # read a set of t2m and t2d forecast steps from a GRIB file
    t2m         = return_grib_data("2 metre temperature",steps)
    # filter the t2m into separate fieldsets (and K->C)
    t2m         = mv.read(data = t2m, param = "2t",step=steps) - 273.15
    # read a set of preci forecast steps from a GRIB file
    preci       = return_grib_data("Total precipitation",steps)
    preci       = preci_def(preci)#/100


# Producing meteograms
# Arguments: [lat,lon], days number, Point name
def metgram_def(_list):
    coords_list = _list[0]
    days        = _list[1]
    cw_name     = _list[2]
    print(datetime.now()," - Constructing the meteogram of ",cw_name," for ",days," days")
    hours       = str(24*days+3)
    steps       = [ "3","to",hours,"by","3" ]
    global r,u,v,t2m,preci
    #================================================ υγρασία ================================================

    delta = 0.3
    # The vertical hovmoeller module takes an area as an input.
    # We define the location by shrinking down the area to a point,
    # using a delta adjusted to the grid resolution (0.5x0.5 degrees)
    loc = coords_list # lat/lon
    area = [loc[0] + delta, loc[1] - delta, loc[0] - delta, loc[1] + delta]  # N/W/S/E

    # compute vertical hovmoeller data
    try:
        hv_r = mv.mhovmoeller_vertical(data=r, area=area)
        hv_u = mv.mhovmoeller_vertical(data=u, area=area)
        hv_v = mv.mhovmoeller_vertical(data=v, area=area)
    except Exception as e:
        print(e,traceback.print_exc())
    # combine u and v into the same data unit so that we can
    # plot wind into the hovmoeller diagram.
    u_tmp       = cw_name + "_hv_u.nc"
    files_to_remove.append(u_tmp)
    v_tmp       = cw_name + "_hv_v.nc"
    files_to_remove.append(v_tmp)
    wind_tmp    = cw_name + "_hv_v.nc"
    files_to_remove.append(wind_tmp)
    mv.write(u_tmp, hv_u)
    mv.write(v_tmp, hv_v)
    ds_u        = xr.open_dataset(u_tmp)
    ds_v        = xr.open_dataset(v_tmp)
    ds          = xr.merge([ds_u, ds_v])
    ds.to_netcdf(wind_tmp)
    hv_wind     = mv.read(wind_tmp)


    r_cont      = mv.mcont(
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
    wind_style  = mv.mwind(
        WIND_FIELD_TYPE             = "flags",
        WIND_THINNING_FACTOR        = 1.00,
        WIND_FLAG_CALM_INDICATOR    = "OFF",
        WIND_FLAG_COLOUR            = "BLACK",
        WIND_FLAG_LENGTH            = 0.5,
        WIND_FLAG_ORIGIN_MARKER     = "OFF",
        WIND_FLAG_THICKNESS         = 1.5,
        # WIND_ADVANCED_METHOD      = "ON",          #colourful
        # wind_flag_min_speed       = 8.00,
        # legend = "on"
    )

    # set up the hovmoeller vertical view as a cartesian view
    horizontal_axis = mv.maxis(
        axis_type                   = "date",
        axis_date_type              = "hours",
        axis_tick_label_height      = 0.3,
        axis_tick_label_frequency   = 1,
        axis_grid                   = "ON",
        axis_grid_line_style        = "DOT",
        axis_grid_colour            = "GREY",
        axis_days_label_height      = 0.3,
        axis_hours_label            = "on",
        axis_hours_label_quality    = "high",
        axis_hours_label_height     = 0.2
    )

    vertical_axis   = mv.maxis(
        axis_title_text             = "Pressure (hPa)",
        axis_title_height           = 0.4,
        axis_grid                   = "ON",
        axis_grid_line_style        = "DOT",
        axis_grid_colour            = "GREY",
        axis_tick_label_height      = 0.3
    )

    view_h          = mv.cartesianview(
        x_automatic                 = "on",
        x_axis_type                 = "date",
        y_min                       = 1000,
        y_max                       = 200,
        horizontal_axis             = horizontal_axis,
        vertical_axis               = vertical_axis,
    )

    # the hovmoeller data is in a NetCDF format. We use
    # netcdf visualisers to plot them into the cartesian view
    nv_r            = mv.netcdf_visualiser(
        netcdf_plot_type            = "xy_matrix",
        netcdf_x_variable           = "time",
        netcdf_y_variable           = "vertical",
        netcdf_value_variable       = "r",
        netcdf_data                 = hv_r,
    )

    nv_wind         = mv.netcdf_visualiser(
        netcdf_plot_type            = "xy_matrix_vectors",
        netcdf_x_variable           = "time",
        netcdf_y_variable           = "vertical",
        netcdf_x_component_variable = "u",
        netcdf_y_component_variable = "v",
        netcdf_data                 = hv_wind,
    )

    # define legend
    legend          = mv.mlegend(
        legend_text_font_size       = 0.4,
        legend_text_colour          = "charcoal"
        )

    # define title
    date                = mv.base_date(r[0]).strftime("%Y-%m-%d %H:%M")
    title               = mv.mtext(
        text_font_size  = 0.4,
        text_lines      = [
                            cw_name +" Wind + Relative humidity",
                            f"Run={date} UTC Lat={loc[0]} Lon={loc[1]}",
                            ],
        text_colour     = "charcoal",
    )


    #============================================= Temperature ================================================


    # for each temperature type, get the weighted averages over an area
    # - returns a list of numbers, one for each field
    t2m_int = mv.integrate(t2m, area)

    # get the valid times for each field
    times_t2m = mv.valid_date(t2m)

    # set up the Cartesian view to plot into
    # including customised axes so that we can change the size
    # of the labels and add titles
    haxis = mv.maxis(
                    axis_type           = "date",
                    axis_date_type      = "hours",
                    axis_grid           = "ON",
                    axis_grid_line_style= "DOT",
                    axis_grid_colour    = "GREY",
                     # axis_months_label_height = 0.45,
                     # axis_years_label_height  = 0.45,
                     # axis_days_label_height   = 0.45,
                    axis_hours_label    = "on",
                    # axis_hours_label_quality  = "high",
                    # axis_hours_label_height   = 0.2
                     )

    vaxis = mv.maxis(
                    axis_title_text     = "Temperature",
                    axis_grid           = "ON",
                    axis_grid_line_style= "DOT",
                    axis_grid_colour    = "GREY",
                    axis_title_height   = 0.4
                     )

    ts_view = mv.cartesianview(
                    x_automatic         = "on",
                    x_axis_type         = "date",
                    y_automatic         = "on",
                    horizontal_axis     = haxis,
                    vertical_axis       = vaxis
                    )

    # create the curves for both parameters
    curve_2t = mv.input_visualiser(
                    input_x_type        = "date",
                    input_date_x_values = times_t2m,
                    input_y_values      = t2m_int
                    )


    # set up visual styling for each curve
    common_graph    = {
                        "graph_line_thickness"  : 2,
                        "legend"                : 'on'
                    }
    graph_2t        = mv.mgraph(
                        common_graph, graph_line_colour = 'green',
                        legend_user_text                = 't2m'
                        )

    # customise the legend
    legend          = mv.mlegend(
                        legend_display_type     = "disjoint",
                        legend_text_font_size   = 0.4
                    )

    #=============================================  Precipitation ==================================================

    # for each temperature type, get the weighted averages over an area
    # - returns a list of numbers, one for each field
    preci_int   = mv.integrate(preci, area)

    # get the valid times for each field
    times_preci = mv.valid_date(preci)

    # set up the axis for the cartesian view
    v_axis      = mv.maxis(
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
                        axis_hours_label          = "on",
                        # axis_hours_label_quality="high",
                        # axis_hours_label_height=0.2
                        )

    my_view = mv.cartesianview(
                                x_automatic     = "on",
                                x_axis_type     = "date",
                                # y_automatic   = "on",
                                # x_automatic   = "on",
                               # y_automatic    = "on",
                               # y_axis_type    = "regular",
                               y_min            = 0,
                               y_max            = 20,
                               horizontal_axis  = h_axis,
                               vertical_axis    = v_axis,
                               # subpage_y_length= 70
                               )


    # define second set of input vectors to plot
    my_input2 = mv.input_visualiser(
                                    # input_plot_type      = "xy_area",
                                    input_x_type         = "date",
                                    input_y_values       = preci_int,
                                    input_date_x_values  = times_preci
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


   # ECMWF Logo
    organizations_image     = mv.mimport(
        import_file_name    = "ECMWF_Master_Logo.png",
        import_x_position   = 1,
        import_y_position   = 9,
        import_width        = 2.0,
        import_height       = 0.4
        )

    ## MV Logo
    #mv_image=mv.mimport(
        #import_file_name    = "Metview_logo.png",
        #import_x_position   = 28.0,
        #import_y_position   = 0.3,
        #import_width        = 1.0,
        #import_height       = 0.9
        #)

    # Sub - pages
    page_h  = mv.plot_page(
                        top     = 5,
                        bottom  = 50,
                        left    = 1,
                        right   = 100,
                        view    = view_h
                        )


    page_preci = mv.plot_page(
                        top     = 53,
                        bottom  = 73,
                        left    = 1,
                        right   = 100,
                        view    = my_view
                        )

    page_temp = mv.plot_page(
                        top     = 76,
                        bottom  = 96,
                        left    = 1,
                        right   = 100,
                        view    = ts_view
                        )


    dw = mv.plot_superpage(
        # the order of these pages is used when indexing them in the plot() command
        pages = [ page_h, page_preci, page_temp]
    )

    # images exporting directory
    export_to_folder= images_folder + "meteograms/"+ cw_name
    # image file name
    img_name        = export_to_folder +"/"+ cw_name
    # mkdir if not exists
    if not os.path.exists(export_to_folder):
        os.makedirs(export_to_folder)

    # define the output plot file
    mv.setoutput(
                    mv.png_output(
                                    output_name                         = img_name,
                                    output_width                        = 1000,
                                    output_cairo_transparent_background = "off",
                                    output_name_first_page_number       = "off",
                                    output_cairo_antialias              = "on"
                                    )
                )

    mv.plot(
        dw[0], nv_r, r_cont, nv_wind, wind_style, legend, title, organizations_image,
        dw[1], my_input2, my_graph2, my_title,
        dw[2], curve_2t, graph_2t, legend,
            )

# main running
def main():
    start_time = datetime.now()
    try:
        collect_data(4)
    except Exception as e:
        print(e,traceback.print_exc())
    try:
        for item in loc_dict.keys():
            metgram_def([loc_dict[item], 4, item])
    except Exception as e:
        print(e,traceback.print_exc())
    # Delete netcdf files produced for meteogram
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
    end_time = datetime.now()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - Meteograms production ended in %s seconds" % (end_time - start_time))


if __name__ == '__main__':
    main()
