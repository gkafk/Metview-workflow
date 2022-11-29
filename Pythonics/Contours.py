'''
Εδώ κατασκευάζονται όλα τα αντικείμενα των contours
Τα χρησιμοποιούμε στο λεξικό contours_dict και τα καλούμε στη συνάρτηση plotter
στη γραμμή contours    = contours_dict[contours_var.get()]
'''
import metview as mv

LABEL_HEIGHT = 0.3

red_blue = mv.mcont(
        legend                         = "on",
        contour                        = "on",
        contour_level_count            = 12,
        contour_label                  = "on",
        contour_shade                  = "on",
        contour_shade_method           = "area_fill",
        contour_shade_max_level_colour = "red",
        contour_shade_min_level_colour = "blue"
        )

white_green = mv.mcont(
        legend                         = "on",
        contour                        = "on",
        contour_level_count            = 12,
        contour_label                  = "on",
        contour_shade                  = "on",
        contour_shade_method           = "area_fill",
        contour_shade_max_level_colour = "white",
        contour_shade_min_level_colour = "green"
        )

ecchart = mv.mcont(
    contour_automatic_setting = 'ecchart'
        )

# contour για τη θερμοκρασία
Temp = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -50,-48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_grey_purple_54"
   )

# PT = mv.mcont(
#    LEGEND                       = "ON",
#    CONTOUR                      = "OFF",
#    CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
#    CONTOUR_LEVEL_LIST           = [ 250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324 ],
#    CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
#    CONTOUR_LABEL_BLANKING       = "OFF",
#    CONTOUR_SHADE                = "ON",
#    CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
#    CONTOUR_SHADE_METHOD         = "AREA_FILL",
#    CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_black_darkred_37"
#    )

PT = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [200,280,290,300,310,320,330,340,350,360,370,380,450],
    contour_label_height        = 0.4,
    contour_shade               = "on",
    contour_shade_colour_method = "palette",
    contour_shade_method        = "area_fill",
    contour_shade_palette_name  = "eccharts_rainbow_black_darkred_13"
   )


# contour για θερμοκρασία στα 2 μέτρα
sfc_T2m_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -50,-48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_grey_purple_54"
   )


sfc_T2m_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blue_magenta_53"
   )

# contour για μεσαία νέφη
MCC = mv.mcont(
            LEGEND                      = "ON",
               CONTOUR                     = "OFF",
               CONTOUR_LEVEL_TOLERANCE     = 1,
               CONTOUR_LABEL               = "OFF",
               CONTOUR_SHADE               = "ON",
               CONTOUR_SHADE_COLOUR_METHOD = "LIST",
               CONTOUR_SHADE_METHOD        = "AREA_FILL",
               CONTOUR_SHADE_COLOUR_LIST   = [ "RGBA(0.9906,0.9373,1,0)","RGBA(0.9729,0.8196,1,0.7059)","RGBA(0.9553,0.702,1,0.7059)","RGBA(0.9377,0.5843,1,0.7059)","RGBA(0.92,0.4667,1,0.7059)","RGBA(0.9024,0.349,1,0.7059)","RGBA(0.8847,0.2314,1,0.7059)","RGBA(0.8682,0.1216,1,0.7059)","RGBA(0.8549,0,1,0.7059)" ]
   )

# contour για υψηλά νέφη
HCC = mv.mcont(
   LEGEND                      = "ON",
   CONTOUR                     = "OFF",
   CONTOUR_LEVEL_TOLERANCE     = 1,
   CONTOUR_LABEL               = "OFF",
   CONTOUR_SHADE               = "ON",
   CONTOUR_SHADE_COLOUR_METHOD = "LIST",
   CONTOUR_SHADE_METHOD        = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST   = [ "RGBA(0.8942,0.9501,0.8303,0)","RGBA(0.8375,0.9233,0.7395,0.7059)","RGBA(0.7808,0.8965,0.6486,0.7059)","RGBA(0.7241,0.8698,0.5577,0.7059)","RGBA(0.6674,0.843,0.4668,0.7059)","RGBA(0.6108,0.8163,0.3759,0.7059)","RGBA(0.5541,0.7895,0.285,0.7059)","RGBA(0.4958,0.7392,0.2176,0.7059)","RGBA(0.4235,0.651,0.1922,0.7059)" ]
   )

