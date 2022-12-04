# !/usr/bin/python3
'''
Inputs:
1. product's directory, in order to take care of all geopotential heights
2. step in order to choose the 3-hour step
3. line coordinates
'''

import metview as mv
from products import *
import os,sys,multiprocessing
import globalVariables as gbl


# grib files directory
output_folder = gbl._OUTPUT_FOLDER

# images exporting directory
images_folder = gbl._IMAGES_EXPORT_DIR

today = datetime.now().strftime("%Y%m%d")

time  =  datetime.now().strftime("%H")
print(today,time)


# get Arguments from watchdog call
if sys.argv[1]:
    print("args:",sys.argv)
    _folder=sys.argv[1]
    _sub_folder=sys.argv[2]
    products_folder = output_folder +"/"+ _folder +"/"+ _sub_folder + "/"
else:
    products_folder = output_folder +"/"+ today +"/"+ run_folder + "/"


# print(products_folder)

#  Airport coordinates Lat,Lon
loc_dict =gbl._LOCATIONS_DICT

# [From , To , steps*3]
route_list=gbl._ROUTES_LIST

# Function for removing hidden files from list
def remove_hidden_files(lista):
    for item in lista[:]:
        if item.startswith(".") or "ERROR" in item or item is None:
            lista.remove(item)

#
def return_grib_datas(prod,steps,levs="0"):
    grib_path   = products_folder +"/"+ prod +"/"+ levs
    grib        = os.listdir(grib_path)
    if grib[0].endswith(levs+".grib"):
        path_to_grib = grib_path + "/" +grib[0]
        data    = mv.read(path_to_grib)
        data    = mv.read(data =data, step=steps)
        return data



def return_fields_list(prod):
    pro_levels_path  = products_folder +"/"+ prod +"/"
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
        # a       = mv.read(data=a, step = steps)
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
    # if product is sfc (level 0 )
    if len(gribs_read)==1:
        all = gribs_read[i]
    return all

