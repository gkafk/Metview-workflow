import metview as mv

default_text_size = 0.3

white = mv.mlegend(
          legend_title              = "off",
          legend_title_orientation  = "horizontal",
          legend_text_colour        = "white",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 0.3,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "white"
          )

blue = mv.mlegend(
          legend_title              = "off",
          legend_title_orientation  = "horizontal",
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 0.3,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

clouds = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "High  clouds           -   Medium  clouds             -  Low  clouds",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_label_frequency    = 20,
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

vis = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Visibility (m)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

t_advection = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Temperature advection (ᵒC/h)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "black"
          )

PV = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Potential vorticity (PVU)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "red"
          )

AH = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Absolute humidity (g/mᵌ)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size    = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "black"
          )

RH = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Relative humidity (%)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          LEGEND_USER_MAXIMUM       = "ON",
          LEGEND_USER_MAXIMUM_TEXT  = "%",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "red",
          legend_text_font_size    = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "red"
          )

relative_vor = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Relative vorticity (x10⁻⁵s ⁻¹)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "red"
          )

snowfall = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Snowfall (mm)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

total_preci = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Total Precipitation (mm)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

tot_wave = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Total Wave (m)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

sst = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Sea surface temperature (ᵒC)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "black",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "black"
          )

mis = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Βροχή mm     -   Χιονιού mm      -    Άνεμος m/s",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

opera = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Βάση νεφών ft - Ποσότητα χαμηλών νεφών  -  Ορατότητα m -   Υετός mm ",
          legend_title_font_size    = 0.30,
          legend_display_type       = "disjoint",
          legend_title_orientation  = "horizontal",
          legend_text_composition   = "USER_TEXT_ONLY",
          legend_user_lines         = ["<= 3000 FT",">= BKN","5000 m","2 mm", "5 mm", "10 mm", "20 mm", "50 mm", "150 mm"],
          legend_units_text         = "oC",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

opera_winds = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "850      -       925      -       1000 ",
          legend_title_font_size    = 0.40,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "kt",
          legend_title_position_ratio = 20.00,
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 6,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 15.00,
          legend_box_y_length       = 1.5,
          legend_border             = "on",
          legend_entry_border       = "on",
          legend_border_colour      = "blue",
          legend_box_blanking       = "on",
          # legend_display_type       = "histogram"
          # legend_display_type       = "disjoint"
          )

opera_wave = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Άνεμος  και κύμα",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "kt",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 6,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 15.00,
          legend_box_y_length       = 1.0,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue",
          legend_box_blanking       = "off",
          # legend_display_type       = "histogram"
          # legend_display_type       = "disjoint"
          )

stat_stab = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = "Static Stability (K/hPa)",
          legend_title_font_size    = 0.30,
          legend_title_orientation  = "horizontal",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "blue",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

therm_wind = mv.mlegend(
          legend_title              = "on",
          legend_title_text         = " Thermal Wind (m/s)",
          legend_title_font_size    = 0.30,
          legend_text_font_size     = default_text_size,
          legend_title_orientation  = "horizontal",
          LEGEND_USER_MAXIMUM       = "ON",
          LEGEND_USER_MAXIMUM_TEXT  = ">30",
          legend_units_text         = "mm",
          legend_title_position_ratio = 60.00,
          legend_text_colour        = "blue",
          legend_box_mode           = "positional",
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 1.00,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "blue"
          )

black = mv.mlegend(
          legend_title             = "off",
          legend_title_orientation = "horizontal",
          legend_text_colour       = "black",
          legend_label_frequency   = 2,
          legend_text_font_size    = default_text_size,
          legend_box_mode          = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position    = 0.5,
          legend_box_y_position    = 0.1,
          legend_box_x_length      = 27.00,
          legend_box_y_length      = 0.3,
          legend_border            = "off",
          legend_entry_border      = "off",
          legend_border_colour     = "black"
          )

red = mv.mlegend(
          legend_title              = "off",
          legend_title_orientation  = "horizontal",
          legend_text_colour        = "red",
          legend_label_frequency   = 2,
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 0.3,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "red"
          )

green = mv.mlegend(
          legend_title              = "off",
          legend_title_orientation  = "horizontal",
          legend_text_colour        = "green",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 0.3,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "green"
          )

purple = mv.mlegend(
          legend_title              = "off",
          legend_title_orientation  = "horizontal",
          legend_text_colour        = "purple",
          legend_text_font_size     = default_text_size,
          legend_box_mode           = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 0.3,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour      = "purple"
          )

yellow = mv.mlegend(
          legend_title = "off",
          legend_title_orientation = "horizontal",
          legend_text_colour = "yellow",
          legend_text_font_size    = default_text_size,
          legend_box_mode = "positional",
          legend_title_position_ratio = 60.00,
          legend_box_x_position     = 0.5,
          legend_box_y_position     = 0.1,
          legend_box_x_length       = 27.00,
          legend_box_y_length       = 0.3,
          legend_border             = "off",
          legend_entry_border       = "off",
          legend_border_colour = "yellow"
          )