# contour για χαμηλά νέφη
LCC=mv.mcont(
   LEGEND                      = "ON",
   CONTOUR                     = "OFF",
   CONTOUR_LEVEL_TOLERANCE     = 1,
   CONTOUR_LABEL               = "OFF",
   CONTOUR_SHADE               = "ON",
   CONTOUR_SHADE_COLOUR_METHOD = "LIST",
   CONTOUR_SHADE_METHOD        = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST   = [ "RGBA(1,0.9038,0.8196,0)","RGBA(1,0.841,0.702,0.7059)","RGBA(1,0.7783,0.5843,0.7059)","RGBA(1,0.7156,0.4667,0.7059)","RGBA(1,0.6528,0.349,0.7059)","RGBA(1,0.5901,0.2314,0.7059)","RGBA(1,0.5273,0.1137,0.7059)","RGBA(0.9961,0.4648,0,0.7059)","RGBA(0.8784,0.4099,0,0.7059)" ]
   )

# contour για σχετική υγρασία
RH_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 10,20,30,40,50,60,70,80,90,100,110 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.9333,0.9333,0.9333)","RGB(0.7176,0.7176,0.7176)","RGB(0.3825,0.2906,0.98)","RGB(0.1169,0.005676,0.959)","RGB(0.0107,0.3957,0.8991)","RGB(0.06621,0.6375,0.9926)","RGB(0.01176,1,0.4894)","RGB(0.06862,1,0.01961)","RGB(0.6514,1,0.003922)","RGB(0.9205,0.9687,0.003815)" ]
   )

RH_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 25,50,75,100,110 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_FREQUENCY      = 1,
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.6827,0.9487,0.696)","RGB(0.412,0.9684,0.8015)","RGB(0.3444,0.7112,0.9732)","RGB(0.4707,0.4872,0.9646)" ]
   )

# contour για απόλυτη υγρασία
AH_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 ],
   CONTOUR_LABEL_HEIGHT         = 0.4,
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blue_purple_24"
   )

AH_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR_LINE_STYLE                      = "DASH",
   CONTOUR_LINE_THICKNESS                  = 3,
   CONTOUR_LINE_COLOUR_RAINBOW             = "ON",
   CONTOUR_LINE_COLOUR_RAINBOW_METHOD      = "LIST",
   CONTOUR_LINE_COLOUR_RAINBOW_COLOUR_LIST = [ "GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","GREEN","YELLOW","YELLOW","YELLOW","YELLOW","RED","RED","RED","RED","RED","RED" ],
   CONTOUR_HIGHLIGHT                       = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE            = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST                      = [ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24 ],
   CONTOUR_LABEL_HEIGHT                    = 0.5
   )

# contour για γεοδυναμικά ύψη
geo = mv.mcont(
       CONTOUR_LINE_THICKNESS       = 3,
       CONTOUR_LINE_COLOUR          = "BLACK",
       CONTOUR_HIGHLIGHT            = "OFF",
       # CONTOUR_REFERENCE_LEVEL      = 156,
       CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
       CONTOUR_INTERVAL             = 6.0,
       CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
       CONTOUR_LABEL_BLANKING       = "OFF",
       CONTOUR_HILO                 = "OFF",
       CONTOUR_HILO_WINDOW_SIZE     = 5
       )

geo_60 = mv.mcont(
       CONTOUR_LINE_THICKNESS       = 4,
       CONTOUR_LINE_COLOUR          = "BLACK",
       CONTOUR_HIGHLIGHT            = "OFF",
       # CONTOUR_REFERENCE_LEVEL      = 156,
       CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
       CONTOUR_INTERVAL             = 60.0,
       CONTOUR_LABEL_HEIGHT         = 0.4,
       # CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
       CONTOUR_LABEL_BLANKING       = "OFF",
       CONTOUR_HILO                 = "OFF",
       CONTOUR_HILO_HEIGHT          = 1.0,
       CONTOUR_HILO_QUALITY         = "HIGH",
       CONTOUR_LO_COLOUR            = "RED"
       )

