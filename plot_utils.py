import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.dates as mdates
import numpy as np
import seaborn as sns
import os




def convert_time_to_numeric(time_values):
    """
    Converts an array of time values to numeric values.

    Parameters:
    - time_values (array): Array of time values.

    Returns:
    - array: Array of numeric values representing time.
    """
    return [mdates.date2num(val) for val in time_values]


def convert_time_to_numeric2(time_values):
    """
    Converts an array of time values to numeric values.

    Parameters:
    - time_values (array): Array of time values.

    Returns:
    - array: Array of numeric values representing time.
    """
    return [val.toordinal() for val in time_values]


def reshape_values_based_on_time(values, time_values):
    """
    Reshapes values to match the shape of time values.

    Parameters:
    - values (array): Array of variable values.
    - time_values (array): Array of time values.

    Returns:
    - array: Reshaped array of variable values.
    """
    return values[:len(time_values)]


def time_values(data):
    """
    Extracts time values from the given data object.

    Parameters:
    - data (pandas DataFrame or xarray DataArray): The input data object containing time information.

    Returns:
    - array: Array of time values.
    """
    return data.time.values


def flatten_data(data):
    """
    Flattens a multi-dimensional array of values.

    Parameters:
    - data (pandas DataFrame or xarray DataArray): The input data object containing variable values.

    Returns:
    - array: Flattened array of variable values.
    """
    return data.values.flatten()


def plot_time_series(time_values, variable_values, variable_name, save_dir=None, unit='',color=None):
    """
    Plots a time series.

    Parameters:
    - time_values (array): Array of time values.
    - variable_values (array): Array of variable values.
    - variable_name (str): Name of the variable to be displayed in labels and title.
    - save_dir (str): Directory to save the plot. If None, the plot is not saved.
    - unit (str): The unit of measurement for the variable, e.g., 'm/s' for meters per second.
    - color (str): Color of the plot.

    Returns:
    - None
    """

    # Convert cftime datetime values to Python datetime objects
    time_values = convert_time_to_numeric(time_values) #[mdates.date2num(val) for val in time_values]

    # Reshape variable values to match the shape of time values
    variable_values = reshape_values_based_on_time(variable_values, time_values) #variable_values[:len(time_values)]

    # Plotting the time series
    plt.figure(figsize=(12, 6))
    plt.plot(mdates.num2date(time_values), variable_values, label=variable_name, color=color)
    plt.xlabel('Time')
    plt.ylabel(f'{variable_name} ({unit})')
    plt.title(f'{variable_name} Time Series')
    plt.legend()
    plt.grid(False)

    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{variable_name.lower().replace(" ", "_")}_Time_Series.png'))

    # Display the plot
    plt.show()





def plot_dual_time_series(primary_time, primary_values, primary_label, primary_color, secondary_time, secondary_values, secondary_label, secondary_color, save_dir=None, unit_primary='', unit_secondary=''):
    """
    Plots two time series on the same plot with a secondary y-axis.

    Parameters:
    - primary_time (array): Array of time values for the primary time series.
    - primary_values (array): Array of variable values for the primary time series.
    - primary_label (str): Label for the primary time series.
    - primary_color (str): Color for the primary time series.

    - secondary_time (array): Array of time values for the secondary time series.
    - secondary_values (array): Array of variable values for the secondary time series.
    - secondary_label (str): Label for the secondary time series.
    - secondary_color (str): Color for the secondary time series.

    - save_dir (str): Directory to save the plot. If None, the plot is not saved.
    - unit_primary (str): Unit for the primary variable.
    - unit_secondary (str): Unit for the secondary variable.

    Returns:
    - None
    """


    # Convert primary_time and secondary_time to numeric values
    primary_time_numeric = convert_time_to_numeric(primary_time) #[mdates.date2num(val) for val in primary_time]
    secondary_time_numeric = convert_time_to_numeric(secondary_time) #[mdates.date2num(val) for val in secondary_time]

    # Reshape primary and secondary values to match the shape of time values
    primary_values = reshape_values_based_on_time(primary_values, primary_time) #primary_values[:len(primary_time_numeric)]
    secondary_values = reshape_values_based_on_time(secondary_values, secondary_time) #secondary_values[:len(primary_time_numeric)]

    # Create a figure and axis for the plot
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plotting the primary time series on the left y-axis
    ax1.plot(mdates.num2date(primary_time_numeric), primary_values, label=primary_label, color=primary_color)
    ax1.set_xlabel('Time')
    ax1.set_ylabel(f'{primary_label} ({unit_primary})')
    ax1.tick_params(axis='y')
    ax1.legend(loc='upper left')
    plt.grid(False)

    # Creating a secondary y-axis for the secondary time series on the right
    ax2 = ax1.twinx()
    ax2.plot(mdates.num2date(secondary_time_numeric), secondary_values, label=secondary_label, color=secondary_color)
    ax2.set_ylabel(f'{secondary_label} ({unit_secondary})')
    ax2.tick_params(axis='y')
    ax2.legend(loc='upper right')
    # Display the plot
    plt.title(f'{primary_label} VS {secondary_label} Time Series')
    plt.grid(False)

    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{primary_label.lower().replace(" ", "_")}_{secondary_label.lower().replace(" ", "_")}_Time_Series.png'))

    plt.show()