large = mv.mlegend(
          legend_title             = "off",
          legend_title_orientation = "horizontal",
          legend_text_colour       = "black",
          legend_text_font_size    = default_text_size,
          legend_box_mode          = "positional",
          legend_label_frequency   = 2,
          legend_title_position_ratio = 60.00,
          legend_box_x_position    = 0.5,
          legend_box_y_position    = 0.1,
          legend_box_x_length      = 27.00,
          legend_box_y_length      = 0.3,
          legend_border            = "off",
          legend_entry_border      = "off",
          legend_border_colour     = "black"
          )


cross_sec = mv.mlegend(
          legend_title                  = "off",
           legend_title_orientation = "vertical",
          # legend_title_orientation = "horizontal",
          # legend_text_colour            = "red",
          # legend_box_mode               = "positional",
           legend_title_position_ratio = 60.00,
           legend_box_x_position     = 0.5,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 27.00,
           legend_box_y_length       = 1.00,
          # legend_border             = "off",
          # legend_entry_border       = "off",
          # legend_border_colour          = "red"
          )

di = mv.mlegend(
            LEGEND_TITLE                = "ON",
            LEGEND_AUTOMATIC_BOX_MARGIN = 1,
            LEGEND_TEXT_FONT_SIZE       = default_text_size,
            legend_title_text         = "Δείκτης Δυσφορίας",
            legend_title_font_size    = 0.30,
            legend_title_orientation  = "horizontal",
            legend_title_position_ratio = 60.00,
            legend_text_colour        = "blue",
            legend_box_mode           = "positional",
            legend_box_x_position     = 0.5,
            legend_box_y_position     = 0.1,
            legend_box_x_length       = 27.00,
            legend_box_y_length       = 1.00,
            legend_border             = "off",
            legend_entry_border       = "off",
            legend_border_colour      = "blue"
            )

# Lightnings
light_av1h = mv.mlegend(
            LEGEND_TITLE                = "ON",
            LEGEND_TITLE_TEXT           = "",
            LEGEND_TITLE_POSITION_RATIO = 30,
            LEGEND_USER_MAXIMUM         = "ON",
            LEGEND_USER_MAXIMUM_TEXT    = ">100 (100km-2/hour)",
            LEGEND_AUTOMATIC_BOX_MARGIN = 1,
            legend_title_font_size    = 0.30,
            legend_title_orientation  = "horizontal",
            legend_title_position_ratio = 60.00,
            legend_text_colour        = "blue",
            legend_box_mode           = "positional",
            legend_box_x_position     = 0.5,
            legend_box_y_position     = 0.1,
            legend_box_x_length       = 27.00,
            legend_box_y_length       = 1.00,
            legend_border             = "off",
            legend_entry_border       = "off",
            legend_border_colour      = "blue"
            )


light_yellow_red = mv.mlegend(
    legend_title                    = "on",
    legend_title_text               = "",
    legend_display_type             ="disjoint",
    legend_text_composition         = "user_text_only",
    legend_user_lines               = [ "Low probability","High probability" ],
    LEGEND_AUTOMATIC_BOX_MARGIN     = 1,
    legend_title_font_size          = 0.4,
    legend_title_orientation        = "horizontal",
    legend_title_position_ratio     = 60.00,
    legend_text_colour              = "blue",
    legend_box_mode                 = "positional",
    legend_box_x_position           = 0.5,
    legend_box_y_position           = 0.1,
    legend_box_x_length             = 27.00,
    legend_box_y_length             = 1.00,
    legend_border                   = "off",
    legend_entry_border             = "off",
    legend_border_colour            = "blue"
)

light_instant = mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "",
           LEGEND_TITLE_POSITION_RATIO = 30,
           LEGEND_USER_MAXIMUM         = "ON",
           LEGEND_USER_MAXIMUM_TEXT    = ">100 (100km-2/hour)",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           legend_title_font_size    = 0.30,
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           legend_text_colour        = "blue",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.5,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 27.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "blue"
           )

# zero level
zero_level = mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "",
           LEGEND_USER_MINIMUM         = "ON",
           LEGEND_USER_MINIMUM_TEXT    = "<",
           LEGEND_USER_MAXIMUM         = "ON",
           LEGEND_USER_MAXIMUM_TEXT    = "> 10000 FT",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           legend_title_font_size    = 0.30,
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           LEGEND_TEXT_FONT_SIZE       = default_text_size,
           legend_text_colour        = "blue",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.5,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 27.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "blue"
    )
