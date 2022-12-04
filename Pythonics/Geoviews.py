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