def plot_correlation_heatmap(data1, data2, save_dir=None, data1_label='', data2_label=''):
    """
    Plots a correlation heatmap for the given datasets.

    Parameters:
    - data1 (xarray.DataArray): DataArray containing time and variable values for the first dataset.
    - data2 (xarray.DataArray): DataArray containing time and variable values for the second dataset.
    - save_path (str): Path to save the plot. If None, the plot is not saved.
    - data1_label (str): Label for the first dataset.
    - data2_label (str): Label for the second dataset.

    Returns:
    - None
    """

    # Convert time values to numeric
    time_values_numeric_1 = convert_time_to_numeric2(time_values(data1))
    time_values_numeric_2 = convert_time_to_numeric2(time_values(data2))

    # Reshape values based on time
    values_1 = reshape_values_based_on_time(flatten_data(data1), time_values_numeric_1)
    values_2 = reshape_values_based_on_time(flatten_data(data2), time_values_numeric_2)

    # Load the reshaped data into DataFrames
    df1 = pd.DataFrame({'Time': time_values_numeric_1, f'{data1_label}': values_1})
    df2 = pd.DataFrame({'Time': time_values_numeric_2, f'{data2_label}': values_2})

    # Convert time to datetime
    df1['Time'] = pd.to_datetime(df1['Time'], origin='julian', unit='D')
    df2['Time'] = pd.to_datetime(df2['Time'], origin='julian', unit='D')

    # Set Time as the index
    df1.set_index('Time', inplace=True)
    df2.set_index('Time', inplace=True)

    # Resample data to monthly averages
    df1_monthly = df1.resample('M').mean()
    df2_monthly = df2.resample('M').mean()

    # Combine DataFrames
    df_combined = pd.concat([df1_monthly, df2_monthly], axis=1)

    # Calculate correlation matrix
    correlation_matrix = df_combined.corr()

    # Plot correlation heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Correlation Heatmap for {" and ".join(df_combined.columns)}')


    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{data1_label.lower().replace(" ", "_")}_and_{data2_label.lower().replace(" ", "_")}_correlation_heatmap.png'))

    # Show the plot
    plt.show()
    



def visualize_linear_regression(X, y, test_size=0.2, random_state=42, save_dir=None, x_lab='', y_lab='',x_unit='', y_unit=''):
    """
    Visualizes linear regression for the given data.

    Parameters:
    - X (array-like): Independent variable values.
    - y (array-like): Dependent variable values.
    - test_size (float): The proportion of the dataset to include in the test split.
    - random_state (int): Controls the randomness of the training and testing splits.
    - save_path (str): Path to save the plot. If None, the plot is not saved.

    Returns:
    - None
    """

    # reshape X values
    X = X.values.reshape(-1, 1)
    # flatten y values
    y = y.values.flatten()
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    # Predict dependent variable for the test set
    y_pred = model.predict(X_test)

    # Extract the coefficients and intercept
    slope = model.coef_[0]
    intercept = model.intercept_

    # Visualize the model
    plt.figure(figsize=(10, 6))

    # Scatter plot of the data points
    plt.scatter(X_test, y_test, color='blue', label='Actual Data')

    # Plot the regression line
    label = f'Regression Line (y = {slope:.2e}x + {intercept:.2e})'
    plt.plot(X_test, y_pred, color='red', linewidth=2, label=label)

    # Add labels and title
    plt.xlabel(f'{x_lab} {x_unit}')
    plt.ylabel(f'{y_lab} {y_unit}')
    plt.title(f'Linear Regression: Vertical {x_lab} vs. {y_lab}')
    plt.legend()
    plt.grid(False)

        
    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{x_lab.lower().replace(" ", "_")}_and_{y_lab.lower().replace(" ", "_")}_linear_regression.png'))

    # Show the plot
    plt.show()

