import panel as pn
import matplotlib.pyplot as plt
import seaborn as sns
from wineapi import WineAPI, REDWINE_FILE, WHITEWINE_FILE
import io

# Loads javascript dependencies and configures Panel (required)
pn.extension()

# INITIALIZE API
api = WineAPI()
api.load_wine(REDWINE_FILE, WHITEWINE_FILE)

# Search Widgets (filtering our data)
wine_type = pn.widgets.Select(name = "Wine Type",
                              options = api.get_wine_types(), value = 'Red')
min_quality = pn.widgets.IntSlider(name = "Min Quality",
                                   start = 3, end = 9, step = 1, value = 5)
max_quality = pn.widgets.IntSlider(name = "Max Quality",
                                   start = 3, end = 9, step = 1, value = 8)
alcohol_range = pn.widgets.RangeSlider(name = "Alcohol Range",
                                       start = 8.0, end = 15.0,
                                       value = (9.0, 12.0), step = 0.1)

# Plotting widgets (configuring the rendering of our visualizations)
width = pn.widgets.IntSlider(name = "Width", start = 250,
                             end = 2000, step = 50, value = 700)
height = pn.widgets.IntSlider(name = "Height", start = 250,
                              end = 2000, step = 50, value = 450)

# CALLBACK FUNCTIONS

# CALLBACK: Scatterplot
def get_plot(wine_type, min_quality, max_quality,
             alcohol_range, width, height):
    df = api.filter_data(wine_type, min_quality, max_quality, alcohol_range)
    fig, ax = plt.subplots(figsize = (width / 100, height / 100))
    sns.scatterplot(data = df, x = 'alcohol', y = 'quality', ax = ax)
    ax.set_title(f'{wine_type} Wine: Alcohol vs Quality')
    ax.set_xlabel('Alcohol (%)')
    ax.set_ylabel('Quality')
    plt.tight_layout()
    return pn.pane.Matplotlib(fig, tight=True, width=width, height=height)

# CALLBACK: Table
def get_catalog(wine_type, min_quality, max_quality, alcohol_range):
    df = api.filter_data(wine_type, min_quality, max_quality, alcohol_range)
    return pn.widgets.Tabulator(df, selectable = False)

# CALLBACK: CSV Download
def get_csv():
    df = api.filter_data(
        wine_type.value,
        min_quality.value,
        max_quality.value,
        alcohol_range.value
    )
    buffer = io.StringIO()
    df.to_csv(buffer, index = False)
    buffer.seek(0)
    return buffer

download_button = pn.widgets.FileDownload(
    callback = get_csv,
    filename = "filtered_wine_data.csv",
    label = "⬇ Download CSV",
    button_type = "primary"
)

# CALLBACK: Bar Chart
def get_bar_chart(wine_type, min_quality, max_quality, alcohol_range):
    df = api.filter_data(wine_type, min_quality, max_quality, alcohol_range)
    fig, ax = plt.subplots(figsize = (7, 4.5))  # 700x450 in inches
    sns.countplot(data = df, x = 'quality', color = 'skyblue', ax = ax)
    ax.set_title(f'{wine_type} Wines by Quality Score')
    ax.set_xlabel('Quality Score')
    ax.set_ylabel('Count')
    plt.tight_layout()
    return pn.pane.Matplotlib(fig, tight = True, width = 700, height = 450)

# CALLBACK BINDINGS (Connecting widgets to callback functions)
plot = pn.bind(get_plot, wine_type, min_quality,
               max_quality, alcohol_range, width, height)
catalog = pn.bind(get_catalog, wine_type, min_quality,
                  max_quality, alcohol_range)
bar_chart = pn.bind(get_bar_chart, wine_type, min_quality,
                    max_quality, alcohol_range)

# DASHBOARD WIDGET CONTAINERS ("CARDS")

card_width = 320

search_card = pn.Card(
    pn.Column(
        # Widget 1
        wine_type,
        # Widget 2
        min_quality,
        # Widget 3
        max_quality,
        # Widget 4
        alcohol_range,
        # Widget 5
        download_button
    ),
    title = "Filter Options",
    width = card_width,
    collapsed = False
)

plot_card = pn.Card(
    pn.Column(
        width,
        height
    ),
    title = "Plot Settings",
    width = card_width,
    collapsed = False
)

# LAYOUT
layout = pn.template.FastListTemplate(
    title = "Wine Quality Explorer",
    sidebar = [
        search_card,
        plot_card,
    ],
    theme_toggle = False,
    main = [
        pn.Tabs(
            ("Wine Alcohol vs Quality Scatterplot", plot),
            ("Wine Quality Bar Graph", bar_chart),
            ("Wine Data Table (optional filtering)", catalog),
            active = 0
        )
    ],
    header_background = '#8e44ad'
).servable()

layout.show()
