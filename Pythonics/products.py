# !/usr/bin/python3
'''
Functions and dictionaries for producing images.
'''
import metview as mv
import Contours
import Coastlines
import Geoviews
import Texts
import Legends
import Winds
from datetime import datetime,date,timedelta
import os
# import local modules
import globalVariables as gbl

# Geopotential heights list
levels_steady_list = gbl._LEVELS_STEADY_LIST

output_folder = gbl._OUTPUT_FOLDER

# Cleanig hidden files function
def remove_hidden_files(lista):
    for item in lista[:]:
        if item.startswith(".") or "ERROR" in item:
            lista.remove(item)

# total precipitation function
def preci_compute(dat):
    fields  = int( mv.count(dat) )
    dat     = (dat[1:fields] - dat[0:fields-1])*1000
    return dat

# Wind spdeed function
def wind_compute(u,v):
    dat             = mv.sqrt( u**2 + v**2 )*1.944
    return dat

# define the vector structure for plotting - wind
def wind_barbs_def(u,v):
    v = mv.grib_vectors(
                        type        = "Vector Field",
                        u_component = u,
                        v_component = v
                        )
    return v

# define the vector structure for plotting - wave
def wave_direction_def(wave_height,wave_direction):
    v = mv.grib_vectors(
                        type      = "Polar Field",
                        intensity = wave_height,
                        direction = wave_direction
                        )
    return v

# Return grib data for choosen steps
def return_grib_data(products_folder,name,level,steps):
    grib_path   = products_folder +  name + "/"+ level
    grib        = os.listdir(grib_path)
    if grib[0].endswith(level+".grib"):
        grib    = grib_path + "/" +grib[0]
        data    = mv.read(grib)
        data    = mv.read(data =data, step=steps)
        return data

# Simple def for plotting a single grib
def simple_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    data = return_grib_data( products_folder,gribs[0], level, steps )
    # get contours
    data_contour = contours_dict[contours[0]]
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast, data, data_contour, data_legend, data_txt

# Absolute humidity def
def ah_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    RH = return_grib_data( products_folder,gribs[0], level, steps )
    T  = return_grib_data( products_folder,gribs[1], level, steps )
    ah_formula = ((((2.1674 * 6.112) * RH) * (mv.exp(((17.67 * (T - 273.15)) / (T - 29.65))))) / T)
    # get contours
    data_contour = contours_dict[contours[0]]
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast, ah_formula, data_contour, data_legend, data_txt

# run difference def
def run_dif_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    tod_steps = [ "3","to","108","by","3" ]
    pre_steps = [ "15","to","120","by","3" ]
    print("working_run_folder: ",products_folder)

    #*******************************************************************************
    # find previous run folder
    day_folder          = products_folder.split("/")[4]
    run_time            = products_folder.split("/")[5]
    folder_to_date      = datetime.strptime(day_folder,'%Y%m%d')
    yesterday           = folder_to_date - timedelta(days=1)
    yesterday           = yesterday.strftime("%Y%m%d")
    if run_time=="0000":
        pre_run_day     = yesterday
        pre_run_time    = "1200"
    else:
        pre_run_day     = day_folder
        pre_run_time    = "0000"
    # previous run grib files folder
    previous_run_folder = output_folder +"/"+ pre_run_day +"/"+ pre_run_time + "/"
    if os.path.exists(previous_run_folder):
        print("previous_run_folder: ",previous_run_folder)
    else:
        print(previous_run_folder,"not found in output folder")
        raise FileNotFoundError("previous run folder not found in output folder")
        # return None
    #*******************************************************************************

    # get grib data
    gh_today = return_grib_data( products_folder,gribs[0], level, tod_steps )/1
    gh_previous = return_grib_data( previous_run_folder,gribs[0], level, pre_steps )/1
    print("pre:",gh_previous)
    gh_diff     = gh_today - gh_previous
    gh_diff     = mv.grib_set_long(gh_diff,['paramId',79])
    # get contours
    contour_black  = contours_dict[contours[0]]
    contour_blue   = contours_dict[contours[1]]
    contour_shade  = contours_dict[contours[2]]
    # rest
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast, gh_diff,contour_shade ,gh_today, contour_black,gh_previous, contour_blue ,data_legend, data_txt

# synoptics def
def synoptics_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    t500 = return_grib_data( products_folder,gribs[0], "500", steps )
    t850 = return_grib_data( products_folder,gribs[0], "850", steps )
    gh500= return_grib_data( products_folder,gribs[1], "500", steps )/1
    mslp = return_grib_data( products_folder,gribs[2], "0", steps )/1000
    # get contours
    t500_contour = contours_dict[contours[1]]
    t850_contour = contours_dict[contours[0]]
    gh500_contour= contours_dict[contours[2]]
    mslp_contour = contours_dict[contours[3]]
    # rest
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast,t850,t850_contour, t500,t500_contour,gh500,gh500_contour,mslp,mslp_contour, data_legend, data_txt


# Sea Temperature def
def sst_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    data = return_grib_data( products_folder,gribs[0], level, steps )
    # get contours
    data_contour = contours_dict[contours[0]]
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data, data_contour,  data_coast,data_legend, data_txt

# Cloud base def
def cloud_base_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    data = return_grib_data( products_folder,gribs[0], level, steps )
    # convert meters to feet
    data = data * 3.28084
    # get contours
    data_contour = contours_dict[contours[0]]
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast, data, data_contour, data_legend, data_txt

# 3h lightnings instant def
def lights_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    data    = return_grib_data( products_folder,gribs[0], level, steps )
    # fields  = int( mv.count(data) )
    # data    = data[2:fields] + data[1:fields-1] +  data[0:fields-2]
    data    = data * 4.167
    # get contours
    data_contour = contours_dict[contours[0]]
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast, data, data_contour, data_legend, data_txt

