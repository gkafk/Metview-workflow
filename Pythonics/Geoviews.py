'''
This is the list of Magics predefined projections:

['north_pole', 'eurasia', 'global', 'south_west_europe',
'east_tropic', 'south_east_europe', 'south_east_asia_and_indonesia',
'northern_africa', 'antarctic', 'central_europe',
'pacific', 'southern_asia', 'south_america',
'north_east_europe', 'north_west_europe', 'europe',
'arctic', 'central_america', 'southern_africa',
'eastern_asia', 'middle_east_and_india', 'west_tropic',
'south_pole', 'south_atlantic_and_indian_ocean',
'equatorial_pacific', 'australasia', 'north_atlantic',
'western_asia', 'north_america']

'''

import metview as mv

mediterra = mv.geoview(
          # COASTLINES             = Coastlines,
          MAP_PROJECTION         = "EPSG:4326",
          MAP_AREA_DEFINITION    = "CORNERS",
          AREA                   = [ 29.93,10.0,51.2,40.0], #S,W,N,E
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )

hellas_cyprus = mv.geoview(
          # COASTLINES             = Coastlines,
          MAP_PROJECTION         = "EPSG:4326",
          MAP_AREA_DEFINITION    = "CORNERS",
          AREA                   = [ 29.93,15.8,44.9,37.0], #S,W,N,E
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )

euro_polar_Large = mv.geoview(
          # COASTLINES             = Coastlines,
          MAP_PROJECTION         = "POLAR_STEREOGRAPHIC",
          AREA                   = [ 28,-20.6,52.3,60.6], #S,W,N,E
          MAP_AREA_DEFINITION    = "CORNERS",
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )

greece = mv.geoview(
          MAP_PROJECTION         = "EPSG:4326",
          MAP_AREA_DEFINITION    = "CORNERS",
          AREA                   = [34,19,43.20,32 ],#S,W,N,E
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )

lights_radar = mv.geoview(
          MAP_PROJECTION         = "EPSG:4326",
          MAP_AREA_DEFINITION    = "CORNERS",
          AREA                   = [34.8,20,42,30.183 ],#S,W,N,E
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )

euro_cyli = mv.geoview(
           MAP_PROJECTION         = "EPSG:4326",
          # MAP_PROJECTION         = "POLAR_STEREOGRAPHIC",
          MAP_AREA_DEFINITION    = "CORNERS",
          AREA                   = [ 28,-7,61.33,40.1 ],#S,W,N,E
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )


euro_polar = mv.geoview(
          # MAP_PROJECTION         = "EPSG:4326",
          MAP_PROJECTION         = "POLAR_STEREOGRAPHIC",
          MAP_AREA_DEFINITION    = "CORNERS",
           AREA                   = [  32.0, -7.0, 44.0,  50.0],#S,W,N,E
          # AREA                   = [  32.2, -7.0, 45.0,  45.0],#S,W,N,E
          SUBPAGE_X_POSITION     = 0,
          SUBPAGE_Y_POSITION     = 0,
          SUBPAGE_X_LENGTH       = 100,
          SUBPAGE_Y_LENGTH       = 100,
          PAGE_FRAME             = "ON",
          PAGE_FRAME_COLOUR      = "SKY",
          SUBPAGE_FRAME_COLOUR   = "BACKGROUND",
          MAP_VERTICAL_LONGITUDE = 0
          )


## coastlines για τους παρακάτω χάρτες
#land_light_grey = mv.mcoast(
      #MAP_COASTLINE_THICKNESS         = 1.5,
      #MAP_COASTLINE_LAND_SHADE        = "ON",
      #MAP_COASTLINE_LAND_SHADE_COLOUR = "RGB(0.9255,0.9255,0.9255)",
      #MAP_BOUNDARIES                  = "ON",
      #MAP_GRID_LINE_STYLE             = "DASH",
      #MAP_GRID_LATITUDE_INCREMENT     = 1,
      #MAP_GRID_LONGITUDE_INCREMENT    = 1,
      #MAP_LABEL_HEIGHT                = 0.4
      #)

#Xios_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 37.21,24.37,39.50,27.39 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #MAP_VERTICAL_LONGITUDE = 0,
          #PAGE_FRAME             = "off",
          #COASTLINES             = land_light_grey
          #)

#Limnos_Mitilini_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 38.57,24.21,40.735,27.27 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #PAGE_FRAME             = "off",
          #MAP_VERTICAL_LONGITUDE = 0,
          #COASTLINES             = land_light_grey
          #)

#Rodos_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 35.48,26.23,37.645,29.29 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #PAGE_FRAME             = "off",
          #MAP_VERTICAL_LONGITUDE = 0,
          #COASTLINES             = land_light_grey
          #)

#Crete_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 33.58,23.42,35.745,26.48 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #PAGE_FRAME             = "off",
          #MAP_VERTICAL_LONGITUDE = 0,
          #COASTLINES             = land_light_grey
          #)

   
#North_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 36.62,19.94,42.05,27.62 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #PAGE_FRAME             = "off",
          #MAP_VERTICAL_LONGITUDE = 0,
          #COASTLINES             = land_light_grey
          #)

#T_North_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 37.92,25.77,42.28,31.89 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #PAGE_FRAME             = "off",
          #MAP_VERTICAL_LONGITUDE = 0,
          #COASTLINES             = land_light_grey
          #)

#T_South_cylin = mv.geoview(
          #MAP_AREA_DEFINITION    = "CORNERS",
          #AREA                   = [ 35.65,25.9,39.54,31.4 ],#S,W,N,E
          #SUBPAGE_X_POSITION     = 0,
          #SUBPAGE_Y_POSITION     = 0,
          #SUBPAGE_X_LENGTH       = 100,
          #SUBPAGE_Y_LENGTH       = 100,
          #PAGE_FRAME             = "off",
          #MAP_VERTICAL_LONGITUDE = 0,
          #COASTLINES             = land_light_grey
          #)

#W_of_Cyprus_cylin = mv.geoview(
            #MAP_AREA_DEFINITION    = "CORNERS",
            #AREA                   = [ 33.69,27.91,38.19,34.27 ],#S,W,N,E
            #SUBPAGE_X_POSITION     = 0,
            #SUBPAGE_Y_POSITION     = 0,
            #SUBPAGE_X_LENGTH       = 100,
            #SUBPAGE_Y_LENGTH       = 100,
            #PAGE_FRAME             = "off",
            #MAP_VERTICAL_LONGITUDE = 0,
            #COASTLINES             = land_light_grey
            #)