# preci type
preci_type = mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "",
           LEGEND_TITLE_POSITION_RATIO = 30,
           LEGEND_DISPLAY_TYPE         = "DISJOINT",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           LEGEND_TEXT_FONT_SIZE       = default_text_size,
           LEGEND_TEXT_COMPOSITION     = "USER_TEXT_ONLY",
           LEGEND_USER_LINES           = [ "Rain","Freezing rain","Snow","Net snow","Sleet","Ice pellets" ],
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           legend_text_colour        = "blue",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.5,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 27.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "blue"
           )

# wind speed
wind_speed= mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "Wind speed",
           LEGEND_TITLE_POSITION_RATIO = 30,
           LEGEND_DISPLAY_TYPE         = "DISJOINT",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           LEGEND_TEXT_FONT_SIZE       = 0.2,
           LEGEND_TEXT_FONT_STYLE      = "bold",
           LEGEND_TEXT_COMPOSITION     = "USER_TEXT_ONLY",
           LEGEND_USER_LINES           = [ "11-16KT (4B)","17-21KT (5B)","22-27KT (6B)","28-33KT (7B)","34-40KT (8B)","41-47KT (9B)","48-55KT (10B)","56-63KT (11B)","64-71KT (12B)" ],
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           legend_text_colour        = "black",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.1,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 35.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "black"
           )
# wind gust
u10_wind_gust= mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "10m wind gust",
           LEGEND_TITLE_POSITION_RATIO = 30,
           LEGEND_DISPLAY_TYPE         = "DISJOINT",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           LEGEND_TEXT_FONT_SIZE       = 0.2,
           LEGEND_TEXT_FONT_STYLE      = "bold",
           LEGEND_TEXT_COMPOSITION     = "USER_TEXT_ONLY",
           LEGEND_USER_LINES           = [ "11-16KT (4B)","17-21KT (5B)","22-27KT (6B)","28-33KT (7B)","34-40KT (8B)","41-47KT (9B)","48-55KT (10B)","56-63KT (11B)","64-71KT (12B)" ],
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           legend_text_colour        = "black",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.1,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 30.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "black"
           )

# jet - αεροχείμαρρος
jet = mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "Jet",
           LEGEND_TITLE_POSITION_RATIO = 30,
           # LEGEND_DISPLAY_TYPE         = "DISJOINT",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           LEGEND_TEXT_FONT_SIZE       = default_text_size,
           # LEGEND_TEXT_FONT_STYLE      = "bold",
           # LEGEND_TEXT_COMPOSITION     = "USER_TEXT_ONLY",
           # LEGEND_USER_LINES           = [60,80,100,120,140,160,180,200],
           LEGEND_USER_MAXIMUM         = "ON",
           LEGEND_USER_MAXIMUM_TEXT    = ">180 KT",
           # LEGEND_USER_LINES           = [0,20,40,60,80,100,120,140,160,180,200],
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           legend_text_colour        = "black",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.1,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 30.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "black"
           )

# total_preci_rate
total_preci_rate = mv.mlegend(
           LEGEND_TITLE                = "ON",
           LEGEND_TITLE_TEXT           = "",
           LEGEND_TITLE_POSITION_RATIO = 30,
           LEGEND_USER_MAXIMUM         = "ON",
           LEGEND_USER_MAXIMUM_TEXT    = "   >200 mm/hr",
           LEGEND_AUTOMATIC_BOX_MARGIN = 1,
           LEGEND_TEXT_FONT_SIZE       = default_text_size,
           legend_title_orientation  = "horizontal",
           legend_title_position_ratio = 60.00,
           legend_text_colour        = "blue",
           legend_box_mode           = "positional",
           legend_box_x_position     = 0.5,
           legend_box_y_position     = 0.1,
           legend_box_x_length       = 27.00,
           legend_box_y_length       = 1.00,
           legend_border             = "off",
           legend_entry_border       = "off",
           legend_border_colour      = "blue"
   )


# critical limits
cri_limits = mv.mlegend(
        legend_title                 = "on",
        legend_title_text            = "",
        legend_title_position_ratio  = 60,
        legend_display_type          ="disjoint",
        legend_automatic_box_margin  = 1,
        legend_text_font_size        = default_text_size,
        LEGEND_TEXT_COMPOSITION      = "user_text_only",
        LEGEND_USER_LINES            = [ "SeaTemp>14°C","w.chill<0°C","w.chill<-15°C","wspd>27","wspd>35KT","wave>4m" ],
        LEGEND_AUTOMATIC_BOX_MARGIN = 1,
        legend_title_orientation  = "horizontal",
        legend_text_colour        = "blue",
        legend_box_mode           = "positional",
        legend_box_x_position     = 0.5,
        legend_box_y_position     = 0.1,
        legend_box_x_length       = 27.00,
        legend_box_y_length       = 1.00,
        legend_border             = "off",
        legend_entry_border       = "off",
        legend_border_colour      = "blue"
        )
