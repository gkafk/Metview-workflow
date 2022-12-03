'''
Constructing coastline objects.
Using them in dictionary coastlines_dict call on plotter function
'''

import metview as mv

black = mv.mcoast(
           MAP_COASTLINE_RESOLUTION        = "FULL",
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "BLACK",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  ="RGB(90,90,90)",
           MAP_BOUNDARIES                  = "ON",
           MAP_RIVERS                      = "ON",
           MAP_RIVERS_COLOUR               = "OLIVE",
           MAP_CITIES                      = "ON",
           MAP_CITIES_FONT_NAME            = "ARIAL",
           MAP_CITIES_FONT_SIZE            = 0.2,
           MAP_CITIES_UNIT_SYSTEM          = "CM",
           MAP_CITIES_TEXT_BLANKING        = "OFF",
           MAP_CITIES_MARKER               = "CIRCLE",
           MAP_CITIES_MARKER_HEIGHT        = 0.1,
           MAP_CITIES_MARKER_COLOUR        = "DARK GREY",
           MAP_DISPUTED_BOUNDARIES_STYLE   = "SOLID",
           MAP_DISPUTED_BOUNDARIES_COLOUR  = "AVOCADO",
           MAP_GRID                        = "ON",
           MAP_LABEL                       = "OFF"
          )

red= mv.mcoast(
           MAP_COASTLINE_RESOLUTION        = "FULL",
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "MUSTARD",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "ECMWF_BLUE",
           MAP_BOUNDARIES                  = "ON",
           MAP_RIVERS                      = "ON",
           MAP_RIVERS_COLOUR               = "OLIVE",
           MAP_CITIES                      = "ON",
           MAP_CITIES_FONT_NAME            = "ARIAL",
           MAP_CITIES_FONT_SIZE            = 0.4,
           MAP_CITIES_UNIT_SYSTEM          = "CM",
           MAP_CITIES_TEXT_BLANKING        = "OFF",
           MAP_CITIES_MARKER               = "CIRCLE",
           MAP_CITIES_MARKER_HEIGHT        = 0.1,
           MAP_CITIES_MARKER_COLOUR        = "RED",
           MAP_DISPUTED_BOUNDARIES_STYLE   = "SOLID",
           MAP_DISPUTED_BOUNDARIES_COLOUR  = "RED",
           MAP_GRID                        = "OFF",
           MAP_LABEL                       = "OFF"
          )

blue = mv.mcoast(
           MAP_COASTLINE_RESOLUTION        = "FULL",
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "MUSTARD",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "ECMWF_BLUE",
           MAP_BOUNDARIES                  = "ON",
           MAP_RIVERS                      = "ON",
           MAP_RIVERS_COLOUR               = "OLIVE",
           MAP_CITIES                      = "ON",
           MAP_CITIES_FONT_NAME            = "ARIAL",
           MAP_CITIES_FONT_SIZE            = 0.2,
           MAP_CITIES_UNIT_SYSTEM          = "CM",
           MAP_CITIES_TEXT_BLANKING        = "OFF",
           MAP_CITIES_MARKER               = "CIRCLE",
           MAP_CITIES_MARKER_HEIGHT        = 0.1,
           MAP_CITIES_MARKER_COLOUR        = "BLUE",
           MAP_DISPUTED_BOUNDARIES_STYLE   = "SOLID",
           MAP_DISPUTED_BOUNDARIES_COLOUR  = "BLUE",
           MAP_GRID                        = "OFF",
           MAP_LABEL                       = "OFF"
          )

meteo = mv.mcoast(
           # MAP_COASTLINE_RESOLUTION        = "MEDIUM",
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "RGB(97,80,62)",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "RGB(47,80,112)",
           MAP_BOUNDARIES                  = "ON",
           MAP_RIVERS                      = "ON",
           MAP_RIVERS_COLOUR               = "OLIVE",
           MAP_CITIES                      = "ON",
           MAP_CITIES_FONT_NAME            = "ARIAL",
           MAP_CITIES_FONT_SIZE            = 0.2,
           MAP_CITIES_UNIT_SYSTEM          = "CM",
           MAP_CITIES_TEXT_BLANKING        = "OFF",
           MAP_CITIES_MARKER               = "CIRCLE",
           MAP_CITIES_MARKER_HEIGHT        = 0.1,
           MAP_CITIES_MARKER_COLOUR        = "BLUE",
           MAP_DISPUTED_BOUNDARIES_STYLE   = "SOLID",
           MAP_DISPUTED_BOUNDARIES_COLOUR  = "BLUE",
           MAP_GRID                        = "OFF",
           MAP_LABEL                       = "OFF"
          )