#  Function for producing cross Section
def cross_section_run(r_list,data):
    origin      = r_list[0]
    destination = r_list[1]
    crossline   = loc_dict[origin]+loc_dict[destination]
    steps       = r_list[2]*3
    cw_name     = origin + "-" + destination
    # crossline   = [38.87,21.06,39.95,23.46] #lat,lon,lat,lon
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
                                          HORIZONTAL_POINT_MODE      = "nearest_gridpoint",
                                          # HORIZONTAL_POINT_MODE      = "INTERPOLATE",
                                          VERTICAL_COORDINATES       = "DEFAULT",
                                          W_WIND_SCALING_FACTOR_MODE = "AUTOMATIC",
                                          LEVEL_SELECTION_TYPE       = "FROM_DATA",
                                          VERTICAL_SCALING           = "LOG",
                                          SUBPAGE_CLIPPING           = "OFF",
                                          SUBPAGE_X_POSITION         = 7.5,
                                          SUBPAGE_Y_POSITION         = 7,
                                          SUBPAGE_X_LENGTH           = 88,
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
    contours      = contours_dict["RH_1"]
    contours_2    = contours_dict["geo_60"]
    contours_3    = contours_dict["total_preci_1"]
    # load coastlines
    coastlines    = coastlines_dict["mis"]

    min_lat = min(crossline[0],crossline[2])
    min_lon = min(crossline[1],crossline[3])
    max_lat = max(crossline[0],crossline[2])
    max_lon = max(crossline[1],crossline[3])
    # diff_max_lat = (max_lon - min_lon)/1.7
    # diff_min_lat = (max_lon - min_lon)/-1.4 - 2
    dif_lat = max_lat - min_lat
    dif_lon = max_lon - min_lon

    if dif_lat > dif_lon:
        frame_width= max_lat - min_lat +10
        incr_lat=5
        incr_lon=(frame_width/1.2 - (max_lon-min_lon)/2)
    else:
        frame_len = abs(max_lon - min_lon)+10
        incr_lat = (0.6*frame_len-(max_lat-min_lat))/2
        incr_lon = 5

    # load geoviews and maps
    maps = mv.geoview(
        map_area_definition = "corners",
        #area                = [ 34,19,43.20,32 ],
        # area                = [ 29.93,10.0,51.2,40.0], #S,W,N,E
        area                = [min_lat-incr_lat,min_lon-incr_lon,max_lat+incr_lat,max_lon+incr_lon],
        coastlines          = coastlines,
        SUBPAGE_CLIPPING    = "on",
        subpage_y_lenght    = 75
        )
    # define wind plotting style
    wind_style = mv.mwind(
        wind_field_type="flags",
        # wind_thinning_mode="density",
        # wind_density = 5.0,
        # wind_thinning_mode="thinning",
        wind_thinning_factor= 1.0,
        wind_flag_colour="black",
        wind_flag_origin_marker="off",
        wind_flag_length=0.7,
    )
    # add texts on map
    empty_title     = Texts.empty_title #used to remove default title
    left_map_text   = Texts.left_cross_map
    right_map_text  = Texts.right_cross_map

    # add legend on map
    legend      = Legends.cross_sec

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
    # data
    U_V      = data[0]
    U_V      = mv.read(data=U_V, step=steps)
    rh       = data[1]
    rh       = mv.read(data=rh, step=steps)
    rh_level = data[2]
    rh_level = mv.read(data=rh_level, step=steps)
    preci    = data[3]
    preci = mv.read(data=preci, step=steps)

    # Products exporting directory
    export_to_folder= images_folder + "route_weather/"+ cw_name
    # image file name
    img_name        = export_to_folder +"/"+ cw_name+str(steps)
    # Create folder if not exists
    if not os.path.exists(export_to_folder):
        os.makedirs(export_to_folder)


    organizations_image=mv.mimport(
                                import_file_name    = "ECMWF_Master_Logo.png",
                                import_x_position   = 0.4,
                                import_y_position   = 5,
                                import_width        = 2.0,
                                import_height       = 0.4
                                )

    # define the output plot file
    mv.setoutput(mv.png_output(
                               output_font_scale                    = 3.0,
                               output_name                          = img_name,
                               output_file_minimal_width            = 2,
                               output_width                         = 1800,
                               output_cairo_transparent_background  = "off",
                               output_cairo_antialias               = "on",
                               output_name_first_page_number        = "off",
                               ) )

    mv.plot(
            dw[0],coastlines, rh_level, contours, vis_line, graph_line , empty_title, left_map_text, legend, organizations_image,
            dw[1],coastlines, preci,contours_3, vis_line, graph_line ,empty_title, right_map_text, legend,
            dw[2], rh, contours,  U_V, wind_style
            )


def main():
    print("Start producing route weather images ")
    start_time = datetime.now()

    # get data from grib files====================================
    level           = 850
    step_select     = 3
    # get winds
    u               = return_fields_list( "U component of wind")
    u               = mv.read(data=u, grid=[0.2,0.2])
    v               = return_fields_list( "V component of wind")
    v               = mv.read(data=v, grid=[0.2,0.2])
    U_V             = mv.merge(u, v)
    # get cross section data
    rh              = return_fields_list("Relative humidity")
    # rh = mv.read(data=rh, grid=[0.125,0.125])
    rh_level        = mv.read(data=rh, levelist=level)
    preci           = return_fields_list("Total precipitation")
    preci           = preci_compute(preci)

    for item in route_list:
        print(item)
        for istep in range(1,item[2]):
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - ", item[0],item[1], istep*3)
            multi_proc = multiprocessing.Process(target=cross_section_run,args=([item[0],item[1],istep],[U_V,rh,rh_level,preci],))
            multi_proc.start()
            multi_proc.join()


    end_time = datetime.now()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")," - Route weather maps production ended in %s seconds" % (end_time - start_time))



if __name__=="__main__":
    main()
