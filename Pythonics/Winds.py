
import metview as mv

wind_speed_1 = mv.mwind(
                           WIND_FIELD_TYPE          = "FLAGS",
                           wind_flag_origin_marker  = "off",
                           WIND_THINNING_FACTOR     = 10,
                           WIND_ADVANCED_METHOD     = "OFF",# otan einai ON ta anemakia einai xromatista
                           WIND_FLAG_CALM_INDICATOR = "OFF",
                           WIND_FLAG_COLOUR         = "BLACK",
                           WIND_FLAG_LENGTH         = 1,
                           WIND_FLAG_ORIGIN_MARKER  = "OFF",
                           wind_flag_min_speed      = 8.00,
                           WIND_FLAG_THICKNESS      = 1.8,
                           legend = "on"
                        )

black_flags = mv.mwind(
                           WIND_FIELD_TYPE          = "FLAGS",
                           WIND_THINNING_FACTOR     = 15,
                           WIND_FLAG_CALM_INDICATOR = "OFF",
                           WIND_FLAG_CALM_BELOW     = 5.5,
                           WIND_FLAG_COLOUR         = "BLACK",
                           WIND_FLAG_ORIGIN_MARKER  = "OFF",
                           WIND_FLAG_LENGTH         = 1,
                           WIND_FLAG_THICKNESS      = 2
                           )

blue_flags = mv.mwind(
                           WIND_FIELD_TYPE          = "FLAGS",
                           WIND_THINNING_FACTOR     = 15,
                           WIND_FLAG_CALM_INDICATOR = "OFF",
                           WIND_FLAG_CALM_BELOW     = 5.5,
                           WIND_FLAG_COLOUR         = "rgb(32, 99, 154)",
                           WIND_FLAG_ORIGIN_MARKER  = "OFF",
                           WIND_FLAG_LENGTH         = 1,
                           WIND_FLAG_THICKNESS      = 2 # παίρνει μόνο ακέραιο
                           )

black_arrows = mv.mwind(
                           WIND_FIELD_TYPE          = "ARROWS",
                           WIND_THINNING_FACTOR     = 10,
                           WIND_FLAG_CALM_INDICATOR = "OFF",
                           WIND_FLAG_CALM_BELOW     = 5.5,
                           WIND_FLAG_COLOUR         = "BLACK",
                           WIND_FLAG_ORIGIN_MARKER  = "OFF",
                           WIND_FLAG_LENGTH         = 1,
                           WIND_FLAG_THICKNESS      = 1
                           )

mis_wind_plot = mv.mwind(
                           WIND_FIELD_TYPE                          = "FLAGS",
                           WIND_THINNING_FACTOR                     = 15,
                           WIND_ADVANCED_METHOD                     = "ON",
                           WIND_ADVANCED_COLOUR_SELECTION_TYPE      = "LIST",
                           WIND_ADVANCED_COLOUR_LEVEL_LIST          = [ 4,12,102.889 ],
                           WIND_ADVANCED_COLOUR_TABLE_COLOUR_METHOD = "LIST",
                           WIND_ADVANCED_COLOUR_LIST                = [ "RGB(0.3725,0.3725,0.3725)","RED_ORANGE" ],
                           WIND_FLAG_COLOUR                         = "BLACK",
                           WIND_FLAG_LENGTH                         = 1,
                           WIND_FLAG_ORIGIN_MARKER                  = "OFF",
                           WIND_FLAG_THICKNESS                      = 2
                       )

mis_wind_plot_arrows = mv.mwind(
                           WIND_THINNING_FACTOR                     = 5,
                           LEGEND                                   = "ON",
                           WIND_ADVANCED_METHOD                     = "ON",
                           WIND_ADVANCED_COLOUR_SELECTION_TYPE      = "LIST",
                           WIND_ADVANCED_COLOUR_LEVEL_LIST          = [ 2,4,6,9,11,14,17,21,25,29,33,37 ],
                           WIND_ADVANCED_COLOUR_TABLE_COLOUR_METHOD = "LIST",
                           WIND_ADVANCED_COLOUR_LIST                = [ "RGB(0.9469,0.93,0.6923)","RGB(0.9606,0.9406,0.561)","ORANGISH_YELLOW","YELLOWISH_ORANGE","RED_ORANGE","GREEN","KELLY_GREEN","BLUISH_PURPLE","GREY","BURGUNDY","BLUE" ],
                           WIND_ARROW_THICKNESS                     = 2
                        )