cream = mv.mcoast(
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "CREAM",
           map_coastline_resolution        = "high",
           map_coastline_colour            = "BLACK",
           MAP_COASTLINE_THICKNESS         = 1.7,
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "WHITE",
           MAP_BOUNDARIES                  = "ON",
           MAP_LABEL_HEIGHT                = 0.2
           )

cream_land = mv.mcoast(
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "CREAM",
           MAP_COASTLINE_SEA_SHADE         = "OFF",
           MAP_COASTLINE_THICKNESS         = 1.5,
           MAP_BOUNDARIES                  = "ON",
           MAP_LABEL_HEIGHT                = 0.4
           )

bold_land = mv.mcoast(
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "CREAM",
           MAP_COASTLINE_SEA_SHADE         = "OFF",
           MAP_COASTLINE_THICKNESS         = 2.0,
           MAP_BOUNDARIES                  = "ON",
           # map_boundaries_colour           = "mustard",
           map_boundaries_thickness        = 2.0,
           MAP_LABEL_HEIGHT                = 0.4
           )

white = mv.mcoast(
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "WHITE",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "WHITE",
           MAP_BOUNDARIES                  = "ON",
           MAP_LABEL_HEIGHT                = 0.4
           )

mis_bg = mv.mcoast(
           MAP_COASTLINE_THICKNESS         = 1.5,
           MAP_COASTLINE_LAND_SHADE        = "ON",
           # MAP_COASTLINE_LAND_SHADE_COLOUR = "CREAM",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "#bffab6",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "RGB(0.8843,0.9353,0.9353)",
           MAP_BOUNDARIES                  = "OFF",
           MAP_LABEL_HEIGHT                = 0.4,
           MAP_CITIES                      = "OFF",
           MAP_RIVERS                      = "OFF",
           MAP_GRID                        = "OFF",
           MAP_LABEL                       = "OFF"
           )

mis_fg = mv.mcoast(
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "RGB(0.8843,0.9353,0.9353)",
           MAP_BOUNDARIES                  = "OFF",
           MAP_LABEL_HEIGHT                = 0.4,
           MAP_CITIES                      = "OFF",
           MAP_RIVERS                      = "OFF",
           MAP_GRID                        = "OFF",
           MAP_LABEL                       = "OFF"
           )

cross_coast = mv.mcoast(
            map_coastline_colour            = "RGB(0.4449,0.4414,0.4414)",
            map_coastline_resolution        = "medium",
            map_coastline_land_shade        = "on",
            map_coastline_land_shade_colour = "RGB(0.5333,0.5333,0.5333)",
            map_coastline_sea_shade         = "on",
            map_coastline_sea_shade_colour  = "RGB(0.7765,0.8177,0.8941)",
            map_boundaries                  = "on",
            map_boundaries_colour           = "mustard",
            map_boundaries_thickness        = 2,
            map_grid_colour                 = "RGB(0.2627,0.2627,0.2627)",
            map_grid_latitude_increment     = 5,
            map_grid_longitude_increment    = 5
    )


light_radar = mv.mcoast(
            map_coastline_colour            = "RGB(0.4449,0.4414,0.4414)",
            map_coastline_resolution        = "FULL",
            map_coastline_land_shade        = "on",
            map_coastline_land_shade_colour = "RGB(0.5333,0.5333,0.5333)",
            map_coastline_sea_shade         = "on",
            map_coastline_sea_shade_colour  = "RGB(0.7765,0.8177,0.8941)",
            map_boundaries                  = "on",
            map_boundaries_colour           = "mustard",
            map_boundaries_thickness        = 2,
            map_grid_colour                 = "RGB(0.2627,0.2627,0.2627)",
            map_grid_latitude_increment     = 5,
            map_grid_longitude_increment    = 5
    )

opera = mv.mcoast(
           MAP_COASTLINE_THICKNESS         = 1.5,
           MAP_COASTLINE_LAND_SHADE        = "ON",
           MAP_COASTLINE_LAND_SHADE_COLOUR = "RGB(0.9255,0.9255,0.9255)",
           MAP_COASTLINE_SEA_SHADE         = "ON",
           MAP_COASTLINE_SEA_SHADE_COLOUR  = "RGB(0.8843,0.9353,0.9353)",
           MAP_BOUNDARIES                  = "OFF",
           MAP_LABEL_HEIGHT                = 0.4,
           MAP_CITIES                      = "OFF",
           MAP_RIVERS                      = "OFF",
           MAP_GRID                        = "OFF",
           MAP_LABEL                       = "OFF"
           )