geo_60_blue = mv.mcont(
       CONTOUR_LINE_THICKNESS       = 4,
       CONTOUR_LINE_COLOUR          = "BLUE",
       CONTOUR_HIGHLIGHT            = "OFF",
       # CONTOUR_REFERENCE_LEVEL      = 156,
       CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
       CONTOUR_INTERVAL             = 60.0,
       CONTOUR_LABEL_HEIGHT         = 0.4,
       # CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
       CONTOUR_LABEL_BLANKING       = "OFF",
       CONTOUR_HILO                 = "OFF",
       CONTOUR_HILO_HEIGHT          = 1.0,
       CONTOUR_HILO_QUALITY         = "HIGH",
       CONTOUR_LO_COLOUR            = "RED"
       )

geo_120 = mv.mcont(
       CONTOUR_LINE_THICKNESS       = 3,
       CONTOUR_LINE_COLOUR          = "BLUE",
       CONTOUR_HIGHLIGHT            = "OFF",
       # CONTOUR_REFERENCE_LEVEL      = 156,
       CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
       CONTOUR_INTERVAL             = 120.0,
       CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
       CONTOUR_LABEL_COLOUR         = "BLUE",
       CONTOUR_LABEL_BLANKING       = "ON",
       CONTOUR_HILO                 = "OFF",
       CONTOUR_HILO_WINDOW_SIZE     = 5
       )

geo_120_wind = mv.mcont(
       CONTOUR_LINE_THICKNESS       = 3,
       CONTOUR_LINE_COLOUR          = "GREY",
       CONTOUR_HIGHLIGHT            = "OFF",
       # CONTOUR_REFERENCE_LEVEL      = 156,
       CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
       CONTOUR_INTERVAL             = 120.0,
       CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
       CONTOUR_LABEL_COLOUR         = "BLACK",
       CONTOUR_LABEL_BLANKING       = "ON",
       CONTOUR_HILO                 = "OFF",
       CONTOUR_HILO_WINDOW_SIZE     = 5
       )

geo_line = mv.mcont(
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_REFERENCE_LEVEL      = 156,
   CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
   CONTOUR_INTERVAL             = 6.0,
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_HILO                 = "OFF"
   )

geo_T_line_1 = mv.mcont(
   CONTOUR_LINE_STYLE           ="DASH",
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_LINE_COLOUR          = "RED",
   CONTOUR_HIGHLIGHT_STYLE      = "DASH",
   CONTOUR_HIGHLIGHT_COLOUR     = "RED",
   CONTOUR_HIGHLIGHT_THICKNESS  = 5,
   CONTOUR_HIGHLIGHT_FREQUENCY  = 25,
   CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
   CONTOUR_INTERVAL             = 5.0,
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "RED"
   )

run_difference = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -200,-150,-100,-75,-50,-30,-20,-15,-12,-9,-6,-3,3,6,9,12,15,20,30,50,75,100,150,200 ],
   CONTOUR_LABEL_HEIGHT         = 0.4,
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_grey_red_25"
   )

# contour για μέση πίεση επιφανείας
SFC_MSLP_line_1 = mv.mcont(
   LEGEND                       = "OFF",
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_REFERENCE_LEVEL      = 1000,
   CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
   CONTOUR_INTERVAL             = 4.0,
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF"
   )

SFC_MSLP_line_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_REFERENCE_LEVEL      = 1000,
   CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
   CONTOUR_INTERVAL             = 2.0,
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF"
   )

MSLP_white = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_LINE_COLOUR          = "white",
   # CONTOUR_HIGHLIGHT_STYLE      = "DASH",
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_REFERENCE_LEVEL      = 1000,
   CONTOUR_LEVEL_SELECTION_TYPE = "INTERVAL",
   CONTOUR_INTERVAL             = 2.0,
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF"
   )

