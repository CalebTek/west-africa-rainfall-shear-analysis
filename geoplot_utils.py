import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import xarray as xr
import numpy as np
import os


def generate_array(start, num_output):
    start += 1.25
    return np.array([start + 2.5 * i for i in range(num_output)])


def plot_cartopy(data, variable_label, save_dir=None, unit=''):
    """
    Plot Cartopy map for a given xarray DataArray.

    Parameters:
    - data (xr.DataArray): xarray DataArray with 'lat', 'lon', and 'values'.
    - variable_label (str): Label for the variable to be shown on the colorbar.
    - save_path (str): Path to save the plot. If None, the plot is not saved.

    Returns:
    - None
    """
    # Create a Cartopy GeoAxes
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})

    # Plot the data using contourf
    cf = ax.contourf(data['lon'], data['lat'], data.isel(time=0), transform=ccrs.PlateCarree(), cmap='viridis')

    # Add colorbar
    cbar = plt.colorbar(cf, ax=ax, orientation='vertical', pad=0.1)
    cbar.set_label(f'{variable_label} {unit}')

    # Add coastlines, gridlines, etc.
    ax.coastlines()
    ax.gridlines(draw_labels=True)

    # Set the title
    ax.set_title(f'Mean {variable_label} West Africa')


    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{variable_label.lower().replace(" ", "_")}_geoplot.png'), bbox_inches='tight')
        
    # Show the plot
    plt.show()


def plot_cartopy_periodic(data, variable_label, save_dir=None, unit=''):
    """
    Plot mean Cartopy map for a given xarray DataArray.

    Parameters:
    - data (xr.DataArray): xarray DataArray with 'time', 'lat', 'lon'.
    - variable_label (str): Label for the variable to be shown on the colorbar.
    - save_path (str): Path to save the plot. If None, the plot is not saved.

    Returns:
    - None
    """

    # Define three-month periods
    months_periods = [
        [12, 1, 2],  # DJF
        [3, 4, 5],   # MAM
        [6, 7, 8],   # JJA
        [9, 10, 11]  # SON
    ]

    # Create a Cartopy GeoAxes grid
    fig, axes = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(12, 10))
    fig.subplots_adjust(hspace=0.5)

    # Flatten the 2D array of subplots for easy iteration
    axes_flat = axes.flatten()

    # Select and save three-month periods
    for i, months in enumerate(months_periods):
        # Select the three-month period
        selected_period = data.sel(time=data['time.month'].isin(months))

        # Plotting the data using contourf
        cf = axes_flat[i].contourf(selected_period['lon'], selected_period['lat'], selected_period.mean(dim='time'),
                                   transform=ccrs.PlateCarree(), cmap='viridis')

        # Add colorbar
        cbar = plt.colorbar(cf, ax=axes_flat[i], orientation='vertical', pad=0.1)
        cbar.set_label(f'{variable_label} {unit}')

        # Add coastlines, gridlines, etc.
        axes_flat[i].coastlines()
        axes_flat[i].gridlines(draw_labels=True)

        # Set the title
        axes_flat[i].set_title(f'Mean {variable_label} ({selected_period.time.values[0].strftime("%b")}-{selected_period.time.values[-1].strftime("%b")})')


    # Save the figure if save_dir is provided
    if save_dir:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        plt.savefig(os.path.join(save_dir, f'{variable_label.lower().replace(" ", "_")}_3_month_period_geoplot.png'), bbox_inches='tight')

    # Show the plot
    plt.show()

def plot_cartopy_monthly(data, variable_label, save_dir=None, unit=''):
    """
    Plot mean Cartopy maps for each quarter of the year for a given xarray DataArray.

    Parameters:
    - data (xr.DataArray): xarray DataArray with 'time', 'lat', 'lon'.
    - variable_label (str): Label for the variable to be shown on the colorbar.
    - save_path (str): Path to save the plots. If None, the plots are not saved.

    Returns:
    - None
    """

    # Define all months
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # Repeat the process four times for the entire year
    for plot_num in range(3):
        # Create a Cartopy GeoAxes grid for each plot
        fig, axes = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(12, 10))
        fig.subplots_adjust(hspace=0.5)

        # Flatten the 2D array of subplots for easy iteration
        axes_flat = axes.flatten()

        # Select and save each month for the current plot
        for i, month in enumerate(months[plot_num * 4: (plot_num + 1) * 4]):
            # Select the month
            selected_month = data.sel(time=data['time.month'] == month)

            # Plotting the data using contourf
            cf = axes_flat[i].contourf(selected_month['lon'], selected_month['lat'], selected_month.mean(dim='time'),
                                       transform=ccrs.PlateCarree(), cmap='viridis')

            # Add colorbar
            cbar = plt.colorbar(cf, ax=axes_flat[i], orientation='vertical', pad=0.1)
            cbar.set_label(f'{variable_label}')

            # Add coastlines, gridlines, etc.
            axes_flat[i].coastlines()
            axes_flat[i].gridlines(draw_labels=True)

            # Set the title
            axes_flat[i].set_title(f'Mean {variable_label} - {selected_month.time.values[0].strftime("%B")}')


        # Save the figure if save_dir is provided
        if save_dir:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            plt.savefig(os.path.join(save_dir, f'{variable_label.lower().replace(" ", "_")}_plot_quarter_{plot_num + 1}.png'), bbox_inches='tight')

        # Show the plot
        plt.show()