# define wind vector plotting for opera winds
wind_plot_1000 = mv.mwind(
                            wind_field_type           = "flags",
                            wind_thinning_factor      = 3,
                            legend                    = "on",
                            wind_flag_colour          = "black",
                            wind_flag_length          = 1,
                            wind_flag_origin_marker   = "off",
                            wind_flag_thickness       = 2
                            )

wind_plot_925 = mv.mwind(
                            wind_field_type           = "flags",
                            wind_thinning_factor      = 3,
                            legend                    = "on",
                            wind_flag_colour          = "red",
                            wind_flag_length          = 1,
                            wind_flag_origin_marker   = "off",
                            wind_flag_thickness       = 2
                            )

wind_plot_850 = mv.mwind(
                            wind_field_type           = "flags",
                            wind_thinning_factor      = 3,
                            legend                    = "on",
                            wind_flag_colour          = "blue",
                            wind_flag_length          = 1,
                            wind_flag_origin_marker   = "off",
                            wind_flag_thickness       = 2
                            )

wind_plot_wave = mv.mwind(
                           WIND_FIELD_TYPE          = "FLAGS",
                           WIND_THINNING_FACTOR     = 3,
                           WIND_FLAG_CALM_INDICATOR = "OFF",
                           WIND_FLAG_CALM_BELOW     = 5.5,
                           WIND_FLAG_COLOUR         = "BLACK",
                           WIND_FLAG_ORIGIN_MARKER  = "OFF",
                           WIND_FLAG_THICKNESS      = 2
                           )
wind_wave_plot = mv.mwind(
                             wind_thinning_factor                  = 3,
                             legend                                = "on",
                             WIND_ARROW_COLOUR                     = "black",
                             wind_advanced_method                  = "off",
                             wind_advanced_colour_parameter        = "parameter",
                             wind_advanced_colour_max_level_colour = "black",
                             wind_advanced_colour_min_level_colour = "violet",
                             wind_advanced_colour_direction        = "clockwise",
                            # wind_field_type                       = "flags",
                             wind_field_type                       = "arrows",
                             wind_arrow_unit_velocity              = 8,
                             wind_arrow_thickness                  = 1
                            )

therm_wind = mv.mwind(
                           WIND_FIELD_TYPE          = "ARROWS",
                           WIND_THINNING_FACTOR     = 5,
                           WIND_ARROW_COLOUR        = "BLACK",
                           WIND_FLAG_CALM_INDICATOR = "OFF",
                           WIND_FLAG_CALM_BELOW     = 5.5,
                           WIND_FLAG_COLOUR         = "BLACK",
                           WIND_FLAG_ORIGIN_MARKER  = "OFF",
                           WIND_FLAG_LENGTH         = 1,
                           WIND_FLAG_THICKNESS      = 1
                           )

q_vec_arrows= mv.mwind(
               WIND_FIELD_TYPE           = "ARROWS",
               WIND_THINNING_FACTOR      = 2,
               Legend                    = "off",
               WIND_ADVANCED_METHOD      = "off",
               WIND_ARROW_CALM_INDICATOR = "OFF",
               wind_arrow_calm_below     = 0.5,
               WIND_ARROW_COLOUR         = "BLACK",
               wind_arrow_head_shape     = 0,
               WIND_ARROW_HEAD_RATIO     = 0.3,
               wind_arrow_fixed_velocity = 0,
               WIND_ARROW_THICKNESS      = 2,
               wind_arrow_style          = "solid",
               wind_arrow_unit_velocity  = 25.0
               )