# contour για σημείο δρόσου
Td_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -50,-48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_grey_purple_54"
   )

Td_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blue_magenta_53"
   )

# contour για relative vorticity
RV = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -200,-100,-75,-50,-30,-20,-15,-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9,11,13,15,20,30,50,75,100,200 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_blue_red_27"
   )

PV_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -100,-10,-5,-3,-1,0,0.5,1,1.5,2,3,4,5,6,7,8,9,10,12,15,20,100 ],
   CONTOUR_LABEL_HEIGHT         = 0.4,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_black_tan_22"
   )

PV_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -1,-0.5,0,0.5,1,1.5,2,3,4,5,7,9,12,15,18 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blu_gr_red_purple_14"
   )

PV_3 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -4,-3.75,-3.5,-3.25,-3,-2.75,-2.5,-2.25,-2,-1.75,-1.5,-1.25,-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1,1.5,2,2.5,3,3.5,4,4.5,5,6,7,8,9,10,12,14,16,18,20 ],
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_grey_red_37"
   )



# contour για Vertical Velocity
VV = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -50,-10,-5,-2,-1,-0.5,-0.3,-0.2,-0.1,-0.05,0.05,0.1,0.2,0.3,0.5,1,2,5,10,50 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_violet_brown_19"
   )

# contour για RH_VV
VV_pos_line = mv.mcont(
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_LINE_COLOUR          = "YELLOWISH_ORANGE",
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF"
   )

VV_neg_line = mv.mcont(
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_LINE_COLOUR          = "VIOLET",
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -2,-1.8,-1.6,-1.4,-1.2,-1,-0.8,-0.6,-0.4,-0.2 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF"
   )


# contour για ορατότητα
visibility = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0,500,1000,1500,2000,2500,3000,4000,5000,6000,7000,8000,9000,10000 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_magenta_grey_13"
   )

# contour για ύψος κύματος
wave_height = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.25,0.5,1,1.5,2,2.5,3,3.5,4,5,8,12 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blue_charcoal_11"
   )

# contour για θερμοκρασία θάλλασας SST
SST = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_purple_red_19"
   )

# contour για χιονόπτωση
snowfall_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.5,2,4,10,25,50,100,150,250 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_blue_red_8"
   )

snowfall_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.1,0.5,1,5,10,15,20,25,30,40,50,75,100,150,200,300 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blue_purple_15"
   )

snowfall_3 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.5,1,2,3,4,5,6,8,10,15,20,25,30,40,50,75,100,200,300 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_purple_burgundy_18"
   )

snow_dots = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.5,2,4,10 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   # CONTOUR_SHADE_TECHNIQUE      = "marker",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_COLOUR_LIST    = [ "White","White","White" ],
   contour_shade_method         = "dot",
   contour_shade_min_level_density = 10,
   contour_shade_max_level_density = 200,
   CONTOUR_SHADE_DOT_SIZE       = 0.09
   )

# contour για  βάση νεφών
cloud_base = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0,500,1000,1500,2000,2500,3000,4000,6000,8000,10000,14000,18000,22000 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_magenta_grey_13"
   )

# contour για CAPE
CAPE = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 50,100,200,400,800,1200,1600,2000,2500,3000,4000,9000 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_blue_purple_11"
   )

# contour για υετό
total_preci_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.5,2,4,10,25,50,100,150,250 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_blue_red_8"
   )

# contour για ανέμους
wspd_1 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 11,17,22,28,34,41,48,56,64,71,200 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "YELLOW","YELLOWISH_ORANGE","ORANGISH_RED","GREEN","KELLY_GREEN","BLUISH_PURPLE","GREY","BURGUNDY","BLUE" ]
   )

wspd_2 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   # CONTOUR_LEVEL_LIST           = [ 0,20,40,60,80,100,120,140,160,180,200 ],
   CONTOUR_LEVEL_LIST           = [ 60,70,80,100,120,150,180,300 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_green_purple_7"
   # CONTOUR_SHADE_PALETTE_NAME   = "eccharts_yellow_blue_dark_9"
   )



wspd_3 = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 60,70,80,90,100,110,120,130,200 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_green_purple_7"
   )

