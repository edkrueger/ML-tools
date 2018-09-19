from bokeh.plotting import figure, show
import pandas as pd

# note: to render bokeh plots in a notebook add the following two line *to the notebook*
# from bokeh.plotting import output_notebook
# output_notebook()

def smooth_plot(df, label_postion, frequencies):
    
    """
    Returns a bokeh plot of a time series smoothed at different frenquencies.
    
    Arguments
    ---------
    df (DataFrame): A time series DataFrame.
    label_position (str or int): A label or column index.
    time_groups (array-like): A list of smoothing times. Example: ["5min", "15min", "30min", "1h"]
    """
    
    # get the signal's name
    if isinstance(label_postion, str):
        signal_name = label_postion

    elif isinstance(label_postion, int):
        signal_name = df.columns[label_postion]

    else:
        raise TypeError("num_name must be an int or a str.")
        
    # create the color palate
    from bokeh.palettes import Category10 as palette
    palette = palette[10]
    palette = iter(palette)
    
    # create the plot
    p = figure(plot_width=800, plot_height=400,
               x_axis_type="datetime", title="{signal_name}".format(signal_name=signal_name))
    
    for frequency in frequencies:
        
        grouped_df = df.groupby(pd.Grouper(freq=frequency)).mean()

        x_values = grouped_df.index
        y_values = grouped_df[signal_name]
        
        # add the line
        p.step(x=x_values, y=y_values, legend=frequency + " average", color=next(palette))
        
    show(p)
    
    return p