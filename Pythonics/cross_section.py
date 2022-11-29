'''
Είσοδοι:
1. φάκελος του προϊόντος, για να πάρει όλα τα ύψη
2. step για την επιλογή του τριώρου
3. συντεταγμένες της γραμμής
'''

import metview as mv
import os
import globalVariables as gbl


# gribs_read = []
# output_folder="/home/metview/metview/System/data/grib_files/output/"
output_folder=gbl._OUTPUT_FOLDER
folder_x = "20211010/0000/Relative humidity/"
# folder_x = "2021_04_05/0000/Temperature/"
step_var = 6

# συνάρτηση για να σβήνει κρυφά αρχεία κτλ από λίστα
def remove_hidden_files(lista):
    for item in lista[:]:
        if item.startswith(".") or "ERROR" in item or item is None:
            lista.remove(item)

grib_list=os.listdir(output_folder+folder_x)
remove_hidden_files(grib_list)
grib_list=sorted(grib_list,key = int)
print(grib_list)
s_all = mv.Fieldset()
for x in grib_list:
    grib=str(os.listdir(output_folder+folder_x + x)[0])
    print(grib)
    a = mv.read( output_folder+folder_x + x + "/"+grib)
    a_level=mv.read(data=a,step=step_var)
    print(a)
    # gribs_read.append(a_level)
    try:
        s_all.append(a_level)
    except Exception as e:
        print("Exception:",e)

# print(gribs_read)

# pairnei to merge ana 2
# i=0
# while i < len(gribs_read)-1:
#     if i == 0:
#         all = gribs_read[i]
#     else:
#         all = mv.merge(gribs_read[i],all)
#     i+=1

# f_all = mv.Fieldset(fields=gribs_read)
# tap = tuple(gribs_read)
# print(tap)
all = mv.merge(s_all)
# all = mv.merge(f_all)






# read the GRIB data from file
# t_fc = mv.read("t_fc24.grib")
# print("t_fc:\n",t_fc)

# set up the view to plot the data into
cross_section_view = mv.mxsectview(
    bottom_level = 1000.0,
    top_level    = 1,
    # line         = [-40.1, -105.6, 61.5, 85.1] #lat,lon,lat,lon
    line         = [38.87,21.06,39.95,23.46] #lat,lon,lat,lon
)


# set up the contouring style
shading = mv.mcont(
    legend                         = "on",
    contour                        = "off",
    contour_level_count            = 12,
    contour_label                  = "off",
    contour_shade                  = "on",
    contour_shade_method           = "area_fill",
    contour_shade_max_level_colour = "RGB(0.72,0.059,0.059)",
    contour_shade_min_level_colour = "RGB(0.99,0.98,0.98)"
)

# set up the title, just to make the font bigger
title = mv.mtext(text_font_size = 0.5)

# define the output plot file
# mv.setoutput(mv.pdf_output(output_name = 'cross_section_pl_data'))

# plot the data into the Cross Section view with visdefs for styling
# mv.plot(cross_section_view, t_fc, shading, title)
mv.plot(cross_section_view, all,  shading, title)