#mis contours
mis_HCC = mv.mcont(
   CONTOUR                     ="OFF",
   CONTOUR_LEVEL_TOLERANCE     = 1,
   CONTOUR_LABEL               = "OFF",
   CONTOUR_SHADE               = "ON",
   CONTOUR_SHADE_COLOUR_METHOD = "PALETTE",
   CONTOUR_SHADE_METHOD        = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME  = "eccharts_white_transparent_12"
   )


mis_MCC = mv.mcont(
   CONTOUR                     = "OFF",
   CONTOUR_LEVEL_TOLERANCE     = 1,
   CONTOUR_LABEL               = "OFF",
   CONTOUR_SHADE               = "ON",
   CONTOUR_SHADE_COLOUR_METHOD = "PALETTE",
   CONTOUR_SHADE_METHOD        = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME  = "eccharts_lightgrey_transparent_12"
   )

mis_LCC = mv.mcont(
   CONTOUR                     = "OFF",
   CONTOUR_LEVEL_TOLERANCE     = 1,
   CONTOUR_LABEL               = "OFF",
   CONTOUR_SHADE               = "ON",
   CONTOUR_SHADE_COLOUR_METHOD = "PALETTE",
   CONTOUR_SHADE_METHOD        = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME  = "eccharts_grey_transparent_12"
   )

mis_total_preci = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.5,10,50,150 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.6221,0.7384,0.9543)","RGB(0.3621,0.6353,0.9085)","RGB(0.5065,0.4355,0.9684)" ]
   )

mis_snowfall = mv.mcont(
   LEGEND                        = "ON",
   CONTOUR                       = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE  = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST            = [ 0.5,10,50,150 ],
   CONTOUR_LABEL                 = "OFF",
   CONTOUR_SHADE                 = "ON",
   CONTOUR_SHADE_COLOUR_METHOD   = "LIST",
   CONTOUR_SHADE_METHOD          = "HATCH",
   CONTOUR_SHADE_COLOUR_LIST     = [ "RGB(0.958,0.5322,0.9012)","RGB(0.9719,0.3771,0.6745)","MAGENTA" ],
   CONTOUR_SHADE_HATCH_THICKNESS = 2
   )

mis_wave_height = mv.mcont(
   CONTOUR                          = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE     = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST               = [ 0.25,0.5,1,1.5,2,2.5,3,3.5,4,5,8,12 ],
   CONTOUR_LABEL_BLANKING           = "OFF",
   CONTOUR_LABEL_FREQUENCY          = 1,
   CONTOUR_GRID_VALUE_PLOT          = "ON",
   CONTOUR_GRID_VALUE_LAT_FREQUENCY = 10,
   CONTOUR_GRID_VALUE_LON_FREQUENCY = 10,
   CONTOUR_GRID_VALUE_HEIGHT        = 0.3,
   CONTOUR_GRID_VALUE_MARKER_HEIGHT = 0.3
   )

mis_T2m = mv.mcont(
   LEGEND                           = "OFF",
   CONTOUR                          = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE     = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST               = [ -50,-48,-46,-44,-42,-40,-38,-36,-34,-32,-30,-28,-26,-24,-22,-20,-18,-16,-14,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58 ],
   CONTOUR_LABEL_HEIGHT             = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING           = "OFF",
   contour_grid_value_colour        = "ORANGE",
   # contour_grid_value_justification = "RIGHT",
   CONTOUR_LABEL_FREQUENCY          = 1,
   CONTOUR_GRID_VALUE_PLOT          = "ON",
   CONTOUR_GRID_VALUE_LAT_FREQUENCY = 5,
   CONTOUR_GRID_VALUE_LON_FREQUENCY = 5,
   CONTOUR_GRID_VALUE_HEIGHT        = 0.3,
   CONTOUR_GRID_VALUE_MARKER_HEIGHT = 0.3
   )

