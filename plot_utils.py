import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import os

def plot_time_series(time_values, variable_values, variable_name, save_dir=None, unit=''):
    """
    Plots a time series.

    Parameters:
    - time_values (array): Array of time values.
    - variable_values (array): Array of variable values.
    - variable_name (str): Name of the variable to be displayed in labels and title.
    - save_dir (str): Directory to save the plot. If None, the plot is not saved.
    - unit (str): The unit of measurement for the variable, e.g., 'm/s' for meters per second.

    Returns:
    - None
    """

    # Convert cftime datetime values to Python datetime objects
    time_values = [mdates.date2num(val) for val in time_values]

    # Reshape variable values to match the shape of time values
    variable_values = variable_values[:len(time_values)]

    # Plotting the time series
    plt.figure(figsize=(12, 6))
    plt.plot(mdates.num2date(time_values), variable_values, label=variable_name)
    plt.xlabel('Time')
    plt.ylabel(f'{variable_name} ({unit})')
    plt.title(f'{variable_name} Time Series')
    plt.legend()
    plt.grid(False)

    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{variable_name}_Time_Series.png'))

    # Display the plot
    plt.show()


