from dataclasses import dataclass
from bokeh.io import show
from bokeh.palettes import turbo, Paired8
from bokeh.plotting import figure, output_file
from bokeh.transform import factor_cmap, cumsum

from math import pi
from numpy import source

import pandas as pd


def vbar(data_to_plot, output_name, x_label, y_label):
    output_file(filename=f"{output_name}.html", title="prueba")

    x = list(data_to_plot.keys())
    y = list(data_to_plot.values())

    for i in range(len(x)):
        if x[i] == "":
            x[i] = "Sin dato"

    p = figure(
        x_range=x,
        title=f"Número de {output_name}",
        x_axis_label=x_label,
        y_axis_label=y_label,
        tooltips=[(f"{x_label}", "@x"), (f"Número {y_label}", "@top")],
        plot_width=1000,
        plot_height=900,
    )

    # source = ColumnDataSource(data=departamentos)

    p.vbar(x=x,
           top=y,
           width=0.9,
           line_color='white',
           fill_color=factor_cmap('x', palette=turbo(len(x)), factors=x))

    p.xaxis.major_label_orientation = 1
    p.title.text_font_size = "20px"
    p.xaxis.axis_label_text_font_size = "20px"
    p.yaxis.axis_label_text_font_size = "20px"
    p.xaxis.axis_label_text_font_style = "bold"
    p.yaxis.axis_label_text_font_style = "bold"
    # p.legend.orientation = "horizontal"

    show(p)


# def vbar_stack(data_to_plot, output_name, x_label, y_label):
#     output_file(filename=f"{output_name}.html", title=output_name)

#     x = list(data_to_plot.keys())
#     y = []
#     data = {
#         "x": x,
#     }

#     for key in data_to_plot:
#         for value in data_to_plot[key]:
#             if (list(value.keys())[0] not in y):
#                 y.append((list(value.keys())[0]))

#     y.sort()

#     # for key in data_to_plot:
#     #     for value in data_to_plot[key]:
#     #         for j in y:

#     p = figure(
#         x_range=x,
#         title=f"Número de {output_name}",
#         tooltips=[(f"{x_label}", "@x"), (f"Número {y_label}", "@top")],
#         plot_width=1000,
#         plot_height=1000,
#     )

#     p.vbar_stack(y,
#                  x="x",
#                  width=0.9,
#                  line_color='white',
#                  source=data,
#                  legend_label=y,
#                  fill_color=factor_cmap('x',
#                                         palette=turbo((len(y))),
#                                         factors=x))

#     p.y_range.start = 0
#     p.x_range.range_padding = 0.1
#     p.xgrid.grid_line_color = None
#     p.axis.minor_tick_line_color = None
#     p.outline_line_color = None
#     p.legend.location = "top_left"
#     p.legend.orientation = "horizontal"

# show(p)


def circle(data_to_plot):
    source = pd.Series(data_to_plot).reset_index(name='value').rename(
        columns={'index': 'GrupoEdad'})
    source['angle'] = source['value'] / source['value'].sum() * 2 * pi

    source['color'] = Paired8

    p = figure(height=1000,
               width=1000,
               title="Victimas por grupo de edad",
               toolbar_location=None,
               tools="hover",
               tooltips="@GrupoEdad: @value",
               x_range=(-0.5, 1.0))

    p.wedge(x=0,
            y=1,
            radius=0.5,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white",
            fill_color='color',
            legend_field='GrupoEdad',
            source=source)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    p.legend.click_policy = "hide"

    show(p)