# Opera contoures
opera_preci = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 2,5,10,20,50,150 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "RGBA(0.6221,0.7384,0.9543,0.5882)","RGBA(0.3621,0.6353,0.9085,0.5882)","RGBA(0.5065,0.4355,0.9684,0.5882)","RGBA(0.3048,0.2003,0.984,0.5882)","RGBA(0.03862,0.03862,0.6908,0.5882)" ]
   )

opera_LCC = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR_LINE_THICKNESS       = 3,
   CONTOUR_LINE_COLOUR          = "ORANGE",
   CONTOUR_HIGHLIGHT            = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.625,1.5 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = "RGBA(1,0.498,0,0.3922)"
   )

opera_cloud_base = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0,3000 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = "RGBA(0.2,0.2,0.2,0.3922)"
   )

opera_visibility = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0,5000 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "HATCH",
   CONTOUR_SHADE_COLOUR_LIST    = "RGB(0.498,0,1)"
   )

# define opera wind value plottig
opera_w_1000 = mv.mcont(
   contour                          = "off",
   contour_level_selection_type     = "interval",
   contour_interval                 = 1.0,
   contour_label_blanking           = "off",
   contour_label_frequency          = 1,
   contour_grid_value_plot          = "on",
   contour_grid_value_lat_frequency = 3,
   contour_grid_value_lon_frequency = 3,
   contour_grid_value_height        = 0.3,
   contour_grid_value_colour        = "black",
   contour_grid_value_plot_type     = "values",
   contour_grid_value_justification = "right",
   contour_grid_value_vertical_align= "base"
   )

opera_w_925 = mv.mcont(
   contour                          = "off",
   contour_level_selection_type     = "interval",
   contour_interval                 = 1.0,
   contour_label_blanking           = "off",
   contour_label_frequency          = 1,
   contour_grid_value_plot          = "on",
   contour_grid_value_lat_frequency = 3,
   contour_grid_value_lon_frequency = 3,
   contour_grid_value_height        = 0.3,
   contour_grid_value_colour        = "red",
   contour_grid_value_plot_type     = "values",
   contour_grid_value_justification = "centre",
   contour_grid_value_vertical_align= "top"
   )

opera_w_850 = mv.mcont(
   contour                          = "off",
   contour_level_selection_type     = "interval",
   contour_interval                 = 1.0,
   contour_label_blanking           = "off",
   contour_label_frequency          = 1,
   contour_grid_value_plot          = "on",
   contour_grid_value_lat_frequency = 3,
   contour_grid_value_lon_frequency = 3,
   contour_grid_value_height        = 0.3,
   contour_grid_value_colour        = "blue",
   contour_grid_value_plot_type     = "values",
   contour_grid_value_justification = "left",
   contour_grid_value_vertical_align= "base"
   )


opera_wave_wind = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 11,17,22,28,34,41,48,56,64,71 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "YELLOW","YELLOWISH_ORANGE","ORANGISH_RED","GREEN","KELLY_GREEN","BLUISH_PURPLE","GREY","BURGUNDY","BLUE" ]
   )


opera_wave_swh = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 1,2,3,4,6,9 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "HATCH",
   CONTOUR_SHADE_COLOUR_LIST    = [ "RGB(0.03215,0.03215,0.9326)","RGB(0.01808,0.01808,0.7505)","RGB(0.02953,0.02953,0.5979)","RGB(0.03922,0.03922,0.4706)","RGB(0.04973,0.04973,0.3346)" ]
   )


# T advection contoures

# define contour shading for advection
adv = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [-15,-10,-7,-5,-4,-3,-2.5,-2,-1.5,-1,-0.5,0.5,1,1.5,2,2.5,3,4,5,7,10,15],
    contour_label_height        = LABEL_HEIGHT,
    CONTOUR_LABEL_BLANKING       = "OFF",
    contour_shade               = "on",
    contour_shade_colour_method = "palette",
    contour_shade_method        = "area_fill",
    contour_shade_palette_name  = "eccharts_black_red_21"
    )

# define contouring for geopotential
adv_geo = mv.mcont(
    contour_line_colour          = "blue",
    contour_line_thickness       = 3,
    contour_level_selection_type = "interval",
    contour_interval             = 60,
    contour_label_height         = LABEL_HEIGHT,
    CONTOUR_LABEL_BLANKING       = "OFF"
    )