# Zero level def
def zero_level_def(products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    data    = return_grib_data( products_folder,gribs[0], level, steps )
    data    = data * 3.28084
    # get contours
    data_contour = contours_dict[contours[0]]
    data_legend = legends_dict[legend]
    data_map    = geoviews_dict[maps]
    data_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return data_map,  data_coast, data, data_contour, data_legend, data_txt

# σ Temperature with Geopotential heights def
def temperature_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    temp = return_grib_data( products_folder,gribs[0], level, steps )
    geo = return_grib_data( products_folder,gribs[1], level, steps )/1
    # get contours
    temp_contour = contours_dict[contours[0]]
    geo_contour  =contours_dict[contours[1]]
    # rest
    temp_legend = legends_dict[legend]
    temp_map    = geoviews_dict[maps]
    temp_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return temp_map, data_coast, temp, temp_contour,  geo, geo_contour, temp_legend, temp_txt

#   Geopotential heights  with temperature def
def geo_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    geo = return_grib_data( products_folder,gribs[0], level, steps )/1
    temp = return_grib_data( products_folder,gribs[1], level, steps )
    # get contours
    geo_contour  =contours_dict[contours[0]]
    temp_contour = contours_dict[contours[1]]
    # rest
    temp_legend = legends_dict[legend]
    temp_map    = geoviews_dict[maps]
    temp_txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return temp_map, data_coast, temp, temp_contour,  geo, geo_contour, temp_legend, temp_txt

#   RH-VV def
def rh_vv_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    rh = return_grib_data( products_folder,gribs[0], level, steps )
    vv = return_grib_data( products_folder,gribs[1], level, steps )
    # get contours
    rh_contour  =contours_dict[contours[0]]
    vv1_contour = contours_dict[contours[1]]
    vv2_contour = contours_dict[contours[2]]
    # rest
    legend = legends_dict[legend]
    maps    = geoviews_dict[maps]
    txt    = texts_dict[text]
    data_coast  = coastlines_dict[coast]
    return maps, data_coast, rh, rh_contour,  vv, vv1_contour,vv2_contour, legend, txt

#   PT - potential temperature def
def pt_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    pt = return_grib_data( products_folder,gribs[0], level, steps )
    pt = pt*(1000/850)**0.2854
    u  = return_grib_data( products_folder,gribs[1], level, steps )
    v  = return_grib_data( products_folder,gribs[2], level, steps )
    # get winds
    # wind barbs
    vect      =  wind_barbs_def(u,v)
    # vect_data = wind_compute(u,v)
    # get contours
    pt_contour  = contours_dict[contours[0]]
    wind_contour  = contours_dict[contours[1]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts,pt, pt_contour, vect, wind_contour, legends, txt


#   Q-vectors
def q_vectors_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    pt = return_grib_data( products_folder,gribs[0], level, steps )
    u  = return_grib_data( products_folder,gribs[1], level, steps )
    v  = return_grib_data( products_folder,gribs[2], level, steps )
    gh = return_grib_data( products_folder,gribs[3], level, steps )/1
    # compute
    pt = pt*(1000/850)**0.2854
    # get grib's frames
    fields  = int( mv.count(pt) )
    # get all fields
    gradPT= mv.gradient(pt[0:fields])
    gradu = mv.gradient(u[0:fields])
    gradv = mv.gradient(v[0:fields])

    Q1 = -(9.8/pt[0:fields])*(gradu[0:fields*2:2]*gradPT[0:fields*2:2]+gradv[0:fields*2:2]*gradPT[1:fields*2:2])
    Q2 = -(9.8/pt[0:fields])*(gradu[1:fields*2:2]*gradPT[0:fields*2:2]+gradv[1:fields*2:2]*gradPT[1:fields*2:2])

    #scaling
    Q1 = Q1*1E11
    Q2 = Q2*1E11

    # add wind barbs
    vect      =  wind_barbs_def(Q1,Q2)
    # vect_data = wind_compute(u,v)
    # get contours
    pt_contour  = contours_dict[contours[0]]
    gh_contour  = contours_dict[contours[1]]
    w_contour   = winds_dict[contours[2]]

    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts,pt, pt_contour, gh, gh_contour, vect, w_contour, legends, txt


#  total cloud cover def
def tcc_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    hcc = return_grib_data( products_folder,gribs[0], level, steps )
    mcc = return_grib_data( products_folder,gribs[1], level, steps )
    lcc = return_grib_data( products_folder,gribs[2], level, steps )
    # get contours
    hcc_contour  = contours_dict[contours[0]]
    mcc_contour  = contours_dict[contours[1]]
    lcc_contour  = contours_dict[contours[2]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts,hcc, hcc_contour, mcc, mcc_contour, lcc, lcc_contour, legends, txt

#   total precipitation def
def preci_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    preci = return_grib_data( products_folder,gribs[0], level, steps )
    preci   = preci_compute(preci)
    # fields  = int( mv.count(preci) )
    # preci     = (preci[1:fields] - preci[0:fields-1])*1000
    # get contours
    preci_contour  = contours_dict[contours[0]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, preci ,preci_contour,  legends, txt

#  precipitation and snow def
def preci_snow_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    preci = return_grib_data( products_folder,gribs[0], level, steps )
    preci = preci_compute(preci)
    snow  = return_grib_data( products_folder,gribs[1], level, steps )
    snow  = preci_compute(snow)
    # get contours
    preci_contour  = contours_dict[contours[0]]
    snow_contour   = contours_dict[contours[1]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, preci ,preci_contour, snow, snow_contour, legends, txt


#  total precipitation and lightnings def
def preci_lights_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    # get grib data
    steps_6 = [ "0","to","90","by","3" ]
    preci   = return_grib_data( products_folder,gribs[0], level, steps_6 )
    preci   = preci_compute(preci)
    lights  = return_grib_data( products_folder,gribs[1], level, steps )
    # get contours
    preci_contour  = contours_dict[contours[0]]
    light_contour  = contours_dict[contours[1]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, preci ,preci_contour,lights,light_contour, legends, txt

# Η συνάρτηση για τα οπερα
# απαιτούμενα προϊόντα Total precipitation,low cloud coverage,visibility, cloud base height
# def opera_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
#     # get grib data
#     preci   = return_grib_data( products_folder,gribs[0], level, steps )
#     preci   = preci_compute(preci)
#     # fields  = int( mv.count(preci) )
#     # preci   = (preci[1:fields] - preci[0:fields-1])*1000
#     vis     = return_grib_data( products_folder,gribs[1], level, steps )
#     lcc     = return_grib_data( products_folder,gribs[2], level, steps )
#     bas     = return_grib_data( products_folder,gribs[3], level, steps )
#     # get contours
#     preci_contour= contours_dict[contours[0]]
#     vis_contour  = contours_dict[contours[1]]
#     lcc_contour  = contours_dict[contours[2]]
#     bas_contour  = contours_dict[contours[3]]
#     # rest
#     legends      = legends_dict[legend]
#     map_s        = geoviews_dict[maps]
#     txt          = texts_dict[text]
#     coasts       = coastlines_dict[coast]
#     return map_s, coasts,preci, preci_contour, vis, vis_contour, lcc, lcc_contour, bas, bas_contour, legends, txt



#  winds at heights
#  gribs needed "U component of wind","V component of wind"
def opera_winds_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    heights     = ["850","925","1000"]
    u1_level    =  v1_level    = heights[0]
    u2_level    =  v2_level    = heights[1]
    u3_level    =  v3_level    = heights[2]
    # get grib data
    u1   = return_grib_data( products_folder,gribs[0], u1_level, steps )
    v1   = return_grib_data( products_folder,gribs[1], v1_level, steps )
    u2   = return_grib_data( products_folder,gribs[0], u2_level, steps )
    v2   = return_grib_data( products_folder,gribs[1], v2_level, steps )
    u3   = return_grib_data( products_folder,gribs[0], u3_level, steps )
    v3   = return_grib_data( products_folder,gribs[1], v3_level, steps )

    # add wind barbs
    vect_1      =  wind_barbs_def(u1,v1)
    vect_2      =  wind_barbs_def(u2,v2)
    vect_3      =  wind_barbs_def(u3,v3)

    wind_barbs_1  = Winds.wind_plot_850
    wind_barbs_2  = Winds.wind_plot_925
    wind_barbs_3  = Winds.wind_plot_1000

    # wspd m/s to KT calculations
    wspd1       = mv.sqrt(u1**2 + v1**2)*1.944
    wspd2       = mv.sqrt(u2**2 + v2**2)*1.944
    wspd3       = mv.sqrt(u3**2 + v3**2)*1.944

    # convert wspd to integer
    wspd1 = mv.int(wspd1)
    wspd2 = mv.int(wspd2)
    wspd3 = mv.int(wspd3)

    # get contours
    oper_shade_1  = contours_dict[contours[0]]
    oper_shade_2  = contours_dict[contours[1]]
    oper_shade_3  = contours_dict[contours[2]]

    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, vect_3,wind_barbs_3,wspd3,oper_shade_3,vect_2,wind_barbs_2,wspd2,oper_shade_2,vect_1,wind_barbs_1,wspd1,oper_shade_1, legends, txt



# Weather simple
# gribs needed "High cloud cover","Medium cloud cover","Low cloud cover",
# "Total precipitation","Snowfall","10 metre U wind component",
# "10 metre U wind component","2 metre temperature", "Significant height of combined wind waves and swell"
#  contours needed "mis_HCC","mis_MCC","mis_LCC","mis_total_preci","mis_snowfall", "mis_T2m","mis_wave_height"
def mis_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    steps_6 = [ "0","to","75","by","3" ]
    # get grib data
    hcc     = return_grib_data( products_folder,gribs[0], level, steps )
    mcc     = return_grib_data( products_folder,gribs[1], level, steps )
    lcc     = return_grib_data( products_folder,gribs[2], level, steps )
    preci   = return_grib_data( products_folder,gribs[3], level, steps_6 )
    preci   = preci_compute(preci)
    snow    = return_grib_data( products_folder,gribs[4], level, steps_6 )
    snow    = preci_compute(snow)
    v10     = return_grib_data( products_folder,gribs[5], level, steps )
    u10     = return_grib_data( products_folder,gribs[6], level, steps )
    vect    = wind_barbs_def(u10,v10)
    t2m     = return_grib_data( products_folder,gribs[7], level, steps )
    swh     = mv.int(return_grib_data( products_folder,gribs[8], level, steps ))
    # light   = mv.int(return_grib_data( products_folder,gribs[9], level, steps ))* 4.167
    light   = return_grib_data( products_folder,gribs[9], level, steps )* 4.167
    # 2 meter temperature
    # Using  lsm to remove temperature over sea
    lsm         = mv.read("lsm.grib")
    euro        = [ 29.93,10.0,51.2,40.0] #S,W,N,E
    lsm         = mv.read(data=lsm,area=euro)
    t2m         = mv.int(mv.read(data=t2m,area=euro)-273)
    mask        = mv.bitmap(lsm > 0.1, 0)
    t2m         = mv.bitmap(t2m, mask)
    t2m_shade   = Contours.mis_T2m
    # get contours
    hcc_contour  = contours_dict[contours[0]]
    mcc_contour  = contours_dict[contours[1]]
    lcc_contour  = contours_dict[contours[2]]
    preci_contour= contours_dict[contours[3]]
    snow_contour = contours_dict[contours[4]]
    t2m_contour  = contours_dict[contours[5]]
    swh_contour  = contours_dict[contours[6]]
    ligh_contour = contours_dict[contours[7]]
    wind_barbs   = winds_dict["mis"]
    # wind_barbs  = Winds.mis_wind_plot_arrows
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, hcc, hcc_contour,mcc,mcc_contour,lcc,lcc_contour, preci, preci_contour, snow,snow_contour,swh,swh_contour,light, ligh_contour , t2m,t2m_contour,vect,wind_barbs,legends, txt


#   Discomfort Index def
def di_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
     # get grib data
    # steps = [ "3","to","120","by","3" ]
    t2m     = return_grib_data( products_folder,gribs[0], level, steps )
    # Be carefull!!! humidity must be used from folder 1000 - ground level humidity ************************************
    rh      = return_grib_data( products_folder,gribs[1], "1000", steps )
    di      = t2m - 273.15 - 0.4*(t2m - 273.15 -10)*(1 - rh/100)
    # get contours
    di_shade    = contours_dict[contours[0]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, di, di_shade,legends, txt

#  total wave def
def total_wave_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    ht  = return_grib_data( products_folder,gribs[0], level, steps )
    dr  = return_grib_data( products_folder,gribs[1], level, steps )
    vector = wave_direction_def(ht,dr)
    # get contours
    ht_contour  = contours_dict[contours[0]]
    wind_barbs   = winds_dict["wind_wave_plot"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, ht,ht_contour, vector,wind_barbs, legends, txt

#   wind speed def
def wind_speed_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    u_w     = return_grib_data( products_folder,gribs[0], level, steps )
    v_w     = return_grib_data( products_folder,gribs[1], level, steps )
    gh      = return_grib_data( products_folder,gribs[2], level, steps )/1
    data    = wind_compute(u_w,v_w)
    vector  = wind_barbs_def(u_w,v_w)
    # get contours
    wind_contour = contours_dict[contours[0]]
    gh_contour   = contours_dict[contours[1]]
    wind_barbs   = winds_dict["black flags"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, data, wind_contour,gh, gh_contour, vector, wind_barbs, legends, txt

#  wind gust def
def wind_gust_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    gust    = return_grib_data( products_folder,gribs[0], level, steps )*1.944
    u_w     = return_grib_data( products_folder,gribs[1], level, steps )
    v_w     = return_grib_data( products_folder,gribs[2], level, steps )
    vector  = wind_barbs_def(u_w,v_w)
    # get contours
    gust_contour = contours_dict[contours[0]]
    wind_barbs   = winds_dict["black flags"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts,  gust, gust_contour, vector, wind_barbs, legends, txt

#   thermal advection def
def t_adv_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    u_w     = return_grib_data( products_folder,gribs[0], level, steps )
    v_w     = return_grib_data( products_folder,gribs[1], level, steps )
    # data    = wind_compute(u_w,v_w)
    vector  = wind_barbs_def(u_w,v_w)
    temp    = return_grib_data( products_folder,gribs[2], level, steps )
    gh      = return_grib_data( products_folder,gribs[3], level, steps )/1
    # Get  grib's frames
    fields       = int( mv.count(temp) )
    # use all fields
    grad         = mv.gradient(temp[0:fields])
    adv          = - u_w[0:fields]*grad[0:fields*2:2] - v_w[0:fields]*grad[1:fields*2:2]
    # convert per hour
    adv          = adv * 3600
    # get contours
    adv_contour  = contours_dict[contours[0]]
    gh_contour   = contours_dict[contours[1]]
    wind_barbs   = winds_dict["wind_speed_1"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, adv, adv_contour, vector, wind_barbs, gh,gh_contour, legends, txt

#   Potential vorticity def
def pv_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    u_w     = return_grib_data( products_folder,gribs[0], level, steps )
    v_w     = return_grib_data( products_folder,gribs[1], level, steps )
    # data    = wind_compute(u_w,v_w)
    vector  = wind_barbs_def(u_w,v_w)
    pv      = return_grib_data( products_folder,gribs[2], level, steps )
    gh      = return_grib_data( products_folder,gribs[3], level, steps )/1
    # get contours
    pv_contour   = contours_dict[contours[0]]
    gh_contour   = contours_dict[contours[1]]
    wind_barbs   = winds_dict["wind_speed_1"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, pv , pv_contour, vector, wind_barbs, gh,gh_contour, legends, txt

#  isentropic Potential vorticity def
def pv_isentropic_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    u_w     = return_grib_data( products_folder,gribs[0], level, steps )
    v_w     = return_grib_data( products_folder,gribs[1], level, steps )
    # data    = wind_compute(u_w,v_w)
    vector  = wind_barbs_def(u_w,v_w)
    pv      = return_grib_data( products_folder,gribs[2], level, steps )
    # get contours
    pv_contour   = contours_dict[contours[0]]
    wind_barbs   = winds_dict["wind_speed_1"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, pv , pv_contour, vector, wind_barbs, legends, txt

#  Relative vorticity def
def relative_vorticity_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps):
    # get grib data
    rv     = return_grib_data( products_folder,gribs[0], level, steps )
    t      = return_grib_data( products_folder,gribs[1], level, steps )
    gh     = return_grib_data( products_folder,gribs[2], level, steps )/1
    # get contours
    rv_contour   = contours_dict[contours[0]]
    t_contour    = contours_dict[contours[1]]
    gh_contour   = contours_dict[contours[2]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, rv , rv_contour, t,t_contour, gh,gh_contour, legends, txt


#  Thermal wind def
# ["U component of wind","V component of wind"]
def therm_wind_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    heights     = {"300":"500","500":"700","700":"850","850":"925"}
    # compute 2nd height
    level_index = levels_steady_list.index(level)
    if level in heights:
        level_2 = heights[level]
    else:
        level_2 = levels_steady_list[level_index + 2]
    print("u1:",level,"- u2:",level_2)
    # get grib data
    u1     = return_grib_data( products_folder,gribs[0], level, steps )
    v1     = return_grib_data( products_folder,gribs[1], level, steps )
    u2     = return_grib_data( products_folder,gribs[0], level_2, steps )
    v2     = return_grib_data( products_folder,gribs[1], level_2, steps )
    therm_data   = mv.sqrt((u1 -u2)**2 + (v1 - v2)**2)
    vector  = wind_barbs_def(u1 -u2,v1 - v2)
    # get contours
    therm_shade  = contours_dict[contours[0]]
    wind_barbs   = winds_dict["therm_wind"]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, therm_data,therm_shade  , vector, legends,wind_barbs, txt

# static stability def
# Only temperature is needed in different heights
def static_def( products_folder, gribs, contours, coast, maps, legend, text, level, steps ):
    heights     = {"300":"500","500":"700","700":"850","850":"925"}
    # 2nd Height compute
    level_index = levels_steady_list.index(level)
    if level in heights:
        level_2= heights[level]
    else:
        level_2= levels_steady_list[level_index + 2]
    print("t1:",level,"t2",level_2)
    # get grib data
    t1     = return_grib_data( products_folder,gribs[0], level, steps )
    t2     = return_grib_data( products_folder,gribs[0], level_2, steps )
    # convert to t
    t1          = t1*(1000/int(level))**0.2854
    t2          = t2*(1000/int(level_2))**0.2854
    t1_plus_t2  = (t1 - t2)/(int(level_2)-int(level))
    # get contours
    static_shade  = contours_dict[contours[0]]
    # rest
    legends      = legends_dict[legend]
    map_s        = geoviews_dict[maps]
    txt          = texts_dict[text]
    coasts       = coastlines_dict[coast]
    return map_s, coasts, t1_plus_t2,static_shade,  legends, txt


#===================================================================================================
#                               Products configurations
#==================================================================================================

products_dict = {
                    "Temperature":{
                                    "function"  : temperature_def,
                                    "gribs"     : ["Temperature","Geopotential height"],
                                    "contours"  : ["Temp","geo_60_blue"],
                                    "map"       : "Euro polar",
                                    "coastlines": "bold_land",
                                    "legend"    : "large",
                                    "text"      : "temperature",
                                    "wind"      : ""
                                    },

                    "Temperature 500":{
                                    "function"  : temperature_def,
                                    "gribs"     : ["Temperature","Geopotential height"],
                                    "contours"  : ["geo_T_line_1","geo_60_blue"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "black",
                                    "text"      : "temperature",
                                    "wind"      : ""
                                    },

                    "Geopotential Height":{
                                    "function"  : geo_def,
                                    "gribs"     : ["Geopotential height","Temperature"],
                                    "contours"  : ["geo_60_blue","geo_T_line_1"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "temperature",
                                    "wind"      : ""
                                    },



                    "Run Difference":{
                                    "function"  : run_dif_def,
                                    "gribs"     : ["Geopotential height"],
                                    "contours"  : ["geo_60_blue","geo_60","run_difference"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "run_diff",
                                    "wind"      : ""
                                    },



                    "PT":{
                                    "function"  : pt_def,
                                    "gribs"     : ["Temperature","U component of wind","V component of wind"],
                                    "contours"  : ["PT","wspd_1"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "temperature",
                                    "wind"      : ""
                                    },

                    "2 metre temperature":{
                                    "function"  : simple_def,
                                    "gribs"     : ["2 metre temperature"],
                                    "contours"  : ["sfc_T2m_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "black",
                                    "text"      : "left_black",
                                    "wind"      : ""
                                    },

                    "2 metre dewpoint temperature":{
                                    "function"  : simple_def,
                                    "gribs"     : ["2 metre dewpoint temperature"],
                                    "contours"  : ["Td_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "black",
                                    "text"      : "left_black",
                                    "wind"      : ""
                                    },

                    "Visibility":{
                                    "function"  : simple_def,
                                    "gribs"     : ["Visibility"],
                                    "contours"  : ["visibility"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "vis",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                    "Divergence":{
                                    "function"  : simple_def,
                                    "gribs"     : ["Divergence"],
                                    "contours"  : ["ecchart"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                    "Relative humidity":{
                                    "function"  : simple_def,
                                    "gribs"     : ["Relative humidity"],
                                    "contours"  : ["RH_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "bold_land",
                                    "legend"    : "RH",
                                    "text"      : "left_red",
                                    "wind"      : ""
                                    },

                    "Absolute humidity":{
                                    "function"  : ah_def,
                                    "gribs"     : ["Relative humidity","Temperature"],
                                    "contours"  : ["AH_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "AH",
                                    "text"      : "AH",
                                    "wind"      : ""
                                    },

                    "Relative vorticity":{
                                    "function"  : relative_vorticity_def,
                                    "gribs"     : ["Vorticity (relative)","Temperature","Geopotential height"],
                                    "contours"  : ["RV","geo_T_line_1","geo_60_blue"],
                                    "map"       : "Euro polar",
                                    "coastlines": "bold_land",
                                    "legend"    : "relative_vor",
                                    "text"      : "relative_vor",
                                    "wind"      : ""
                                    },

                    "Mean sea level pressure":{
                                    "function"  : simple_def,
                                    "gribs"     : ["Mean sea level pressure"],
                                    "contours"  : ["SFC_MSLP_line_1"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                    "Sea surface temperature":{
                                    "function"  : sst_def,
                                    "gribs"     : ["Sea surface temperature"],
                                    "contours"  : ["SST"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream_land",
                                    "legend"    : "sst",
                                    "text"      : "left_black",
                                    "wind"      : ""
                                    },

                   "Cloud base height" :{
                                    "function"  : cloud_base_def,
                                    "gribs"     : ["Cloud base height"],
                                    "contours"  : ["cloud_base"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Low cloud cover" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["Low cloud cover"],
                                    "contours"  : ["LCC"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Medium cloud cover" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["Medium cloud cover"],
                                    "contours"  : ["MCC"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "High cloud cover" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["High cloud cover"],
                                    "contours"  : ["HCC"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Total cloud cover" :{
                                    "function"  : tcc_def,
                                    "gribs"     : ["High cloud cover","Medium cloud cover","Low cloud cover"],
                                    "contours"  : ["HCC","MCC","LCC"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "clouds",
                                    "text"      : "total_cloud",
                                    "wind"      : ""
                                    },

                   "Total precipitation" :{
                                    "function"  : preci_def,
                                    "gribs"     : ["Total precipitation"],
                                    "contours"  : ["total_preci_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "total_preci",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Preci - Lightnings" :{
                                    "function"  : preci_lights_def,
                                    "gribs"     : ["Total precipitation","L2_Averaged total lightning flash density in the last 3 hours"],
                                    "contours"  : ["total_preci_1","lights_cros"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "total_preci",
                                    "text"      : "preci_lights",
                                    "wind"      : ""
                                    },


                   "Preci - snow" :{
                                    "function"  : preci_snow_def,
                                    "gribs"     : ["Total precipitation","Snowfall"],
                                    "contours"  : ["total_preci_1","snow_dots"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "total_preci",
                                    "text"      : "preci_snow",
                                    "wind"      : ""
                                    },


                   "Snowfall" :{
                                    "function"  : preci_def,
                                    "gribs"     : ["Snowfall"],
                                    "contours"  : ["snowfall_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "snowfall",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                   "Opera winds" :{
                                    "function"  : opera_winds_def,
                                    "gribs"     : ["U component of wind","V component of wind"],
                                    "contours"  : ["opera_w_850","opera_w_925","opera_w_1000"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "opera",
                                    "legend"    : "opera_winds",
                                    "text"      : "opera_winds",
                                    "wind"      : ""
                                    },



                   "Discomfort Index" :{
                                    "function"  : di_def,
                                    "gribs"     : ["2 metre temperature","Relative humidity"],
                                    "contours"  : ["DI"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "mis",
                                    "legend"    : "di",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                   "Total wave" :{
                                    "function"  : total_wave_def,
                                    "gribs"     : ["Significant height of combined wind waves and swell","Mean wave direction"],
                                    "contours"  : ["wave_height"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "meteo",
                                    "legend"    : "tot_wave",
                                    "text"      : "tot_wave",
                                    "wind"      : ""
                                    },


                   "10m Wind speed" :{
                                    "function"  : wind_speed_def,
                                    "gribs"     : ["10 metre U wind component","10 metre V wind component","Mean sea level pressure"],
                                    "contours"  : ["wspd_1","geo_120"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "u10_wind",
                                    "wind"      : ""
                                    },


                   "10m Wind gust" :{
                                    "function"  : wind_gust_def,
                                    "gribs"     : ["L2_10 metre wind gust in the last 3 hours","10 metre U wind component","10 metre V wind component"],
                                    "contours"  : ["wspd_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "bold_land",
                                    "legend"    : "u10_wind_gust",
                                    "text"      : "u10_wind_gust",
                                    "wind"      : ""
                                    },



                   "100m Wind speed" :{
                                    "function"  : wind_speed_def,
                                    "gribs"     : ["100 metre U wind component","100 metre V wind component","Mean sea level pressure"],
                                    "contours"  : ["wspd_1","geo_120_wind"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "u100_wind",
                                    "wind"      : ""
                                    },



                   "Wind speed" :{
                                    "function"  : wind_speed_def,
                                    "gribs"     : ["U component of wind","V component of wind","Geopotential height"],
                                    "contours"  : ["wspd_1","geo_120"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "bold_land",
                                    "legend"    : "wind_speed",
                                    "text"      : "wind_speed",
                                    "wind"      : ""
                                    },



                   "Jet" :{
                                    "function"  : wind_speed_def,
                                    "gribs"     : ["U component of wind","V component of wind","Geopotential height"],
                                    "contours"  : ["wspd_2","geo_120"],
                                    "map"       : "Euro polar",
                                    "coastlines": "bold_land",
                                    "legend"    : "jet",
                                    "text"      : "jet",
                                    "wind"      : ""
                                    },


                   "T-advection" :{
                                    "function"  : t_adv_def,
                                    "gribs"     : ["U component of wind","V component of wind","Temperature","Geopotential height"],
                                    "contours"  : ["T_adv","geo_60_blue"],
                                    "map"       : "Euro polar",
                                    "coastlines": "opera",
                                    "legend"    : "t_advection",
                                    "text"      : "t_advection",
                                    "wind"      : ""
                                    },



                   "Thermal wind" :{
                                    "function"  : therm_wind_def,
                                    "gribs"     : ["U component of wind","V component of wind"],
                                    "contours"  : ["therm_wind"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "therm_wind",
                                    "text"      : "therm_wind",
                                    "wind"      : ""
                                    },

                   "Potential vorticity" :{
                                    "function"  : pv_def,
                                    "gribs"     : ["U component of wind","V component of wind","Potential vorticity","Geopotential height"],
                                    "contours"  : ["PV_1","geo_60_blue"],
                                    "map"       : "Euro polar",
                                    "coastlines": "bold_land",
                                    "legend"    : "PV",
                                    "text"      : "PV",
                                    "wind"      : ""
                                    },

                   "Potential vorticity isentropic" :{
                                    "function"  : pv_isentropic_def,
                                    "gribs"     : ["L2_U component of wind","L2_V component of wind","L2_Potential vorticity"],
                                    "contours"  : ["PV_1"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "PV",
                                    "text"      : "PV",
                                    "wind"      : ""
                                    },


                   "Static stability" :{
                                    "function"  : static_def,
                                    "gribs"     : ["Temperature"],
                                    "contours"  : ["stat_stab"],
                                    "map"       : "Euro polar",
                                    "coastlines": "opera",
                                    "legend"    : "stat_stab",
                                    "text"      : "stat_stab",
                                    "wind"      : ""
                                    },


                   "Q-vectors" :{
                                    "function"  : q_vectors_def,
                                    "gribs"     : ["Temperature","U component of wind","V component of wind","Geopotential height"],
                                    "contours"  : ["PT_Q","GEO_Q","q_vec_arrows"],
                                    "map"       : "Euro polar",
                                    "coastlines": "opera",
                                    "legend"    : "red",
                                    "text"      : "q_vect",
                                    "wind"      : ""
                                    },

                   "MIS" :{
                                    "function"  : mis_def,
                                    "gribs"     : ["High cloud cover","Medium cloud cover","Low cloud cover",
                                                   "Total precipitation","Snowfall","10 metre U wind component",
                                                   "10 metre U wind component","2 metre temperature",
                                                   "Significant height of combined wind waves and swell",
                                                   "L2_Averaged total lightning flash density in the last 3 hours"],
                                    "contours"  : ["MIS_HCC","MIS_MCC","MIS_LCC","mis_total_preci","mis_snowfall",
                                                   "mis_T2m","mis_wave_height","lights_cros"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "mis",
                                    "legend"    : "mis",
                                    "text"      : "mis",
                                    "wind"      : "mis"
                                    },

                   "Lightnings AVG1H" :{
                                    "function"  : lights_def,
                                    # "function"  : simple_def,
                                    "gribs"     : ["L2_Averaged total lightning flash density in the last hour"],
                                    "contours"  : ["light_av1h"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "light_av1h",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Lightnings AVG3H" :{
                                    "function"  : lights_def,
                                    # "function"  : simple_def,
                                    "gribs"     : ["L2_Averaged total lightning flash density in the last 3 hours"],
                                    "contours"  : ["light_av1h"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "light_av1h",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Lightnings radar" :{
                                    "function"  : lights_def,
                                    # "function"  : simple_def,
                                    "gribs"     : ["L2_Averaged total lightning flash density in the last 3 hours"],
                                    "contours"  : ["light_yr"],
                                    "map"       : "lights_radar",
                                    "coastlines": "light_radar",
                                    "legend"    : "light_yr",
                                    "text"      : "light_radar",
                                    "wind"      : ""
                                    },

                   "Lightnings instant" :{
                                    "function"  : lights_def,
                                    # "function"  : simple_def,
                                    "gribs"     : ["L2_Instantaneous total lightning flash density"],
                                    "contours"  : ["light_instant"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "light_instant",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Zero level" :{
                                    "function"  : zero_level_def,
                                    "gribs"     : ["0 degrees C isothermal level (atm)"],
                                    "contours"  : ["zero_level"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "zero_level",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Precipitation type" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["L2_Precipitation type"],
                                    "contours"  : ["preci_type"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "preci_type",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Total precipitation rate" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["L2_Total precipitation rate"],
                                    "contours"  : ["total_preci_rate"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "total_preci_rate",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                   "CAPE" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["Convective available potential energy"],
                                    "contours"  : ["CAPE"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                   "Vertical velocity" :{
                                    "function"  : simple_def,
                                    "gribs"     : ["Vertical velocity"],
                                    "contours"  : ["VV"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "RH-VV" :{
                                    "function"  : rh_vv_def,
                                    "gribs"     : ["Relative humidity","Vertical velocity"],
                                    "contours"  : ["RH_1","VV_pos_line","VV_neg_line"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                   "Large-scale precipitation" :{
                                    "function"  : preci_def,
                                    "gribs"     : ["Large-scale precipitation"],
                                    "contours"  : ["total_preci_1"],
                                    "map"       : "Mediterranean",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },


                   "Convective precipitation" :{
                                    "function"  : preci_def,
                                    "gribs"     : ["Convective precipitation"],
                                    "contours"  : ["total_preci_1"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "red",
                                    "text"      : "left",
                                    "wind"      : ""
                                    },

                   "Synoptics" :{
                                    "function"  : synoptics_def,
                                    "gribs"     : ["Temperature","Geopotential height","Mean sea level pressure"],
                                    "contours"  : ["Temp","geo_T_line_1","geo_60_blue","MSLP_white"],
                                    "map"       : "Euro polar",
                                    "coastlines": "cream",
                                    "legend"    : "black",
                                    "text"      : "synop",
                                    "wind"      : ""
                                    },

                }



#===================================================================================================
#                           Dictionaries
#===================================================================================================

# Contour's dictionary
contours_dict = {
                "ecchart":Contours.ecchart,
                "red_blue":Contours.red_blue, "white_green":Contours.white_green,
                "Temp":Contours.Temp,
                "PT":Contours.PT,
                "sfc_T2m_1":Contours.sfc_T2m_1,"sfc_T2m_2":Contours.sfc_T2m_2,
                "MCC":Contours.MCC, "HCC":Contours.HCC,"LCC":Contours.LCC,
                "MIS_HCC":Contours.mis_HCC,"MIS_LCC":Contours.mis_LCC,"MIS_MCC":Contours.mis_MCC,
                "mis_total_preci":Contours.mis_total_preci,
                "mis_snowfall":Contours.mis_snowfall,
                "mis_T2m":Contours.mis_T2m,
                "mis_wave_height":Contours.mis_wave_height,
                "cloud_base":Contours.cloud_base,
                "PV_1":Contours.PV_1, "PV_2":Contours.PV_2,
                "RV":Contours.RV,
                "RH_1":Contours.RH_1, "RH_2":Contours.RH_2,
                "AH_1":Contours.AH_1, "AH_2":Contours.AH_2,
                "geo":Contours.geo, "geo_60":Contours.geo_60,"geo_60_blue":Contours.geo_60_blue,"geo_120":Contours.geo_120,"geo_120_wind":Contours.geo_120_wind,
                "geo_line":Contours.geo_line,"geo_T_line_1":Contours.geo_T_line_1,
                "SFC_MSLP_line_1":Contours.SFC_MSLP_line_1,"SFC_MSLP_line_2":Contours.SFC_MSLP_line_2,"MSLP_white":Contours.MSLP_white,
                "Td_1":Contours.Td_1,"Td_2":Contours.Td_2,"RV":Contours.RV,
                "VV_pos_line":Contours.VV_pos_line ,"VV_neg_line":Contours.VV_neg_line,"VV":Contours.VV,
                "visibility":Contours.visibility,
                "wave_height":Contours.wave_height,
                "SST":Contours.SST,
                "snowfall_1":Contours.snowfall_1,"snowfall_2":Contours.snowfall_2,"snowfall_3":Contours.snowfall_3,"snow_dots":Contours.snow_dots,
                "wspd_1":Contours.wspd_1,"wspd_2":Contours.wspd_2,"wspd_3":Contours.wspd_3,
                "total_preci_1":Contours.total_preci_1,"lights_cros":Contours.lights_cros,
                "opera_w_850":Contours.opera_w_850, "opera_w_925":Contours.opera_w_925, "opera_w_1000":Contours.opera_w_1000,
                "opera_wave_swh":Contours.opera_wave_swh,"opera_wave_wind":Contours.opera_wave_wind,
                "opera_preci":Contours.opera_preci,"opera_LCC":Contours.opera_LCC,"opera_visibility":Contours.opera_visibility,
                "opera_cloud_base":Contours.opera_cloud_base,
                "CAPE":Contours.CAPE,
                "T_adv_geo":Contours.adv_geo,"T_adv":Contours.adv,
                "stat_stab":Contours.stat_stab,
                "therm_wind":Contours.therm_wind,
                "light_av1h":Contours.light_av1h,
                "light_instant":Contours.light_instant,
                "light_yr":Contours.light_yellow_red,
                "light_mis":Contours.light_mis,
                "zero_level":Contours.zero_level,
                "preci_type":Contours.preci_type,
                "total_preci_rate":Contours.total_preci_rate,
                "DI":Contours.di,
                "run_difference":Contours.run_difference,
                "PT_Q":Contours.PT_Q, "GEO_Q":Contours.GEO_Q,
                "wind_chill_0":Contours.wind_chill_0, "wind_chill_m15":Contours.wind_chill_m15, "wind_chill_wspd":Contours.wind_chill_wspd,
                "wind_chill_wave":Contours.wind_chill_wave, "wind_chill_Tsea":Contours.wind_chill_Tsea,
                }


# text's dictionary
texts_dict    = {
                "white":Texts.white,"black":Texts.black,"blue":Texts.blue,"red":Texts.red,
                "green":Texts.green,"purple":Texts.purple,"yellow":Texts.yellow,
                "met_power":Texts.met_power,
                "synop":Texts.synop,
                "temperature":Texts.temperature,
                "left":Texts.left,"left_black":Texts.left_black,"left_red":Texts.left_red,
                "preci_snow":Texts.preci_snow, "preci_lights":Texts.preci_lights,
                "mis":Texts.mis_txt,
                "opera":Texts.opera,"opera_winds":Texts.opera_winds,"opera_wave":Texts.opera_wave,
                "total_cloud":Texts.total_cloud,
                "tot_wave":Texts.tot_wave,
                "wind_speed":Texts.wind_speed,"u10_wind":Texts.u10_wind,"u100_wind":Texts.u100_wind,"jet":Texts.jet,
                "u10_wind_gust":Texts.u10_wind_gust,
                "PV":Texts.pv,
                "AH":Texts.AH,
                "relative_vor":Texts.relative_vor,
                "t_advection":Texts.t_advection,
                "q_vect":Texts.q_vect,
                "stat_stab":Texts.stat_stab,
                "run_diff":Texts.run_diff,
                "therm_wind":Texts.therm_wind,
                "light_radar":Texts.light_radar
              }


# Maps's dictionary
geoviews_dict = {
                "Euro polar":Geoviews.euro_polar,
                "Europe":Geoviews.euro_cyli,
                "Mediterranean":Geoviews.mediterra,
                "Hellas":Geoviews.greece,
                "lights_radar":Geoviews.lights_radar,
                }

# Legend's dictionary
legends_dict  = {
                "white":Legends.white,"black":Legends.black,"blue":Legends.blue,
                "red":Legends.red,"green":Legends.green,"purple":Legends.purple,"yellow":Legends.yellow,
                "large":Legends.large,
                "cross_sec":Legends.cross_sec,
                "clouds":Legends.clouds,
                "vis":Legends.vis,
                "relative_vor":Legends.relative_vor,
                "RH":Legends.RH,
                "AH":Legends.AH,
                "PV":Legends.PV,
                "snowfall":Legends.snowfall,
                "total_preci":Legends.total_preci,
                "tot_wave":Legends.tot_wave,"sst":Legends.sst,
                "mis":Legends.mis,
                "light_instant":Legends.light_instant,
                "light_av1h":Legends.light_av1h,
                "light_yr":Legends.light_yellow_red,
                "opera_winds":Legends.opera_winds,
                "t_advection":Legends.t_advection,
                "stat_stab":Legends.stat_stab,
                "zero_level":Legends.zero_level,
                "preci_type":Legends.preci_type,
                "total_preci_rate":Legends.total_preci_rate,
                "di":Legends.di,
                "wind_speed":Legends.wind_speed,"u10_wind_gust":Legends.u10_wind_gust,
                "jet":Legends.jet,
                "therm_wind":Legends.therm_wind,
                }

# Coastlines's dictionary
coastlines_dict = {
                "meteo":Coastlines.meteo,
                "black":Coastlines.black,"blue":Coastlines.blue,"red":Coastlines.red,
                "cream":Coastlines.cream,"white":Coastlines.white,
                "mis":Coastlines.mis_bg,
                "cross_coast":Coastlines.cross_coast,
                "opera":Coastlines.opera,
                "cream_land":Coastlines.cream_land,
                "bold_land":Coastlines.bold_land,
                "light_radar":Coastlines.light_radar,
                }

winds_dict = {
                "wind_speed_1":Winds.wind_speed_1,#"wind_speed_2":Winds.wind_speed_2,"wind_speed_3":Winds.wind_speed_3,
                "black flags":Winds.black_flags,"blue_flags":Winds.blue_flags,
                "black arrows":Winds.black_arrows,
                "mis":Winds.mis_wind_plot_arrows,
                "wind_plot_1000":Winds.wind_plot_1000,
                "wind_plot_850":Winds.wind_plot_850,
                "wind_plot_925":Winds.wind_plot_925,
                "wind_plot_wave":Winds.wind_plot_wave,
                "therm_wind":Winds.therm_wind,
                "q_vec_arrows":Winds.q_vec_arrows,
                "wind_wave_plot":Winds.wind_wave_plot
                }
