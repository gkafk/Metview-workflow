import metview as mv

default_text_size = 0.35

empty_title = mv.mtext(text_line_count=0)

white = mv.mtext(
           TEXT_COLOUR         = "white",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6
           )

black = mv.mtext(
           TEXT_COLOUR         = "black",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6
           )

blue = mv.mtext(
           TEXT_COLOUR         = "blue",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6
           )

red = mv.mtext(
           TEXT_COLOUR         = "red",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6,
           TEXT_JUSTIFICATION  ="left"
           )

green = mv.mtext(
           TEXT_COLOUR         = "green",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6
           )

purple = mv.mtext(
           TEXT_COLOUR         = "purple",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6
           )

yellow = mv.mtext(
           TEXT_COLOUR         = "yellow",
           TEXT_FONT           = "ARIAL",
           TEXT_FONT_SIZE      = default_text_size,
           TEXT_MODE           = "POSITIONAL",
           TEXT_BOX_X_POSITION = 6
           )


met_power = mv.mtext(
    text_lines          = ["Powered by Metview ECMWF"],
    text_justification  = 'left',
    text_font_size      = 0.3,
    text_mode           = "positional",
    text_box_x_position = 24.9,
    text_box_y_position = 1.0,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

temperature = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' where='shortName=t'/>",
                           "VALID TIME:  <font colour='black'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=t'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

synop = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' where='shortName=gh'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=gh'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 6.2,
    text_box_y_length   = 2.3,
    text_box_blanking   = "on",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

left_cross_map = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                            "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' />",
                            "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' /></font> "],
    text_justification  = 'left',
    text_font_size      = 0.2,
    text_mode           = "positional",
    # text_mode           = "title",
    text_box_x_position = 2.2,
    text_box_y_position = -0.7,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

right_cross_map = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' />",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' /></font> "],
    text_justification  = 'left',
    text_font_size      = 0.2,
    text_mode           = "positional",
    text_box_x_position = 0.75,
    text_box_y_position = -0.7,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

left = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' />",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' /></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

left_black = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='black'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' />",
                           "VALID TIME:  <font colour='black'> <grib_info key='valid-date' format='%a %d, %H:%M' /></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

left_red = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' />",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' /></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'red'
    )

preci_lights = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "Lightnings <font colour='red'> ( +++ ) </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'   where='shortName=tp'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'   where='shortName=tp'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

preci_snow = mv.mtext(
    text_lines          = ["<grib_info key='name'/> at <grib_info key='level'/> hPa  STEP <font colour='red'> <grib_info key='step' /> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'   where='shortName=tp'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'   where='shortName=tp'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

run_diff = mv.mtext(
    text_lines          = ["<grib_info key='name' where='shortName=gh'/> at <grib_info key='level' where='shortName=gh'/> hPa  STEP <font colour='red'> <grib_info key='step' where='shortName=gh'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' where='shortName=gh'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=gh'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

pv = mv.mtext(
    text_lines          = ["<grib_info key='name' where='shortName=pv'/> at <grib_info key='level' where='shortName=pv'/> hPa  STEP <font colour='red'> <grib_info key='step' where='shortName=pv'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' where='shortName=pv'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=pv'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

relative_vor = mv.mtext(
    text_lines          = ["<grib_info key='name' where='shortName=vo'/> at <grib_info key='level' where='shortName=vo'/> hPa  STEP <font colour='black'> <grib_info key='step' where='shortName=vo'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M' where='shortName=vo'/>",
                           "VALID TIME:  <font colour='black'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=vo'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

opera = mv.mtext(
    text_lines          = ["Opera cloud- preci - vis  STEP <font colour='red'> <grib_info key='step' where='shortName=vis'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=vis'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=vis'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

opera_winds = mv.mtext(
    text_lines          = ["Opera wind at <grib_info key='level' where='shortName=u'/>  STEP <font colour='red'> <grib_info key='step' where='shortName=u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=u'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

opera_wave = mv.mtext(
    text_lines          = ["Opera wave   STEP <font colour='red'> <grib_info key='step' where='shortName=swh'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=swh'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=swh'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size ,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

mis_txt = mv.mtext(
    text_lines          = ["TOTAL 3-hour <font colour='red'> <grib_info key='step'  where='shortName=hcc'/> </font> ",
                           "Lightnings <font colour='red'> ( +++ ) </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=hcc'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=hcc'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

stat_stab = mv.mtext(
    text_lines          = ["Static Stability at <grib_info key='level' where='shortName=t'/> hPa STEP <font colour='red'> <grib_info key='step'  where='shortName=t'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=t'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=t'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

therm_wind = mv.mtext(
    text_lines          = ["Thermal Wind at <grib_info key='level' where='shortName=u'/> hPa STEP <font colour='red'> <grib_info key='step'  where='shortName=u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=u'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

t_advection= mv.mtext(
    text_lines          = ["T-Advection STEP <font colour='red'> <grib_info key='step'  where='shortName=u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=u'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

q_vect = mv.mtext(
    text_lines          = ["Q-vectors STEP <font colour='red'> <grib_info key='step'  where='shortName=gh'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=gh'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=gh'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

total_cloud= mv.mtext(
    text_lines          = ["Total cloud cover STEP <font colour='red'> <grib_info key='step'  where='shortName=lcc'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=lcc'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=lcc'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

tot_wave= mv.mtext(
    text_lines          = ["Total wave STEP <font colour='red'> <grib_info key='step'  where='shortName=swh'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=swh'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M' where='shortName=swh'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )


jet = mv.mtext(
    text_lines          = ["Wind speed STEP <font colour='black'> <grib_info key='step' where='shortName=u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=u'/>",
                           "VALID TIME:  <font colour='black'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

wind_speed = mv.mtext(
    text_lines          = ["Wind speed STEP <font colour='black'> <grib_info key='step' where='shortName=u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=u'/>",
                           "VALID TIME:  <font colour='black'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

u10_wind = mv.mtext(
    text_lines          = ["10m Wind speed STEP <font colour='red'> <grib_info key='step' where='shortName=10u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=10u'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=10u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

u10_wind_gust = mv.mtext(
    text_lines          = ["10m Wind flags and gust STEP <font colour='red'> <grib_info key='step' where='shortName=10fg3'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=10fg3'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=10fg3'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )

u100_wind = mv.mtext(
    text_lines          = ["100m Wind speed STEP <font colour='red'> <grib_info key='step' where='shortName=100u'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=100u'/>",
                           "VALID TIME:  <font colour='red'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=100u'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'charcoal'
    )


AH = mv.mtext(
    text_lines          = ["Absolute humidity STEP <font colour='black'> <grib_info key='step' where='shortName=r'/> </font> ",
                           "START TIME: <grib_info key='base-date' format='%d-%m-%Y %H:%M'  where='shortName=r'/>",
                           "VALID TIME:  <font colour='black'> <grib_info key='valid-date' format='%a %d, %H:%M'  where='shortName=r'/></font> "],
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )

light_radar = mv.mtext(
    text_lines       = "<grib_info key='valid-date' where='shortName=litota3'/>",
    text_justification  = 'left',
    text_font_size      = default_text_size,
    text_mode           = "positional",
    text_box_x_position = 0.2,
    text_box_y_position = 1,
    text_box_x_length   = 8,
    text_box_y_length   = 2,
    text_box_blanking   = "off",
    text_border         = "off",
    text_border_colour  = "rgb(0.11,0.11,0.41)",
    text_colour         = 'black'
    )