# define contouring for static stability
stat_stab = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -0.20,-0.18,-0.16,-0.14,-0.12,-0.10,-0.08,-0.06,-0.04,-0.02,0,0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "m_green_purple_20"
   )

therm_wind = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,80 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "m_yellow_red_16"
   )

# δείκτης δυσφορίας
di = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 27,27.5,28,28.6,30,35,40 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_yellow_purple_6"
   )

RH_CRS_blue = mv.mcont(
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

# Lightnings
light_av1h = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.1,0.5,1,2,5,10,20,50,100,500 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_red_yellow_9"
   )

light_yellow_red = mv.mcont(
    legend                        = "on",
    contour                       = "off",
    contour_level_selection_type  = "level_list",
    contour_level_list            = [0.5,3,500],
    contour_label                 = "off",
    contour_label_height          = 0.4,
    contour_shade                 = "on",
    contour_shade_colour_method   = "list",
    contour_shade_method          = "area_fill",
    contour_shade_colour_list     = ["yellow","red"]
   )
   
light_instant = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.1,0.5,1,2,5,10,20,50,100,500 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_red_yellow_9"
   )

lights_cros = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 0.1,1,10,50 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "OFF",
   # CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   # CONTOUR_SHADE_COLOUR_LIST    = [ "YELLOW","YELLOWISH_ORANGE","REDDISH_ORANGE" ],
   CONTOUR_SHADE_DOT_SIZE       = 0.2,
   contour_grid_value_plot      = "on",
   contour_grid_value_plot_type = "marker",
   contour_grid_value_marker_colour    = "YELLOW",
   contour_grid_value_min       = 0.20,
   contour_grid_value_marker_height = 0.6
   )

light_mis1 = mv.mcont(
   LEGEND                        = "ON",
   CONTOUR                       = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE  = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST            = [ 0.1,1,10,50 ],
   CONTOUR_LABEL                 = "OFF",
   CONTOUR_SHADE                 = "ON",
   CONTOUR_SHADE_COLOUR_METHOD   = "LIST",
   CONTOUR_SHADE_METHOD          = "HATCH",
   CONTOUR_SHADE_COLOUR_LIST     = [ "YELLOW","YELLOWISH_ORANGE","REDDISH_ORANGE" ],
   CONTOUR_SHADE_HATCH_THICKNESS = 2
   )

light_mis = mv.mcont(
   LEGEND                        = "ON",
   CONTOUR                       = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE  = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST            = [ 0.1,1,10,50 ],
   CONTOUR_LABEL                 = "OFF",
   CONTOUR_SHADE                 = "ON",
   CONTOUR_SHADE_COLOUR_METHOD   = "LIST",
   CONTOUR_SHADE_METHOD          = "HATCH",
   CONTOUR_SHADE_COLOUR_LIST     = [ "YELLOWISH_ORANGE","REDDISH_ORANGE","ORANGISH_RED" ],
   CONTOUR_SHADE_HATCH_THICKNESS = 2
   )

# zero level contour
zero_level = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ -500,0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,6000,7000,8000,10000 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_purple_pink_15"
   )
# preci type
preci_type = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 1,3,5,6,7,8,15 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "LIST",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_COLOUR_LIST    = [ "GREEN","RED","BLUE","NAVY","SKY","ORANGE" ]
   )

# total_preci_rate
total_preci_rate = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   # CONTOUR_LEVEL_LIST           = [ 0.08,0.15,0.3,0.65,1.3,2.7,5.6,11.5,23.7,48.6,100,205,421,864,1775,3600 ],
   CONTOUR_LEVEL_LIST           = [ 0.1,0.3,0.5,1,2,3,5,10,15,20,30,50,70,100,150,200 ],
   CONTOUR_LABEL                = "OFF",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_cyan_white_15"
   )

# Q-vectors
PT_Q = mv.mcont(
   LEGEND                       = "ON",
   CONTOUR                      = "OFF",
   CONTOUR_LEVEL_SELECTION_TYPE = "LEVEL_LIST",
   CONTOUR_LEVEL_LIST           = [ 250,252,254,256,258,260,262,264,266,268,270,272,274,276,278,280,282,284,286,288,290,292,294,296,298,300,302,304,306,308,310,312,314,316,318,320,322,324 ],
   CONTOUR_LABEL_HEIGHT         = LABEL_HEIGHT,
   CONTOUR_LABEL_BLANKING       = "OFF",
   CONTOUR_LABEL_COLOUR         = "BLACK",
   CONTOUR_SHADE                = "ON",
   CONTOUR_SHADE_COLOUR_METHOD  = "PALETTE",
   CONTOUR_SHADE_METHOD         = "AREA_FILL",
   CONTOUR_SHADE_PALETTE_NAME   = "eccharts_rainbow_black_darkred_37"
   )

GEO_Q = mv.mcont(
    legend                       = "off",
    contour_line_colour          = "blue",
    contour_line_thickness       = 3,
    #contour_highlight_colour     = "black",
    contour_level_selection_type = "interval",
    contour_interval             = 60,
    contour_label_height         = LABEL_HEIGHT,
    CONTOUR_LABEL_BLANKING       = "OFF"
    )



# define contour shading for wind_chill_0 ************************************
wind_chill_0 = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [-50,0],
    contour_label_height        = 0.4,
    contour_label_colour        = "red",
    contour_label_frequency     = 1,
    CONTOUR_LABEL_BLANKING      = "OFF",
    contour_shade               = "on",
    contour_shade_colour_method = "list",
    contour_shade_method        = "area_fill",
    contour_shade_colour_list   = "RGB(0.4581,0.7784,0.1157)"
    )

# define contour shading for wind_chill_m15
wind_chill_m15 = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [-50,-15],
    contour_label_height        = 0.4,
    contour_label_colour        = "purple",
    contour_label_frequency     = 1,
    CONTOUR_LABEL_BLANKING      = "OFF",
    contour_shade               = "on",
    contour_shade_colour_method = "list",
    contour_shade_method        = "area_fill",
    contour_shade_colour_list   = "kelly_green"
    )

# define contour shading for wind_chill wind speed to knots
wind_chill_wspd = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [27,35,80],
    contour_label_height        = 0.4,
    contour_label_colour        = "blue",
    contour_label_frequency     = 1,
    CONTOUR_LABEL_BLANKING      = "OFF",
    contour_shade               = "on",
    contour_shade_colour_method = "list",
    contour_shade_method        = "area_fill",
    contour_shade_colour_list   = ["ORANGISH_YELLOW","REDDISH_ORANGE"]
    )

# define contour shading for wind_chill wave height
wind_chill_wave = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [4,20],
    contour_label_height        = 0.4,
    contour_label_colour        = "black",
    contour_label_frequency     = 1,
    CONTOUR_LABEL_BLANKING      = "OFF",
    contour_shade               = "on",
    contour_shade_colour_method = "list",
    contour_shade_method        = "hatch",
    contour_shade_colour_list   = "Purplish_blue"
    )

# define contour shading for wind_chill Tsea
wind_chill_Tsea = mv.mcont(
    legend                      = "on",
    contour                     = "off",
    contour_level_selection_type= "level_list",
    contour_level_list          = [14,50],
    CONTOUR_LABEL                = "OFF",
    # contour_label_height        = 0.4,
    # contour_label_colour        = "black",
    # contour_label_frequency     = 1,
    CONTOUR_LABEL_BLANKING      = "OFF",
    contour_shade               = "on",
    contour_shade_colour_method = "list",
    contour_shade_method        = "area_fill",
    contour_shade_colour_list   = "RGB(0.6221,0.9543,0.9543)"
    )

# define contour line for pressure
pressure = mv.mcont(
    contour_line_thickness       = 2,
    contour_line_colour          = "red",
    contour_highlight            = "off",
    contour_level_selection_type = "interval",
    contour_interval             = 50,
    contour_label_height         = 0.4
    )